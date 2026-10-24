#!/usr/bin/env python3
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SLIDES_DIR = BASE_DIR / "slides"
TEMPLATE_FILE = BASE_DIR / "template.html"
OUTPUT_FILE = BASE_DIR / "index.html"

def build():
    if not TEMPLATE_FILE.exists():
        print(f"Error: {TEMPLATE_FILE} not found!")
        return

    # 순차적으로 slides 하위 디렉토리 및 파일 탐색
    slide_files = sorted(SLIDES_DIR.glob("**/*.html"))
    
    slides_html = []
    for sf in slide_files:
        content = sf.read_text(encoding="utf-8").strip()
        slides_html.append(f"      <!-- [COMPONENT] {sf.relative_to(SLIDES_DIR)} -->\n" + content)
    
    total_slides = len(slides_html)
    combined_content = "\n\n".join(slides_html)
    
    template = TEMPLATE_FILE.read_text(encoding="utf-8")
    
    # 템플릿 변수 치환
    rendered = template.replace("{{TOTAL_SLIDES}}", f"{total_slides:02d}")
    rendered = rendered.replace("{{SLIDES_CONTENT}}", combined_content)
    
    # 마크다운 문법 누출 검사 (Linter Guardrail)
    markdown_warnings = []
    for sf in slide_files:
        raw_text = sf.read_text(encoding="utf-8")
        rel_path = sf.relative_to(SLIDES_DIR)
        
        # Check for raw **bold** markdown
        bold_matches = re.findall(r"\*\*[^*]+\*\*", raw_text)
        if bold_matches:
            markdown_warnings.append(f"  - [{rel_path}] Raw bold markdown detected: {bold_matches}")

    if markdown_warnings:
        print("\n⚠️ [WARNING] Raw Markdown syntax detected in HTML slides! (Use HTML tags like <strong> instead):")
        for w in markdown_warnings:
            print(w)
        print("--------------------------------------------------------------------------------\n")
    
    OUTPUT_FILE.write_text(rendered, encoding="utf-8")
    status_msg = "✅ Successfully compiled" if not markdown_warnings else "⚠️ Compiled with warnings"
    print(f"{status_msg} {total_slides} slides from slides/ into index.html")

if __name__ == "__main__":
    build()
