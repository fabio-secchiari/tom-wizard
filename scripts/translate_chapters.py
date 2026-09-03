#!/usr/bin/env python3
"""
Traduce i capitoli inglesi verso DE e FR usando DeepL.
Protegge i comandi LaTeX il più possibile.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

import deepl
from dotenv import load_dotenv

# Carica .env se esiste (per uso locale)
load_dotenv()

# === CONFIGURAZIONE ===
SOURCE_DIR = Path("chapters")          # inglese (source of truth)
TARGET_LANGS = {
    "de": Path("chapters_de"),
    "fr": Path("chapters_fr"),
}
# In futuro aggiungi: "it": Path("chapters_it"),

import re
from typing import List, Tuple

# ============================================================
# PROTEZIONE LATEX MIGLIORATA
# ============================================================

def find_balanced_brace_content(text: str, start: int) -> int:
    """Trova la posizione della graffa chiusa bilanciata a partire da start."""
    if start >= len(text) or text[start] != '{':
        return -1
    depth = 0
    i = start
    while i < len(text):
        if text[i] == '{':
            depth += 1
        elif text[i] == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def protect_latex(text: str) -> Tuple[str, List[str]]:
    """
    Protegge SOLO le parti che non devono essere tradotte.
<<<<<<< HEAD
    Lascia passare \\textbf, \\textit, \\section, ecc. così DeepL può tradurre il contenuto.
=======
    Lascia passare \textbf, \textit, \section, ecc. così DeepL può tradurre il contenuto.
>>>>>>> 96ae8e5999ba65b3a3cdd19cf6a5e034380f084d
    """
    placeholders: List[str] = []
    
    def protect(match):
        placeholders.append(match.group(0))
        return f'<ph id="{len(placeholders)-1}"/>'

    # Ordine importante: prima le cose più lunghe/specifiche
    patterns = [
        # Math display
        r'\\\[.*?\\\]',
        r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}',
        r'\\begin\{align\*?\}.*?\\end\{align\*?\}',
        
        # Math inline
        r'\$[^\$]+\$',
        r'\\\([^\)]+\\\)',
        
        # Comandi che NON devono essere toccati (argomenti non testuali)
        r'\\(?:label|ref|cref|Cref|pageref|cite|citep|includegraphics|url|href|input|include|bibliography|addbibresource)(?:\[[^\]]*\])?\{[^}]*\}',
        
        # Commenti
        r'%.*$',
    ]

    protected = text
    for pattern in patterns:
        protected = re.sub(pattern, protect, protected, flags=re.DOTALL | re.MULTILINE)

    return protected, placeholders


def restore_latex(text: str, placeholders: List[str]) -> str:
    for i, original in enumerate(placeholders):
        text = text.replace(f'<ph id="{i}"/>', original)
    return text


def translate_text(client: deepl.Translator, text: str, target_lang: str) -> str:
    if not text.strip():
        return text

    protected_text, placeholders = protect_latex(text)

    result = client.translate_text(
        protected_text,
        source_lang="EN",
        target_lang=target_lang.upper(),
        formality="prefer_more",
        tag_handling="xml",
        ignore_tags=["ph"],
        # split_sentences="none"  # a volte aiuta con LaTeX, prova se serve
    )

    translated = result.text
    return restore_latex(translated, placeholders)

def get_deepl_client() -> deepl.Translator:
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        print("❌ DEEPL_API_KEY non trovata (né in .env né come variabile d'ambiente)")
        sys.exit(1)
    return deepl.Translator(api_key)


def translate_file(client: deepl.Translator, source_file: Path, target_dir: Path, lang: str):
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / source_file.name

    print(f"  → Traduco {source_file.name} in {lang.upper()}...")

    content = source_file.read_text(encoding="utf-8")
    translated = translate_text(client, content, lang)

    target_file.write_text(translated, encoding="utf-8")
    print(f"    Salvato: {target_file}")


def main(files_to_translate: List[str] = None):
    client = get_deepl_client()

    if files_to_translate:
        source_files = [SOURCE_DIR / f for f in files_to_translate]
    else:
        # Se non vengono passati file, traduce tutto (utile la prima volta)
        source_files = sorted(SOURCE_DIR.glob("*.tex"))

    print(f"File da tradurre: {[f.name for f in source_files]}")

    for source_file in source_files:
        if not source_file.exists():
            print(f"⚠️  File non trovato: {source_file}")
            continue

        for lang, target_dir in TARGET_LANGS.items():
            translate_file(client, source_file, target_dir, lang)

    print("\n✅ Traduzione completata")


if __name__ == "__main__":
    # Se viene chiamato con argomenti, traduce solo quei file
    files = sys.argv[1:] if len(sys.argv) > 1 else None
    main(files)