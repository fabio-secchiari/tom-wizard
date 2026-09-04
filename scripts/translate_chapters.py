#!/usr/bin/env python3
"""
Traduce i capitoli inglesi verso tedesco e francese usando DeepL.

Source of truth:
    src/chapters/

Traduzioni generate:
    src/chapters_de/
    src/chapters_fr/
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

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


# ============================================================
# PROTEZIONE DEL CONTENUTO LATEX
# ============================================================

def protect_latex(text: str) -> Tuple[str, List[str]]:
    """
    Protegge le parti che non devono essere tradotte.

    I comandi di formattazione come \\textbf{}, \\textit{},
    \\section{} ecc. vengono lasciati passare affinché DeepL
    possa tradurre il loro contenuto.
    """

    placeholders: List[str] = []

    def protect(match):
        placeholders.append(match.group(0))
        return f'<ph id="{len(placeholders) - 1}"/>'

    patterns = [
        # Display math
        r'\\\[.*?\\\]',
        r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}',
        r'\\begin\{align\*?\}.*?\\end\{align\*?\}',

        # Inline math
        r'\$[^\$]+\$',
        r'\\\([^\)]+\\\)',

        # Comandi e riferimenti che non devono essere tradotti
        r'\\(?:label|ref|cref|Cref|pageref|cite|citep|'
        r'includegraphics|url|href|input|include|'
        r'bibliography|addbibresource)'
        r'(?:\[[^\]]*\])?\{[^}]*\}',

        # Commenti
        r'%.*$',
    ]

    protected = text

    for pattern in patterns:
        protected = re.sub(
            pattern,
            protect,
            protected,
            flags=re.DOTALL | re.MULTILINE,
        )

    return protected, placeholders


def restore_latex(text: str, placeholders: List[str]) -> str:
    """Ripristina il contenuto LaTeX protetto."""

    for i, original in enumerate(placeholders):
        text = text.replace(
            f'<ph id="{i}"/>',
            original,
        )

    return text


# ============================================================
# DEEPL
# ============================================================

def get_deepl_client() -> deepl.Translator:
    api_key = os.getenv("DEEPL_API_KEY")

    if not api_key:
        print(
            "❌ DEEPL_API_KEY non trovata "
            "(né in .env né come variabile d'ambiente)"
        )
        sys.exit(1)

    return deepl.Translator(api_key)


def translate_text(
    client: deepl.Translator,
    text: str,
    target_lang: str,
) -> str:

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
    )

    return restore_latex(
        result.text,
        placeholders,
    )


# ============================================================
# FILE
# ============================================================

def translate_file(
    client: deepl.Translator,
    source_file: Path,
    target_dir: Path,
    lang: str,
):

    target_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    target_file = target_dir / source_file.name

    print(
        f"  → Traduco {source_file.name} "
        f"in {lang.upper()}..."
    )

    content = source_file.read_text(
        encoding="utf-8"
    )

    translated = translate_text(
        client,
        content,
        lang,
    )

    target_file.write_text(
        translated,
        encoding="utf-8",
    )

    print(
        f"    Salvato: {target_file}"
    )


# ============================================================
# MAIN
# ============================================================

def main(files_to_translate: List[str] | None = None):

    client = get_deepl_client()

    if files_to_translate:

        source_files = [
            SOURCE_DIR / filename
            for filename in files_to_translate
        ]

    else:

        # Senza argomenti traduce tutti i capitoli
        source_files = sorted(
            SOURCE_DIR.glob("*.tex")
        )

    print(
        "File da tradurre:",
        [file.name for file in source_files],
    )

    if not source_files:
        print("⚠️ Nessun file da tradurre.")
        return

    for source_file in source_files:

        if not source_file.exists():

            print(
                f"⚠️ File non trovato: {source_file}"
            )

            continue

        for lang, target_dir in TARGET_LANGS.items():

            translate_file(
                client,
                source_file,
                target_dir,
                lang,
            )

    print("\n✅ Traduzione completata")


if __name__ == "__main__":

    files = (
        sys.argv[1:]
        if len(sys.argv) > 1
        else None
    )

    main(files)