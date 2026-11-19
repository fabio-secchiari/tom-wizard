#!/usr/bin/env python3
"""
Traduce i capitoli inglesi verso tedesco e francese usando DeepL.

Strategia:
  1. Il sorgente LaTeX viene suddiviso in "testo" e "codice" (comandi,
     graffe, math, commenti, ambienti verbatim, ...). Anche password e
     nomi di file con underscore (GIVE\\_ME\\_DF!, ESP32\\_Fw23.bin),
     percorsi/topic MQTT (cmnd/<...>/Power) e il contenuto di \\texttt{}
     sono "codice": DeepL non li vede proprio.
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

# "Parole" da copiare così come sono: password e nomi file con underscore
# (GIVE\_ME\_DF!, ESP32\_Fw23.bin, your\_~Tasmota\_~topic\_~name) e
# percorsi / topic MQTT (cmnd/<...>/Power, /dev/ttyUSB0, \%prefix\%/\%topic\%/).
_WORD_CHAR = r"(?:[\w.!+\-@<>]|\\%|~(?=[\w<\\]))"
_WORD_JOIN = r"(?:\\_|\\textunderscore(?:\{\}|\s)?|/)"
WORD = rf"(?P<word>{_WORD_CHAR}*(?:{_WORD_JOIN}{_WORD_CHAR}*)+)"

_LATEX_PARTS = [
    r"""\\begin\{(?P<verb>verbatim\*?|lstlisting|minted|equation\*?|align\*?)\}
          .*?\\end\{(?P=verb)\}""",                     # ambienti da non toccare
    r"(?<!\\)%[^\n]*\n?",                               # commenti (con il newline!)
    r"\\\[.*?\\\]",                                     # math display
    r"\\\(.*?\\\)",                                     # math inline \( \)
    r"(?<!\\)\$[^$]*\$",                                # math inline $ $
    r"""\\begin\{[^{}]*\}(?:\[[^\]]*\])*
          (?:\{(?:[^{}]|\{[^{}]*\})*\})?""",            # \begin{env}[opt]{width}
    r"\\end\{[^{}]*\}",
    r"\\(?:" + CODE_ARG_COMMANDS + r")\*?(?:\[[^\]]*\])*\{[^{}]*\}",  # \cmd{codice}
    r"\\texttt\{[^{}]*\}",                              # monospaziato = codice
    r"\\verb\*?(?P<delim>[^a-zA-Z\s]).*?(?P=delim)",    # \verb|...|
    WORD,                                               # password, file, percorsi
    r"\\[a-zA-Z@]+\*?",                                 # qualsiasi altro comando
    r"\\[^a-zA-Z]",                                     # \\ \& \% \_ \, ...
    r"[{}~&]",                                          # graffe, spazi fissi, tab
]
LATEX_CODE = re.compile("|".join(_LATEX_PARTS), re.VERBOSE | re.DOTALL)
LATEX_CODE_NO_WORD = re.compile(
    "|".join(x for x in _LATEX_PARTS if x is not WORD), re.VERBOSE | re.DOTALL)


def is_verbatim_word(word: str) -> bool:
    """True se la "parola" va copiata identica (non tradotta)."""
    if re.search(r"\\_|\\textunderscore", word):
        return True                                     # GIVE\_ME\_DF!
    if word.count("/") >= 2 and (
        word.startswith("/") or re.search(r"[<>@\d A-Z]|\\%", word)
    ):
        return True                                     # cmnd/<...>/Power, /dev/x
    return False                                        # and/or, low/medium/high


TAG_RE = re.compile(r'<x\s+id\s*=\s*"(\d+)"\s*/>')


def tokenize(text: str) -> List[Tuple[str, str]]:
    """Restituisce una lista di (tipo, contenuto), tipo in {"text", "code"}.

    Pezzi di codice adiacenti (anche separati solo da spazi/newline)
    vengono uniti in un unico segnaposto, per ridurre il numero di tag.
    """
    tokens: List[Tuple[str, str]] = []

    def scan(chunk: str, regex: "re.Pattern[str]") -> None:
        pos = 0
        for m in regex.finditer(chunk):
            if m.start() > pos:
                tokens.append(("text", chunk[pos:m.start()]))
            if m.lastgroup == "word" and not is_verbatim_word(m.group(0)):
                scan(m.group(0), LATEX_CODE_NO_WORD)    # parola normale: traducibile
            else:
                tokens.append(("code", m.group(0)))
            pos = m.end()
        if pos < len(chunk):
            tokens.append(("text", chunk[pos:]))

    scan(text, LATEX_CODE)

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

    # Gli spazi/a capo ai bordi del testo diventano parte dei segnaposto
    # vicini: così la struttura (righe vuote = paragrafi!) resta quella del
    # sorgente anche se DeepL sposta o aggiunge spazi attorno ai tag.
    for i, (kind, value) in enumerate(merged):
        if kind != "text":
            continue
        if i > 0 and merged[i - 1][0] == "code":
            lead = value[:len(value) - len(value.lstrip())]
            merged[i - 1] = ("code", merged[i - 1][1] + lead)
            value = value[len(lead):]
        if i + 1 < len(merged) and merged[i + 1][0] == "code":
            trail = value[len(value.rstrip()):]
            merged[i + 1] = ("code", trail + merged[i + 1][1])
            value = value[:len(value) - len(trail)]
        merged[i] = ("text", value)
    return [(k, v) for k, v in merged if v]


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
    """Rimette il codice al posto dei tag. Gli spazi che DeepL lascia
    accanto a un tag vengono scartati: quelli giusti sono già dentro il
    segnaposto (vedi tokenize)."""
    parts = TAG_RE.split(translated)        # testo, id, testo, id, ..., testo
    out: List[str] = []
    for i in range(0, len(parts), 2):
        piece = parts[i]
        if i > 0:
            piece = piece.lstrip()          # dopo un tag
        if i + 1 < len(parts):
            piece = piece.rstrip()          # prima di un tag
        out.append(clean_output(xml_unescape(piece)))
        if i + 1 < len(parts):
            idx = int(parts[i + 1])
            seen[idx] = seen.get(idx, 0) + 1
            out.append(placeholders.get(idx, ""))
    return "".join(out)


_GROUP_SCAN_RE = re.compile(
    r"(?P<skip>\\begin\{(verbatim\*?|lstlisting|minted)\}.*?\\end\{\2\}"  # verbatim
    r"|(?<!\\)%[^\n]*"                                                  # commenti
    r"|\\[{}\\])"                                                       # \{ \} \\
    r"|(?P<open>\{)|(?P<close>\})"
    r"|(?P<blank>\n[ \t]*\n(?:[ \t]*\n)*)",
    re.DOTALL)


def fix_blank_lines_inside_groups(text: str) -> Tuple[str, List[str]]:
    """Le righe vuote dentro {...} in LaTeX sono un errore
    (es. \\chapter*{ <riga vuota> Vorwort}) e pandoc si blocca.
    Le sostituisce con un semplice a capo e restituisce (testo, contesti)."""
    out: List[str] = []
    fixed: List[str] = []
    depth = pos = 0
    for m in _GROUP_SCAN_RE.finditer(text):
        out.append(text[pos:m.start()])
        tok = m.group(0)
        if m.group("open"):
            depth += 1
        elif m.group("close"):
            depth = max(0, depth - 1)
        elif m.group("blank") and depth > 0:
            line = text.count("\n", 0, m.start()) + 1
            ctx = text[max(0, m.start() - 40):m.end() + 40].replace("\n", "⏎")
            fixed.append(f"riga {line}: …{ctx}…")
            tok = "\n"
        out.append(tok)
        pos = m.end()
    out.append(text[pos:])
    return "".join(out), fixed


def blank_lines_inside_groups(text: str) -> int:
    return len(fix_blank_lines_inside_groups(text)[1])


# ============================================================
# DEEPL
# ============================================================

def get_deepl_client() -> "deepl.DeepLClient":
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        print("❌ DEEPL_API_KEY non trovata")
        sys.exit(1)
    return deepl.DeepLClient(api_key)


def translate_text(client: "deepl.DeepLClient", text: str, target_lang: str) -> str:
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

    translated = "".join(result)
    if blank_lines_inside_groups(translated) > blank_lines_inside_groups(text):
        if blank_lines_inside_groups(text):
            # Il sorgente ne ha già: non sappiamo quali siano volute.
            raise RuntimeError("DeepL ha inserito righe vuote dentro {...} (LaTeX non valido)")
        # Nel sorgente non ce ne sono: tutte quelle presenti le ha aggiunte
        # DeepL e si possono ridurre a un semplice a capo.
        translated, fixed = fix_blank_lines_inside_groups(translated)
        print(f"    ⚠️ Corrette {len(fixed)} righe vuote inserite da DeepL dentro {{...}}:")
        for f in fixed[:10]:
            print(f"       {f}")
    return translated


# ============================================================
# FILE
# ============================================================

def translate_file(client: "deepl.DeepLClient", source_file: Path,
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
