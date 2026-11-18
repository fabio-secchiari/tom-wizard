#!/usr/bin/env python3
"""
Genera markdown/index.md, index_de.md, index_fr.md dai sorgenti LaTeX con pandoc
(file usati dal sito web).

Prima di passare il testo a pandoc:
  - risolve \\langdir e tutti gli \\input/\\include (pandoc non capisce la macro);
  - trasforma \\iconbox{img}{titolo}{testo} in un blocco "::: tcolorbox" (come prima) con
    immagine + titolo in grassetto + descrizione (pandoc da solo convertiva la
    tabella interna perdendo titolo e testo);
  - normalizza le opzioni di \\includegraphics[...]: su una riga sola (pandoc 3.1
    non legge quelle su più righe), \\textwidth/\\linewidth -> percentuale,
    via le altezze in \\textheight e keepaspectratio (non hanno senso sul web).

Le figure escono come <figure><img ...> HTML (markdown-implicit_figures),
come nei Markdown usati finora dal sito.

Dopo pandoc controlla che nel Markdown non sia rimasto nessun comando LaTeX
non convertito e che i caratteri speciali (es. GIVE_ME_DF!) siano intatti.
"""
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
LANGS = {"en": ("chapters", "index.md"),
         "de": ("chapters_de", "index_de.md"),
         "fr": ("chapters_fr", "index_fr.md")}

INPUT_RE = re.compile(r"(?<!\\)\\(?:input|include)\{([^}]+)\}")
GRAPHICS_OPTS_RE = re.compile(r"(\\includegraphics\s*)\[([^\]]*)\]", re.DOTALL)

# Stringhe che DEVONO comparire nel Markdown inglese (regressioni già viste)
MUST_CONTAIN = ["GIVE_ME_DF!", "ESP32_Fw23.bin", "flash_download_tool_x.x.x.zip", "°C"]


# ------------------------------------------------------------------
# Utilità LaTeX
# ------------------------------------------------------------------

def read_group(text: str, pos: int) -> Optional[Tuple[str, int]]:
    """Legge un gruppo {...} bilanciato a partire da pos (saltando spazi).
    Restituisce (contenuto, posizione dopo la '}') oppure None."""
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != "{":
        return None
    depth, i = 0, pos
    while i < len(text):
        c = text[i]
        if c == "\\":
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[pos + 1:i], i + 1
        i += 1
    return None


def replace_iconbox(text: str) -> str:
    out: List[str] = []
    pos = 0
    for m in re.finditer(r"\\iconbox(?![a-zA-Z])", text):
        if m.start() < pos:
            continue
        args, p = [], m.end()
        for _ in range(3):
            g = read_group(text, p)
            if g is None:
                break
            args.append(g[0].strip())
            p = g[1]
        if len(args) != 3:
            continue
        img, title, body = args
        out.append(text[pos:m.start()])
        out.append(
            "\\begin{tcolorbox}\n"
            f"\\includegraphics[height=8mm]{{{img}}} \\textbf{{{title}}}\\\\\n"
            f"{body}\n"
            "\\end{tcolorbox}\n"
        )
        pos = p
    out.append(text[pos:])
    return "".join(out)


def normalize_graphics_opts(m: re.Match) -> str:
    opts = []
    for opt in re.sub(r"\s+", "", m.group(2)).split(","):
        if not opt or opt == "keepaspectratio" or "\\textheight" in opt:
            continue
        key, _, val = opt.partition("=")
        rel = re.fullmatch(r"([\d.]*)\\(?:textwidth|linewidth|columnwidth)", val)
        if rel:
            factor = float(rel.group(1) or 1)
            val = f"{factor:g}\\textwidth"   # pandoc lo converte in percentuale
        opts.append(f"{key}={val}" if val else key)
    return m.group(1) + ("[" + ",".join(opts) + "]" if opts else "")


def flatten(path: Path, langdir: str) -> str:
    text = path.read_text(encoding="utf-8")
    text = re.sub(r"^\\providecommand\{\\langdir\}.*$", "", text, flags=re.M)
    text = text.replace(r"\langdir", langdir)

    def inline(m: re.Match) -> str:
        target = ROOT / m.group(1).strip()
        if target.suffix != ".tex":
            target = target.with_suffix(".tex")
        if not target.exists():
            return m.group(0)
        return flatten(target, langdir)

    return INPUT_RE.sub(inline, text)


def preprocess(langdir: str) -> str:
    text = flatten(ROOT / "main.tex", langdir)
    text = replace_iconbox(text)
    return GRAPHICS_OPTS_RE.sub(normalize_graphics_opts, text)


# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------

def check_output(lang: str, md: str) -> List[str]:
    problems = []
    leftovers = sorted(set(re.findall(r"\\(?:textunderscore|textdegree|textwidth|textheight|linewidth|iconbox)\b", md)))
    if leftovers:
        problems.append(f"comandi LaTeX rimasti nel Markdown: {leftovers}")
    if lang == "en":
        problems += [f"manca '{s}'" for s in MUST_CONTAIN if s not in md]
    return problems


def main() -> int:
    out_dir = ROOT / "markdown"
    out_dir.mkdir(exist_ok=True)
    failed = False
    for lang, (langdir, out_name) in LANGS.items():
        res = subprocess.run(
            ["pandoc", "-f", "latex", "-t", "markdown-implicit_figures", "--wrap=none"],
            input=preprocess(langdir), text=True, cwd=ROOT, capture_output=True)
        if res.returncode != 0:
            print(f"❌ pandoc ({lang}): {res.stderr.strip()}")
            failed = True
            continue
        (out_dir / out_name).write_text(res.stdout, encoding="utf-8")
        problems = check_output(lang, res.stdout)
        if problems:
            failed = True
            print(f"❌ markdown/{out_name}: " + "; ".join(problems))
        else:
            print(f"✅ markdown/{out_name}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
