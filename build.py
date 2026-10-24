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
    
    OUTPUT_FILE.write_text(rendered, encoding="utf-8")
    print(f"✅ Successfully compiled {total_slides} slides from slides/ into index.html")

if __name__ == "__main__":
    build()
