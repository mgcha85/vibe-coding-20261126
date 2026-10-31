#!/usr/bin/env python3
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SLIDES_DIR = BASE_DIR / "slides"
TEMPLATE_FILE = BASE_DIR / "template.html"
OUTPUT_FILE = BASE_DIR / "index.html"

CHAPTER_INFO = {
    "00-intro": {
        "id": "intro",
        "badge": "INTRO · 오프닝",
        "title": "Intro. 오프닝 & 커리큘럼 로드맵",
        "color": "bg-slate-500/15 text-slate-300 border-slate-400/30",
        "accent": "text-slate-400",
    },
    "01-lineage": {
        "id": "ch01",
        "badge": "CHAPTER 01 · 계보",
        "title": "Ch 01. 계보 : 챗봇에서 자율 에이전트까지",
        "color": "bg-sky-500/15 text-sky-300 border-sky-400/30",
        "accent": "text-sky-400",
    },
    "02-essence": {
        "id": "ch02",
        "badge": "CHAPTER 02 · 본질",
        "title": "Ch 02. 본질 : 바이브 코딩이란 무엇인가",
        "color": "bg-cyan-500/15 text-cyan-300 border-cyan-400/30",
        "accent": "text-cyan-400",
    },
    "03-language": {
        "id": "ch03",
        "badge": "CHAPTER 03 · 언어",
        "title": "Ch 03. 언어 : Python은 최적인가 (Go/Rust/TS)",
        "color": "bg-indigo-500/15 text-indigo-300 border-indigo-400/30",
        "accent": "text-indigo-400",
    },
    "04-toolchain": {
        "id": "ch04",
        "badge": "CHAPTER 04 · 툴체인",
        "title": "Ch 04. 툴체인 : Skills · LLM-Wiki · Context",
        "color": "bg-blue-500/15 text-blue-300 border-blue-400/30",
        "accent": "text-blue-400",
    },
    "05-parallel": {
        "id": "ch05",
        "badge": "CHAPTER 05 · 병렬화",
        "title": "Ch 05. 병렬화 : 다중 에이전트 동시 운용",
        "color": "bg-purple-500/15 text-purple-300 border-purple-400/30",
        "accent": "text-purple-400",
    },
    "06-cost": {
        "id": "ch06",
        "badge": "CHAPTER 06 · 비용",
        "title": "Ch 06. 비용 : 토큰 요금 80~90% 절감",
        "color": "bg-emerald-500/15 text-emerald-300 border-emerald-400/30",
        "accent": "text-emerald-400",
    },
    "07-launch": {
        "id": "ch07",
        "badge": "CHAPTER 07 · 런칭",
        "title": "Ch 07. 런칭 : 인증 · 결제 · 배포 · CI/CD",
        "color": "bg-amber-500/15 text-amber-300 border-amber-400/30",
        "accent": "text-amber-400",
    },
    "08-guardrails": {
        "id": "ch08",
        "badge": "CHAPTER 08 · 가드레일",
        "title": "Ch 08. 가드레일 : RLS 누수 & 보안 가드레일",
        "color": "bg-rose-500/15 text-rose-300 border-rose-400/30",
        "accent": "text-rose-400",
    },
    "99-summary": {
        "id": "summary",
        "badge": "WRAP-UP · 총정리",
        "title": "Wrap-up : 전체 핵심 요약 & 엔지니어의 미래",
        "color": "bg-violet-500/15 text-violet-300 border-violet-400/30",
        "accent": "text-violet-400",
    },
}

def build():
    if not TEMPLATE_FILE.exists():
        print(f"Error: {TEMPLATE_FILE} not found!")
        return

    # 순차적으로 slides 하위 디렉토리 및 파일 탐색
    slide_files = sorted(SLIDES_DIR.glob("**/*.html"))
    
    slides_html = []
    for sf in slide_files:
        chapter_dir = sf.parent.name
        info = CHAPTER_INFO.get(chapter_dir, {
            "id": chapter_dir,
            "badge": chapter_dir.upper(),
            "title": chapter_dir,
            "color": "bg-sky-500/15 text-sky-300 border-sky-400/30",
            "accent": "text-sky-400"
        })
        
        content = sf.read_text(encoding="utf-8").strip()
        
        # Inject data attributes into the first <section
        def add_attrs(match):
            tag = match.group(0)
            if 'data-chapter-id=' in tag:
                return tag
            attrs = (
                f' data-chapter-id="{info["id"]}"'
                f' data-chapter-badge="{info["badge"]}"'
                f' data-chapter-title="{info["title"]}"'
                f' data-chapter-color="{info["color"]}"'
                f' data-chapter-accent="{info["accent"]}"'
            )
            return tag[:-1] + attrs + ">"
            
        content = re.sub(r'<section\b[^>]*>', add_attrs, content, count=1)
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
