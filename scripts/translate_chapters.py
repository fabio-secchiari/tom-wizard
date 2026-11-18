#!/usr/bin/env python3
"""
Traduce i capitoli inglesi verso tedesco e francese usando DeepL.

Strategia:
  1. Il sorgente LaTeX viene suddiviso in "testo" e "codice" (comandi,
     graffe, math, commenti, ambienti verbatim, ...).
  2. Il codice viene sostituito con tag XML vuoti <x id="N"/>, mentre il
     testo viene escapato per XML. Così DeepL (tag_handling="xml") vede i
     segnaposto come veri tag e non li traduce né li modifica.
  3. Dopo la traduzione si verifica che ogni segnaposto sia tornato
     esattamente una volta: se no, il file NON viene sovrascritto e lo
     script termina con codice d'uscita != 0.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from xml.sax.saxutils import escape as xml_escape, unescape as xml_unescape

import deepl
from dotenv import load_dotenv

# ============================================================
# CONFIGURAZIONE
# ============================================================

load_dotenv()

SOURCE_DIR = Path("chapters")
TARGET_LANGS = {
    "de": Path("chapters_de"),
    "fr": Path("chapters_fr"),
}

# DeepL accetta richieste fino a 128 KiB: restiamo molto sotto.
MAX_CHUNK_CHARS = 20_000

# ============================================================
# TOKENIZZAZIONE LATEX
# ============================================================

# Comandi il cui PRIMO argomento è codice (path, label, url, ...) e
# non va tradotto.
CODE_ARG_COMMANDS = (
    "label|ref|pageref|eqref|cref|Cref|autoref|cite|citep|citet|"
    "includegraphics|url|href|input|include|bibliography|addbibresource|"
    "iconbox|lstinputlisting|hyperref|nameref"
)

LATEX_CODE = re.compile(
    r"""
      \\begin\{(?P<verb>verbatim\*?|lstlisting|minted|equation\*?|align\*?)\}
          .*?\\end\{(?P=verb)\}                        # ambienti da non toccare
    | (?<!\\)%[^\n]*\n?                                # commenti (con il newline!)
    | \\\[.*?\\\]                                      # math display
    | \\\(.*?\\\)                                      # math inline \( \)
    | (?<!\\)\$[^$]*\$                                 # math inline $ $
    | \\begin\{[^{}]*\}(?:\[[^\]]*\])*                 # \begin{env}[opt]
          (?:\{(?:[^{}]|\{[^{}]*\})*\})?               #   {width} di subfigure ecc.
    | \\end\{[^{}]*\}
    | \\(?:""" + CODE_ARG_COMMANDS + r""")\*?
          (?:\[[^\]]*\])*\{[^{}]*\}                    # \cmd[opt]{codice}
    | \\[a-zA-Z@]+\*?                                  # qualsiasi altro comando
    | \\[^a-zA-Z]                                      # \\ \& \% \_ \, ...
    | [{}~&]                                           # graffe, spazi fissi, tab
    """,
    re.VERBOSE | re.DOTALL,
)

TAG_RE = re.compile(r'<x\s+id\s*=\s*"(\d+)"\s*/>')


def tokenize(text: str) -> List[Tuple[str, str]]:
    """Restituisce una lista di (tipo, contenuto), tipo in {"text", "code"}.

    Pezzi di codice adiacenti (anche separati solo da spazi/newline)
    vengono uniti in un unico segnaposto, per ridurre il numero di tag.
    """
    tokens: List[Tuple[str, str]] = []
    pos = 0
    for m in LATEX_CODE.finditer(text):
        if m.start() > pos:
            tokens.append(("text", text[pos:m.start()]))
        tokens.append(("code", m.group(0)))
        pos = m.end()
    if pos < len(text):
        tokens.append(("text", text[pos:]))

    merged: List[Tuple[str, str]] = []
    for kind, value in tokens:
        if merged and merged[-1][0] == "code" and (
            kind == "code" or (kind == "text" and not value.strip())
        ):
            merged[-1] = ("code", merged[-1][1] + value)
        elif kind == "code" and len(merged) >= 2 and merged[-1][0] == "text" \
                and not merged[-1][1].strip() and merged[-2][0] == "code":
            ws = merged.pop()[1]
            merged[-1] = ("code", merged[-1][1] + ws + value)
        else:
            merged.append((kind, value))
    return merged


# ============================================================
# SANITIZZAZIONE
# ============================================================

# Caratteri NON consentiti in XML 1.0
XML_FORBIDDEN_CHARS = re.compile(
    "[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]"
)

# Caratteri che DeepL inserisce (tipografia FR/DE) e che pdflatex non gestisce
OUTPUT_REPLACEMENTS = {
    "\u202f": "~",  # narrow no-break space (es. « Texte », d. h.)
    "\u00a0": "~",  # no-break space
    "\u2009": " ",  # thin space
    "\u2011": "-",  # non-breaking hyphen
}


def clean_output(text: str) -> str:
    for src, dst in OUTPUT_REPLACEMENTS.items():
        text = text.replace(src, dst)
    return text


# ============================================================
# PROTEZIONE / RIPRISTINO
# ============================================================

def build_chunks(tokens: List[Tuple[str, str]]) -> Tuple[List[str], Dict[int, str]]:
    """Converte i token in blocchi XML da inviare a DeepL."""
    placeholders: Dict[int, str] = {}
    chunks: List[str] = []
    current: List[str] = []
    size = 0

    for kind, value in tokens:
        if kind == "text":
            piece = xml_escape(XML_FORBIDDEN_CHARS.sub(" ", value))
        else:
            idx = len(placeholders)
            placeholders[idx] = value
            piece = f'<x id="{idx}"/>'
        current.append(piece)
        size += len(piece)

        # Taglio solo dopo un segnaposto che contiene un newline
        if kind == "code" and "\n" in value and size >= MAX_CHUNK_CHARS:
            chunks.append("".join(current))
            current, size = [], 0

    if current:
        chunks.append("".join(current))
    return chunks, placeholders


def restore_chunk(translated: str, placeholders: Dict[int, str],
                  seen: Dict[int, int]) -> str:
    out: List[str] = []
    pos = 0
    for m in TAG_RE.finditer(translated):
        out.append(clean_output(xml_unescape(translated[pos:m.start()])))
        idx = int(m.group(1))
        seen[idx] = seen.get(idx, 0) + 1
        out.append(placeholders.get(idx, ""))
        pos = m.end()
    out.append(clean_output(xml_unescape(translated[pos:])))
    return "".join(out)


# ============================================================
# DEEPL
# ============================================================

def get_deepl_client() -> deepl.Translator:
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        print("❌ DEEPL_API_KEY non trovata")
        sys.exit(1)
    return deepl.Translator(api_key)


def translate_text(client: deepl.Translator, text: str, target_lang: str) -> str:
    if not text.strip():
        return text

    chunks, placeholders = build_chunks(tokenize(text))
    seen: Dict[int, int] = {}
    result: List[str] = []

    for chunk in chunks:
        if not TAG_RE.sub("", chunk).strip():
            # solo codice: niente da tradurre
            result.append(restore_chunk(chunk, placeholders, seen))
            continue
        try:
            res = client.translate_text(
                chunk,
                source_lang="EN",
                target_lang=target_lang.upper(),
                formality="prefer_more",
                tag_handling="xml",
                ignore_tags=["x"],
                preserve_formatting=True,
            )
        except deepl.DeepLException as e:
            Path("debug_protected.txt").write_text(chunk, encoding="utf-8")
            raise RuntimeError(f"Errore DeepL: {e} (blocco salvato in debug_protected.txt)") from e
        result.append(restore_chunk(res.text, placeholders, seen))

    missing = [i for i in placeholders if seen.get(i, 0) == 0]
    duplicated = [i for i, n in seen.items() if n > 1]
    unknown = [i for i in seen if i not in placeholders]
    if missing or duplicated or unknown:
        details = "; ".join(
            f"{name}: " + ", ".join(repr(placeholders.get(i, "?"))[:60] for i in ids[:5])
            for name, ids in (("mancanti", missing), ("duplicati", duplicated),
                              ("sconosciuti", unknown))
            if ids
        )
        raise RuntimeError(f"DeepL ha alterato i segnaposto LaTeX ({details})")

    return "".join(result)


# ============================================================
# FILE
# ============================================================

def translate_file(client: deepl.Translator, source_file: Path,
                   target_dir: Path, lang: str) -> bool:
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / source_file.name

    print(f"  → Traduco {source_file.name} in {lang.upper()}...")
    content = source_file.read_text(encoding="utf-8")

    try:
        translated = translate_text(client, content, lang)
    except Exception as e:
        print(f"    ❌ Errore: {e}")
        return False

    target_file.write_text(translated, encoding="utf-8")
    print(f"    ✅ Salvato: {target_file}")
    return True


# ============================================================
# MAIN
# ============================================================

def main(files_to_translate: Optional[List[str]] = None) -> int:
    if files_to_translate:
        source_files = [SOURCE_DIR / name for name in files_to_translate]
    else:
        source_files = sorted(SOURCE_DIR.glob("*.tex"))

    print("File da tradurre:", [f.name for f in source_files])
    source_files = [f for f in source_files if f.exists() or
                    print(f"⚠️ File non trovato (eliminato?): {f}")]
    if not source_files:
        print("⚠️ Nessun file da tradurre.")
        return 0

    client = get_deepl_client()
    total_jobs = len(source_files) * len(TARGET_LANGS)
    success_count = 0

    for source_file in source_files:
        for lang, target_dir in TARGET_LANGS.items():
            if translate_file(client, source_file, target_dir, lang):
                success_count += 1

    print(f"\nTraduzione completata: {success_count}/{total_jobs} file tradotti con successo.")
    return 0 if success_count == total_jobs else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
