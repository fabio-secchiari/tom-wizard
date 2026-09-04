#!/usr/bin/env python3
"""
Traduce i capitoli inglesi verso tedesco e francese usando DeepL.
Versione definitiva con sanitizzazione XML e debug.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional

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
    placeholders: List[str] = []
    lines = text.splitlines(keepends=True)
    protected_lines = []

    protect_patterns = [
        (r'\\\[.*?\\\]', re.DOTALL),
        (r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}', re.DOTALL),
        (r'\\begin\{align\*?\}.*?\\end\{align\*?\}', re.DOTALL),
        (r'\$[^\$]+\$', 0),
        (r'\\\([^\)]+\\\)', 0),
        (r'\\(?:label|ref|cref|Cref|pageref|cite|citep|includegraphics|url|href|input|include|bibliography|addbibresource)(?:\[[^\]]*\])?\{[^}]*\}', 0),
        (r'\\begin\{([^}]*)\}', 0),
        (r'\\end\{([^}]*)\}', 0),
    ]

    for line in lines:
        def protect_comment(match):
            comment = match.group(0)
            if match.group(1) and match.group(1).endswith('\\'):
                return match.group(0)
            placeholders.append(comment)
            return f'<ph id="{len(placeholders)-1}"/>'

        line = re.sub(r'(?<!\\)%.*$', protect_comment, line)

        for pattern, flags in protect_patterns:
            if not (flags & re.DOTALL):
                def repl(match):
                    placeholders.append(match.group(0))
                    return f'<ph id="{len(placeholders)-1}"/>'
                line = re.sub(pattern, repl, line, flags=flags)

        protected_lines.append(line)

    protected_text = ''.join(protected_lines)

    multi_patterns = [
        (r'\\\[.*?\\\]', re.DOTALL),
        (r'\\begin\{equation\*?\}.*?\\end\{equation\*?\}', re.DOTALL),
        (r'\\begin\{align\*?\}.*?\\end\{align\*?\}', re.DOTALL),
    ]
    for pattern, flags in multi_patterns:
        def repl_multi(match):
            placeholders.append(match.group(0))
            return f'<ph id="{len(placeholders)-1}"/>'
        protected_text = re.sub(pattern, repl_multi, protected_text, flags=flags)

    return protected_text, placeholders

def restore_latex(text: str, placeholders: List[str]) -> str:
    for i, original in enumerate(placeholders):
        text = text.replace(f'<ph id="{i}"/>', original)
    return text

# ============================================================
# SANITIZZAZIONE XML (NUOVA)
# ============================================================

# XML 1.0 caratteri consentiti
XML_ALLOWED_CHARS = re.compile(
    r'[^\x09\x0A\x0D\x20-\uD7FF\uE000-\uFFFD\u10000-\u10FFFF]'
)

def sanitize_for_xml(text: str) -> str:
    """Rimuove i caratteri non consentiti in XML 1.0."""
    return XML_ALLOWED_CHARS.sub(' ', text)

def escape_xml(text: str) -> str:
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text

def unescape_xml(text: str) -> str:
    text = text.replace('&amp;', '&')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    return text

# ============================================================
# DEEPL CLIENT
# ============================================================

def get_deepl_client() -> deepl.Translator:
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        print("❌ DEEPL_API_KEY non trovata")
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

    # ---- SANITIZZAZIONE ----
    # Rimuove caratteri non XML (es. caratteri di controllo)
    protected_text = sanitize_for_xml(protected_text)

    # ---- ESCAPING XML ----
    protected_text = escape_xml(protected_text)

    try:
        result = client.translate_text(
            protected_text,
            source_lang="EN",
            target_lang=target_lang.upper(),
            formality="prefer_more",
            tag_handling="xml",
            ignore_tags=["ph"],
        )
    except deepl.DeepLException as e:
        # Se ancora fallisce, salviamo il testo protetto per debug
        debug_file = Path("debug_protected.txt")
        debug_file.write_text(protected_text, encoding="utf-8")
        print(f"❌ Errore DeepL. Testo protetto salvato in {debug_file}")
        raise RuntimeError(f"Errore DeepL: {e}") from e

    translated = result.text
    translated = unescape_xml(translated)
    return restore_latex(translated, placeholders)

# ============================================================
# FILE
# ============================================================

def translate_file(
    client: deepl.Translator,
    source_file: Path,
    target_dir: Path,
    lang: str,
) -> bool:
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

def main(files_to_translate: Optional[List[str]] = None):
    client = get_deepl_client()

    if files_to_translate:
        source_files = [SOURCE_DIR / filename for filename in files_to_translate]
    else:
        source_files = sorted(SOURCE_DIR.glob("*.tex"))

    print("File da tradurre:", [f.name for f in source_files])
    if not source_files:
        print("⚠️ Nessun file da tradurre.")
        return

    success_count = 0
    total_jobs = len(source_files) * len(TARGET_LANGS)

    for source_file in source_files:
        if not source_file.exists():
            print(f"⚠️ File non trovato: {source_file}")
            continue

        for lang, target_dir in TARGET_LANGS.items():
            ok = translate_file(client, source_file, target_dir, lang)
            if ok:
                success_count += 1

    print(f"\n✅ Traduzione completata: {success_count}/{total_jobs} file tradotti con successo.")

if __name__ == "__main__":
    files = sys.argv[1:] if len(sys.argv) > 1 else None
    main(files)