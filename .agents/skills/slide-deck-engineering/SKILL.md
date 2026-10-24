---
name: slide-deck-engineering
description: >-
  Comprehensive guide and design patterns for creating, maintaining, and visually
  enhancing 16:9 interactive web presentation decks (HTML, Tailwind CSS, SVG Arc-context,
  Bento-tile, animated flow streams) for technical lectures and vibe coding tutorials.
  Activate this skill whenever the user asks to create slides, add diagrams, design visual
  flows, or update presentation lecture decks.
---

# Slide Deck Engineering & Visual Design Skill

This skill captures the end-to-end architecture, strict formatting rules, visual design patterns, and deployment workflow established for high-impact technical lecture slides.

---

## 1. Core Architecture: Modular Slide Component System

### 1.1 Directory Structure
Never edit the monolithic `index.html` directly. Always maintain slides as discrete chapter/subchapter components:
```text
├── slides/
│   ├── 01-lineage/           # Chapter 01 components
│   │   ├── 01-intro.html
│   │   ├── 02-prompt-fall.html
│   │   ├── 03-autogpt-failure.html
│   │   ├── 04-academic-papers.html
│   │   ├── 05-swebench-feedback.html
│   │   └── 06-two-camps.html
│   ├── 02-essence/           # Chapter 02 components
│   ├── ...
├── template.html             # Presentation shell (navigation, 16:9 stage, scripts, Tailwind)
├── build.py                  # Fast compiler & automated markdown linter
├── index.html                # Compiled bundle (generated artifact)
└── docs/curriculum.md        # Syllabus and agenda specification
```

### 1.2 Compilation & Automated Guardrail
- Run `python3 build.py` after editing any slide in `slides/`.
- `build.py` automatically injects total slide count (`{{TOTAL_SLIDES}}`) and replaces `{{SLIDES_CONTENT}}`.
- **Linter Guardrail**: Automatically scans for raw markdown leaks (`**bold**`, etc.) and alerts before outputting.

---

## 2. Visual & Design Standards

### 2.1 16:9 Widescreen & Bento-Tile Theme
- **Fixed Stage Ratio**: `16:9` (`56.25vw` or `177.78vh`), `overflow: hidden`, max-width bounded.
- **Color Palette**:
  - Deep Canvas: `#030712`, `#070d1a`, `#0c1527` with radial dark gradients.
  - Accent Borders: Sky (`#38bdf8`), Purple/Violet (`#c084fc`, `#818cf8`), Emerald (`#34d399`), Amber (`#fbbf24`), Rose/Red (`#f43f5e`).
- **Bento-Tile Spec**: Glassmorphism (`bg-slate-900/60` or `rgba(15, 23, 42, 0.65)`), subtle border (`rgba(255,255,255,0.08)`), `rounded-lg` or `rounded-xl`.
- **Typography**:
  - Headings & Prose: `Pretendard`, sans-serif.
  - Code, Metrics & Tags: `JetBrains Mono`, monospace.

### 2.2 Strict Prohibition: No Raw Markdown in HTML Slides (LESSON_AND_LEARN)
Slides are rendered as pure HTML components. Raw Markdown syntax does **NOT** compile in the browser:
- ❌ `**bold text**` ➔ ✅ `<strong>bold text</strong>` or `<strong class="text-sky-300">`
- ❌ `` `code` `` ➔ ✅ `<code class="font-mono bg-slate-800 px-1 py-0.5 rounded text-sky-300">code</code>`
- ❌ `*italic*` ➔ ✅ `<em>italic</em>`
- ❌ `[text](url)` ➔ ✅ `<a href="url" class="...">text</a>`

---

## 3. High-Impact Visual Storytelling Patterns

Text-heavy slides lose audience attention. Every technical concept should be translated into intuitive visual diagrams:

### Pattern 3.1: SVG Arc-Context Loop & State Machine
- Use smooth bezier curved paths (`M x1 y1 C ... x2 y2` or `Q`) and directional arrow markers.
- **ReAct State Machine**: 4-node circular feedback loop (`Reason (뇌)` ➔ `Act (손)` ➔ `Environment (환경)` ➔ `Observe (눈)` ➔ back to `Reason`).
- **AutoGPT Autonomous Multi-turn**: Front-facing Agent receiving a single prompt, executing an internal 4-step loop behind the scenes (`Thought ➔ Plan ➔ Criticism ➔ Action`), and returning final output without user hand-holding.

### Pattern 3.2: Animated Flowing Stream (Video / Motion Graphic Feel)
When explaining multi-layered architectural pipelines, make the diagram feel like a live, flowing video:
1. **Conveyor Dash Lines**:
   ```css
   @keyframes dashConveyor { to { stroke-dashoffset: -24; } }
   .animate-conveyor { stroke-dasharray: 6 4; animation: dashConveyor 1.2s linear infinite; }
   ```
2. **Streaming Photon Particles (`<animateMotion>`)**:
   Use native SVG `<circle>` particles traveling continuously along paths at staggered intervals:
   ```xml
   <circle r="4" fill="#38bdf8">
     <animateMotion path="M 185 85 L 270 85" dur="1.2s" repeatCount="indefinite"/>
   </circle>
   <circle r="2.5" fill="#e0f2fe">
     <animateMotion path="M 185 85 L 270 85" dur="1.2s" begin="0.6s" repeatCount="indefinite"/>
   </circle>
   ```
3. **Pulsing High-Priority Nodes**:
   Add glowing CSS drop-shadow filters to spotlight newly introduced layers (`✨ NEW LAYER`).

### Pattern 3.3: Historical Layer Stacking Metaphor
Translate technical paradigms into progressive abstraction layers:
- **Layer 0**: `Machine Silicon (0 & 1 Binary)`
- **Layer 1**: `Compiler & OS (Machine translation)`
- **Layer 2**: `Programming Language (High-level: C, Python, Rust)`
- **Layer 3 [NEW 2026]**: `AI Agent Layer (Translates Human Natural Language Intent into Source Code)`
- **Layer 4**: `Human Intent (Natural Language Thought & Business Goal)`

### Pattern 3.4: "Past vs Revolution" Concrete Visual Comparison
Contrast the failure of the past with the modern solution side-by-side:
- **Single-turn Blind Generation**: `User ➔ 1,000-line prompt ➔ LLM guess ➔ Token cut-off / Hallucination 💥`
- **Multi-turn Agent Loop**: `User ➔ Micro-Task ➔ Sandbox execution ➔ Stderr observe ➔ Self-Healing patch ✅`
- **Repo Map Token Compression**: `Full Repo (200k+ tokens ❌)` ➔ `Tree-sitter AST` ➔ `PageRank Graph` ➔ `Skeleton Map (80%+ cost reduction ✅)`

### Pattern 3.5: HyperFrames Living Video / Mockup Keyframe Motion Timeline
Inspired by [HeyGen HyperFrames](https://github.com/heygen-com/hyperframes) (*"Write HTML. Render video. Built for agents"*), simulate active screen recording videos using pure, zero-dependency 60 FPS CSS keyframes:
1. **Video Player Shell & Scrubber**:
   - Add a `● REC` recording indicator (pulsing red dot) and a live gradient scrubber bar (`@keyframes scrubberMove 12s linear infinite`).
   - Display a lightweight timecode (`12s LOOP`, `60 FPS Native`).
2. **Sequential Event Timing (% Keyframe Sequence)**:
   - Synchronize all elements to a unified 12-second loop:
     - `0s ~ 4s (Scene 1)`: User prompt appears (`anim-chat-prompt`) ➔ AI thinking indicator pulses (`anim-chat-thinking`) ➔ code snippet outputs ➔ limitation warning flashes.
     - `4.5s ~ 10s (Scene 2)`: Intent prompt bar glows neon ➔ File tree folders expand and files pop in (`anim-file-1`, `anim-file-2`) ➔ Terminal lines print sequentially ➔ Local server ready badge pops up.
     - `11.5s ~ 12s (Scene 3)`: Smooth fade-out reset to seamlessly restart loop.
3. **Chat Messenger Alignment**:
   - Align User messages to the **Right (`flex justify-end`)** with blue-accented bubbles.
   - Align AI responses to the **Left (`flex justify-start`)** with dark/slate borders and code blocks.

### Pattern 3.6: High-Impact Engineering Infographic Metaphors
When explaining abstract architectural and engineering trade-offs, use concrete physical metaphors:
- **The Vibe Iceberg**: Waterline separating the 10% visible surface (User prompt, 3-minute demo, shiny UI) from the 90% submerged engineering reality (State sync, DB transactions, RLS security, token explosions, context drift).
- **BaaS Lego Block Stream**: 4 modular pre-built blocks (Vercel, Clerk/Auth, Supabase DB, Stripe) connected by thin AI agent "Glue Code" instead of fragile scratch monolithic backends.
- **Compiler Closed-Loop vs Dynamic Broken Loop**: Python's runtime crash leading to hallucinations vs TypeScript/Rust compiler error feedback leading to deterministic one-shot self-healing.
- **Exploration Tax Token Bar**: Visualizing that 70% of tokens are wasted on file discovery before Prompt Caching slashes 90% of costs.

---

## 4. Historical Knowledge Milestones (2022 ~ 2026 Reference)

- **2022**: ChatGPT (Single-turn text chatbot, no hands, no eyes).
- **2023.03**: AutoGPT & ReAct (Monolithic loop, Context Drift & Cascading Hallucination failure).
- **2023.08 ~ 2024**: Academic explosion:
  - MetaGPT: SOP & UML Class Architecture (`SoftwareCompany`, `Boss`, `PM`, `Architect`, `Engineer`, `QA`).
  - ChatDev: Multi-agent Chat-Chain.
  - Reflexion: Verbal Reflection buffer for self-healing.
  - CoALA: Cognitive 4-Memory architecture (Working, Episodic, Semantic, Procedural).
  - Andrew Ng: 4 Agentic Patterns (Reflection, Tool Use, Planning, Multi-Agent).
- **2025**:
  - Test-Time Compute (o1, o3, Claude 3.5/3.7 Hidden CoT "Think before coding").
  - Aider Repo Map (Tree-sitter AST + PageRank token compression).
  - SWE-bench Multimodal & v2 (Vision agents resolving UI/Figma bugs).
- **2026**:
  - Outer Loop (Cloud persistent VM / Git Worktree) vs Inner Loop (IDE micro-task fast diff).
  - 2 Camps: IDE Inline Pair (Cursor/Windsurf) vs Autonomous Worker (Devin/Container Runner).
  - Toolchain Inevitability: Skills, LLM-Wiki, Aside memory isolation.

---

## 5. Deployment Workflow & Checklist

1. **Edit Component**: Update the specific slide in `slides/XX-dir/YY-file.html`.
2. **Compile**: Run `python3 build.py`. Ensure 0 linter warnings.
3. **Commit & Push**:
   ```bash
   git add slides/ index.html docs/
   git commit -m "feat/fix: <description>"
   git push origin main
   ```
4. **Verify GitHub Pages**:
   - Check workflow with `gh run list -L 1`.
   - Verify live URL: `https://mgcha85.github.io/vibe-coding-20261126/` (HTTP 200).
