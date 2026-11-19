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

import hashlib
import json
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

# Blocchi piccoli (circa un paragrafo o poco più): DeepL rimescola meno i
# tag e la cache si riusa meglio quando cambia solo una parte di un capitolo.
CHUNK_TARGET_CHARS = 4_000
CHUNK_MAX_CHARS = 20_000          # DeepL accetta fino a 128 KiB per richiesta

# Cache delle traduzioni già pagate (una per lingua). In CI viene salvata con
# actions/cache anche quando la run fallisce, così non si ripaga la quota.
CACHE_DIR = Path(os.getenv("TRANSLATION_CACHE_DIR", ".translation_cache"))

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
    r"\\item\s*\[(?:[^\[\]{}]|\{[^{}]*\})*\]",               # \item[\textbf{1}]
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

class Chunk:
    """Un blocco XML da tradurre e gli id dei segnaposto che contiene."""
    def __init__(self) -> None:
        self.pieces: List[str] = []
        self.ids: List[int] = []

    @property
    def xml(self) -> str:
        return "".join(self.pieces)

    def has_text(self) -> bool:
        return bool(TAG_RE.sub("", self.xml).strip())


def build_chunks(tokens: List[Tuple[str, str]]) -> Tuple[List[Chunk], Dict[int, str]]:
    """Converte i token in blocchi XML da inviare a DeepL.
    Si taglia dopo un segnaposto con una riga vuota (fine paragrafo) appena
    il blocco supera CHUNK_TARGET_CHARS, o dopo un qualsiasi a capo se supera
    CHUNK_MAX_CHARS."""
    placeholders: Dict[int, str] = {}
    chunks: List[Chunk] = []
    cur = Chunk()
    size = 0
    for kind, value in tokens:
        if kind == "text":
            piece = xml_escape(XML_FORBIDDEN_CHARS.sub(" ", value))
        else:
            idx = len(placeholders)
            placeholders[idx] = value
            piece = f'<x id="{idx}"/>'
            cur.ids.append(idx)
        cur.pieces.append(piece)
        size += len(piece)
        if kind == "code" and (
            (size >= CHUNK_TARGET_CHARS and re.search(r"\n[ \t]*\n", value))
            or (size >= CHUNK_MAX_CHARS and "\n" in value)
        ):
            chunks.append(cur)
            cur, size = Chunk(), 0
    if cur.pieces:
        chunks.append(cur)
    return chunks, placeholders


def split_chunk(chunk: Chunk, placeholders: Dict[int, str]) -> List[Chunk]:
    """Divide un blocco in pezzi più piccoli, tagliando dopo ogni segnaposto
    che contiene un a capo (in pratica: una riga di sorgente alla volta)."""
    parts: List[Chunk] = []
    cur = Chunk()
    for piece in chunk.pieces:
        cur.pieces.append(piece)
        m = TAG_RE.fullmatch(piece)
        if m:
            idx = int(m.group(1))
            cur.ids.append(idx)
            if "\n" in placeholders[idx]:
                parts.append(cur)
                cur = Chunk()
    if cur.pieces:
        parts.append(cur)
    return parts


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


# ------------------------------------------------------------
# Cache
# ------------------------------------------------------------

_caches: Dict[str, Dict[str, str]] = {}


def _cache_file(lang: str) -> Path:
    return CACHE_DIR / f"{lang}.json"


def cache_for(lang: str) -> Dict[str, str]:
    if lang not in _caches:
        try:
            _caches[lang] = json.loads(_cache_file(lang).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            _caches[lang] = {}
    return _caches[lang]


def cache_key(xml: str, lang: str) -> str:
    return hashlib.sha256(f"{lang}\0{xml}".encode("utf-8")).hexdigest()


def save_cache(lang: str) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = _cache_file(lang).with_suffix(".tmp")
    tmp.write_text(json.dumps(cache_for(lang), ensure_ascii=False, indent=0), encoding="utf-8")
    tmp.replace(_cache_file(lang))


# ------------------------------------------------------------
# Controlli di struttura
# ------------------------------------------------------------

def brace_delta(code: str) -> int:
    """Quante graffe apre (+) o chiude (-) un pezzo di codice LaTeX."""
    code = _GROUP_SCAN_RE.sub(
        lambda m: m.group(0) if (m.group("open") or m.group("close")) else "", code)
    return code.count("{") - code.count("}")


def chunk_problem(translated: str, chunk: Chunk, placeholders: Dict[int, str],
                  start_depth: int, depth_before: Dict[int, int]) -> Optional[str]:
    """None se la traduzione di un blocco è strutturalmente valida, altrimenti
    il motivo. Ogni segnaposto deve comparire una volta sola e allo stesso
    livello di graffe che ha nel sorgente (DeepL può spostare una parola in
    grassetto, ma non far finire testo fuori o dentro un'altra graffa)."""
    ids = [int(i) for i in TAG_RE.findall(translated)]
    if sorted(ids) != sorted(chunk.ids):
        missing = set(chunk.ids) - set(ids)
        extra = [i for i in ids if ids.count(i) > 1 or i not in chunk.ids]
        return f"segnaposto mancanti {sorted(missing)[:5]} / in più {sorted(set(extra))[:5]}"
    depth = start_depth
    for idx in ids:
        if depth != depth_before[idx]:
            return f"ordine dei segnaposto cambiato vicino a {placeholders[idx].strip()[:40]!r}"
        depth += brace_delta(placeholders[idx])
    return None


# ------------------------------------------------------------
# Traduzione
# ------------------------------------------------------------

def deepl_translate(client: "deepl.DeepLClient", xml: str, lang: str,
                    stats: Dict[str, int]) -> str:
    cache = cache_for(lang)
    key = cache_key(xml, lang)
    if key in cache:
        stats["cached"] += 1
        return cache[key]
    try:
        res = client.translate_text(
            xml,
            source_lang="EN",
            target_lang=lang.upper(),
            formality="prefer_more",
            tag_handling="xml",
            ignore_tags=["x"],
            preserve_formatting=True,
        )
    except deepl.DeepLException as e:
        Path("debug_protected.txt").write_text(xml, encoding="utf-8")
        raise RuntimeError(f"Errore DeepL: {e} (blocco salvato in debug_protected.txt)") from e
    stats["requests"] += 1
    stats["chars"] += len(TAG_RE.sub("", xml))
    cache[key] = res.text
    save_cache(lang)
    return res.text


def translate_chunk(client, chunk: Chunk, placeholders: Dict[int, str], lang: str,
                    start_depth: int, depth_before: Dict[int, int],
                    stats: Dict[str, int], level: int = 0) -> str:
    """Traduce un blocco; se DeepL ne rovina la struttura lo ritraduce
    diviso in pezzi più piccoli (una riga alla volta)."""
    if not chunk.has_text():
        return chunk.xml
    translated = deepl_translate(client, chunk.xml, lang, stats)
    problem = chunk_problem(translated, chunk, placeholders, start_depth, depth_before)
    if problem is None:
        return translated
    parts = split_chunk(chunk, placeholders)
    if level >= 1 or len(parts) <= 1:
        raise RuntimeError(f"DeepL ha rovinato la struttura LaTeX: {problem}")
    stats["retried"] += 1
    out, depth = [], start_depth
    for part in parts:
        out.append(translate_chunk(client, part, placeholders, lang, depth,
                                   depth_before, stats, level + 1))
        depth += sum(brace_delta(placeholders[i]) for i in part.ids)
    return "".join(out)


def prepare(text: str) -> Tuple[List[Chunk], Dict[int, str], Dict[int, int]]:
    chunks, placeholders = build_chunks(tokenize(text))
    depth_before: Dict[int, int] = {}
    depth = 0
    for idx in sorted(placeholders):
        depth_before[idx] = depth
        depth += brace_delta(placeholders[idx])
    return chunks, placeholders, depth_before


def pending_chars(text: str, lang: str) -> int:
    """Caratteri (circa) che verranno inviati a DeepL: esclusi i blocchi già
    in cache."""
    chunks, _, _ = prepare(text)
    cache = cache_for(lang)
    return sum(len(TAG_RE.sub("", c.xml)) for c in chunks
               if c.has_text() and cache_key(c.xml, lang) not in cache)


def translate_text(client: "deepl.DeepLClient", text: str, target_lang: str,
                   stats: Optional[Dict[str, int]] = None) -> str:
    if not text.strip():
        return text
    stats = stats if stats is not None else {"cached": 0, "requests": 0, "chars": 0, "retried": 0}

    chunks, placeholders, depth_before = prepare(text)
    seen: Dict[int, int] = {}
    result: List[str] = []
    depth = 0
    for chunk in chunks:
        translated = translate_chunk(client, chunk, placeholders, target_lang,
                                     depth, depth_before, stats)
        result.append(restore_chunk(translated, placeholders, seen))
        depth += sum(brace_delta(placeholders[i]) for i in chunk.ids)

    missing = [i for i in placeholders if seen.get(i, 0) != 1]
    if missing:
        raise RuntimeError(f"DeepL ha alterato i segnaposto LaTeX (id {missing[:5]})")

    translated = "".join(result)
    # La struttura delle graffe ora è garantita uguale al sorgente, quindi le
    # righe vuote dentro {...} che il sorgente non ha le ha aggiunte DeepL
    # (dentro il testo) e si possono ridurre a un semplice a capo.
    if blank_lines_inside_groups(text) == 0:
        translated, fixed = fix_blank_lines_inside_groups(translated)
        if fixed:
            print(f"    ⚠️ Corrette {len(fixed)} righe vuote inserite da DeepL dentro {{...}}:")
            for f in fixed[:10]:
                print(f"       {f}")
    elif blank_lines_inside_groups(translated) != blank_lines_inside_groups(text):
        raise RuntimeError("DeepL ha cambiato le righe vuote dentro {...} (LaTeX non valido)")
    return translated


# ============================================================
# FILE
# ============================================================

def translate_file(client: "deepl.DeepLClient", source_file: Path,
                   target_dir: Path, lang: str, stats: Dict[str, int]) -> bool:
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / source_file.name

    print(f"  → Traduco {source_file.name} in {lang.upper()}...")
    content = source_file.read_text(encoding="utf-8")

    try:
        translated = translate_text(client, content, lang, stats)
    except Exception as e:
        print(f"    ❌ Errore: {e}")
        return False

    target_file.write_text(translated, encoding="utf-8")
    print(f"    ✅ Salvato: {target_file}")
    return True


# ============================================================
# MAIN
# ============================================================

def check_quota(client: "deepl.DeepLClient", needed: int) -> bool:
    try:
        usage = client.get_usage().character
    except deepl.DeepLException as e:
        print(f"⚠️ Impossibile leggere la quota DeepL ({e}), proseguo.")
        return True
    if not usage.valid or not usage.limit:
        return True
    left = usage.limit - usage.count
    print(f"Quota DeepL: usati {usage.count:,} / {usage.limit:,} caratteri, "
          f"disponibili {left:,}; da tradurre ~{needed:,}.")
    if needed > left:
        print("❌ Quota DeepL insufficiente: niente viene tradotto finché la quota non si "
              "rinnova (o non si passa a un piano superiore).")
        return False
    return True


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

    needed = sum(pending_chars(f.read_text(encoding="utf-8"), lang)
                 for f in source_files for lang in TARGET_LANGS)
    client = get_deepl_client()
    if needed and not check_quota(client, needed):
        return 1

    stats = {"cached": 0, "requests": 0, "chars": 0, "retried": 0}
    total_jobs = len(source_files) * len(TARGET_LANGS)
    success_count = 0
    for source_file in source_files:
        for lang, target_dir in TARGET_LANGS.items():
            if translate_file(client, source_file, target_dir, lang, stats):
                success_count += 1

    print(f"\nTraduzione completata: {success_count}/{total_jobs} file tradotti con successo.")
    print(f"Blocchi dalla cache: {stats['cached']}, richieste a DeepL: {stats['requests']} "
          f"(~{stats['chars']:,} caratteri), blocchi ritradotti a pezzi: {stats['retried']}.")
    return 0 if success_count == total_jobs else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
