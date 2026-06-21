import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time

def translate_html_safe(file_path, target_lang):
    print(f"Translating {file_path} to {target_lang}...")
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    translator = GoogleTranslator(source='en', target=target_lang)

    # Collect all text nodes
    texts = set()
    
    # We only want to translate visible text inside these tags
    for tag in soup.find_all(['p', 'article', 'h1', 'h2', 'h3', 'div', 'span', 'a']):
        # Ignore scripts, styles
        if tag.name in ['script', 'style']:
            continue
            
        # Ignore our dropdown to prevent messing up the flags
        classes = tag.get('class', [])
        if any(c in ['lang-dropdown', 'selected-lang', 'flag', 'lang-text', 'lang-option', 'chevron', 'logo-top', 'face'] for c in classes):
            continue
            
        # Check direct text
        for content in tag.contents:
            if isinstance(content, str):
                text = content.strip()
                if len(text) > 3 and not re.match(r'^[\W_]+$', text): # Ignore pure symbols
                    # Also ignore some tech words if possible, but deep-translator is okay
                    texts.add(text)

    # Sort texts by length descending so we replace longer strings first (prevents partial replacement)
    sorted_texts = sorted(list(texts), key=len, reverse=True)
    
    print(f"Found {len(sorted_texts)} strings to translate.")
    
    replacements = {}
    for i, text in enumerate(sorted_texts):
        # Skip previously hardcoded translations or codes
        if any(skip in text for skip in ['&#60;', '&#62;', 'Vinod Jangid', 'console.log']):
            continue
            
        try:
            translated = translator.translate(text)
            if translated and translated.lower() != text.lower():
                replacements[text] = translated
                print(f"[{i}/{len(sorted_texts)}] {text[:30]}... -> {translated[:30]}...")
            time.sleep(0.05)
        except Exception as e:
            print(f"Failed to translate: {text[:20]} - {e}")
            
    # Now replace in the original HTML string to preserve exact formatting
    new_html = html
    for en_text, tr_text in replacements.items():
        # Using simple replace. Since we sorted by length, longer matches replace first.
        new_html = new_html.replace(en_text, tr_text)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Done translating {file_path}\n")

translate_html_safe('index-ar.html', 'ar')
translate_html_safe('index-es.html', 'es')
