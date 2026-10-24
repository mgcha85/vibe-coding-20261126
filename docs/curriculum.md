# [강의 계획서] 말이 코드가 되는 시대 : 바이브 코딩(Vibe Coding)의 이상과 현실, 그리고 프로덕션 엔지니어링

- **행사명**: 한국지능시스템학회 2026 추계학술대회 (KIIS 2026) 튜토리얼
- **일시**: 2026년 11월 26일(목) 13:00 ~ 16:00 (총 180분)
- **장소**: 김포대학교 글로벌캠퍼스 211-B호
- **강사**: 차민규 AI Engineer (LG AI & Big Data Group, Agentic AI 팀)
- **대상**: 바이브 코딩을 처음 접하는 입문자부터 실무/연구 도입을 고민하는 연구자 및 개발자

---

## 1. 강의 개요 및 목표

자연어로 소프트웨어를 구축하는 '바이브 코딩(Vibe Coding)'이 소프트웨어 엔지니어링의 패러다임을 혁명적으로 바꾸고 있습니다. 그러나 프롬프트 몇 마디로 실제 고객에게 서비스 가능한 완성형 소프트웨어가 저절로 만들어지는 것은 아닙니다.

본 튜토리얼은 3시간 동안 단순 데모 수준의 프로토타이핑을 넘어, **실제 프로덕션 환경에서 작동하는 소프트웨어를 AI 에이전트로 빌드, 검증, 배포, 운영하는 실전 엔지니어링 기법**을 심도 있게 다룹니다.

---

## 2. 3시간 타임테이블 (총 180분)

| 세션 | 시간 | 소요 | 주제 | 주요 내용 |
| :--- | :--- | :--- | :--- | :--- |
| **Opening** | 13:00 ~ 13:10 | 10분 | 오리엔테이션 및 오프닝 | 강사 소개, 본 튜토리얼의 목적과 로드맵 |
| **Part 1** | 13:10 ~ 13:30 | 20분 | **Ch 01. 계보** : 챗봇에서 자율 에이전트까지 | 프롬프트 엔지니어링의 종말, Tool-use, ReAct, 2026 에이전트 생태계 |
| | 13:30 ~ 13:55 | 25분 | **Ch 02. 본질** : 바이브 코딩이란 무엇인가 | Karpathy의 선언, Intent 기반 프로그래밍, 환상과 현실, 필수 엔지니어링 역량 |
| | 13:55 ~ 14:20 | 25분 | **Ch 03. 런칭** : Vercel · Supabase · Stripe | 1시간 만에 런칭하는 Modern BaaS, RLS, Stripe 결제 연동 실전 파이프라인 |
| **Break** | 14:20 ~ 14:30 | 10분 | 중간 휴식 (1) | 네트워킹 및 질의 준비 |
| **Part 2** | 14:30 ~ 14:50 | 20분 | **Ch 04. 툴체인** : Skills · LLM-Wiki · Aside | 모듈러 Skills, 지속적 Context 캐싱 LLM-Wiki, Aside 독립 에이전트, MCP |
| | 14:50 ~ 15:10 | 20분 | **Ch 05. 언어** : Python은 최적인가 | 타입 안정성(Type Safety), 컴파일러 피드백 루프, Go/Rust/TS vs Python 벤치마크 |
| | 15:10 ~ 15:30 | 20분 | **Ch 06. 비용** : 토큰 요금 80~90% 절감 | 컨텍스트 팽창 억제, Prompt Caching, 계층형 모델 라우팅, AST 선별 주입 |
| **Break** | 15:30 ~ 15:35 | 5분 | 중간 휴식 (2) | 짧은 휴식 |
| **Part 3** | 15:35 ~ 15:50 | 15분 | **Ch 07. 병렬화** : Grok Bot · Jev · Git Worktree | Git Worktree 격리 병렬 코딩, Multi-agent 오케스트레이션, 충돌 방지 전략 |
| | 15:50 ~ 16:00 | 10분 | **Ch 08. 가드레일** : RLS 누수 · 민감정보 격리 | Supabase RLS 취약점 감사, Sandbox 실행, Secret 격리 및 프로덕션 배포 게이트 |
| **Wrap-up** | 16:00 ~ 16:05 | 5분 | 결론 및 Q&A | 엔지니어의 미래 전략, 청중 질의응답 |

---

## 3. 챕터별 세부 아젠다 (Sub-Chapters)

### Chapter 01. 계보 : 챗봇에서 자율 에이전트까지
- **1.1 프롬프트 엔지니어링의 종말**: 1회성 텍스트 생성기에서 지속 실행 에이전트로의 전환
- **1.2 ReAct & Tool-Use 패러다임**: Reason(추론) + Act(행동) + Observe(관찰) 루프
- **1.3 Multi-turn 피드백 루프의 원리**: 에러 로그를 읽고 스스로 코드를 수정하는 메커니즘
- **1.4 2026 에이전트 생태계 해부**: IDE 내장형(Cursor, Windsurf 등) vs 자율 백그라운드 에이전트(Devin, SWE-bench)

### Chapter 02. 본질 : 바이브 코딩이란 무엇인가
- **2.1 Andrej Karpathy의 바이브 코딩 선언**: "코드를 읽지 않고 느낌과 의도로 개발한다?"
- **2.2 Intent(의도) 기반 소프트웨어 합성**: 고수준 스펙(Spec)과 인터페이스 중심 개발
- **2.3 이상 vs 현실 (Reality Check)**: '데모는 5분, 디버깅은 5일'이 발생하는 구조적 이유
- **2.4 2026 바이브 코더의 생존 역량**: 아키텍처 설계력, 테스트 주도 검증(TDD), Linter/타입 시스템 통제력

### Chapter 03. 런칭 : Vercel · Supabase · Stripe
- **3.1 Modern Serverless BaaS 3대장**: 왜 인프라를 직접 구축하지 않는가?
- **3.2 Vercel**: 깃허브 푸시부터 글로벌 CDN 배포, Edge Functions, Preview 환경 자동화
- **3.3 Supabase**: PostgreSQL 엔진 위의 실시간 DB, Auth, Storage, 그리고 Row Level Security(RLS)
- **3.4 Stripe**: 글로벌 결제 인프라, 웹훅 처리, 구독형 SaaS 비즈니스 로직 연동
- **3.5 실전 런칭 파이프라인**: 텍스트 기획서에서 실제 결제 가능한 웹 서비스까지의 End-to-End 파이프라인

### Chapter 04. 툴체인 : Skills · LLM-Wiki · Aside
- **4.1 에이전트 아키텍처의 학술적 진화 (AutoGPT 2023 → 2024+ Multi-Agent & Cognitive Architecture)**:
  - **AutoGPT(2023.03)의 등장과 Single-Agent Monolithic Loop의 한계**:
    - Thought-Plan-Criticism-Action의 단일 루프 시도.
    - 단일 컨텍스트에 모든 계획과 실행 로그를 때려 넣으면서 발생하는 *컨텍스트 드리프트(Context Drift)*, 연쇄 환각(Cascading Hallucination), 무한 루프 및 목표 망각(Goal Loss).
  - **2024년 학계의 패러다임 전환과 Agentic AI 연구 폭발**:
    - **ChatDev (Qian et al., 2023/2024)**: 인간 소프트웨어 회사의 분업(CEO-CTO-Programmer-Tester)을 모방한 Multi-Agent Chat-chain.
    - **MetaGPT (Hong et al., ICLR 2024)**: 단순 자연어 대화의 노이즈를 비판하고, **SOP(표준 운영 절차)**와 구조화된 명세(PRD, 아키텍처 다이어그램)를 강제하여 환각을 억제하고 Pass@1 80% 돌파.
    - **Reflexion (Shinn et al., NeurIPS 2023)**: 언어적 자가 반성(Verbal Self-Reflection)을 단기 메모리에 축적하여 모델 가중치 수정 없이 행동 궤도를 자가 치유.
    - **CoALA (Sumers et al., 2024 Cognitive Architectures for Language Agents)**: 에이전트의 뇌를 Working / Episodic / Semantic / Procedural Memory와 외부 액션 공간으로 체계화.
    - **Andrew Ng의 4대 Agentic Design Patterns (2024)**: Reflection, Tool Use, Planning, Multi-agent Collaboration.
  - **왜 '프롬프트'에서 '툴체인(Skills, Wiki, Aside)'으로 이동해야만 하는가?**:
    - 모델 파라미터가 커져도 인지 아키텍처(외부 기억, 모듈러 도구, 컨텍스트 격리)가 없으면 실전 복잡 엔지니어링은 불가능함을 학술적으로 입증.
- **4.2 Skills Architecture**: CoALA의 절차 기억(Procedural Memory) 구현체 — 도메인 규칙, 컨벤션, 전용 CLI를 LLM에 모듈러 방식으로 주입하기
- **4.3 LLM-Wiki & Context 지속성**: CoALA의 의미/일화 기억(Semantic & Episodic Memory) — 프로젝트 진행에 따른 아키텍처 결정(ADR)과 지식 자동 누적
- **4.4 Aside / 사이드카 에이전트**: 메인 작업 컨텍스트를 오염시키지 않고 서브 태스크를 병렬 조사하는 인지적 격리 기법
- **4.5 MCP (Model Context Protocol)**: 사내 DB, 파일, 개발 툴과 표준화된 통신 구축

### Chapter 05. 언어 : Python은 최적인가
- **5.1 AI 연구의 표준 Python vs 프로덕션 엔지니어링의 충돌**: 동적 타이핑의 치명적 한계
- **5.2 런타임 에러와 에이전트의 환각**: 에이전트가 런타임에 죽지 않고 스스로 고치게 만드는 법
- **5.3 컴파일러와 타입 체커 = 최고의 에이전트 가이드**: Rust / Go / TypeScript가 바이브 코딩에서 압도적인 이유
- **5.4 자가 치유(Self-healing) 성공률 벤치마크**: 타입 힌트와 컴파일 에러 메시지를 통한 원샷 버그 수정
- **5.5 2026 최적의 바이브 코딩 기술 스택 조합**: Frontend(Svelte/TypeScript) + Backend(Go/Rust)

### Chapter 06. 비용 : 토큰 요금 80~90% 절감
- **6.1 에이전트 루프의 경제학**: 파일 전체를 무지성 복붙할 때 발생하는 API 요금 폭탄
- **6.2 Prompt Caching & 컨텍스트 압축**: 변경되지 않는 시스템 프롬프트와 레포지토리 맵 캐싱
- **6.3 계층형(Tiered) 모델 라우팅 전략**: 
  - 1계층(Flash-Lite/Flash): 검색, 심볼 탐색, 단순 파일 분할
  - 2계층(Pro/Thinking): 아키텍처 설계, 핵심 로직 작성, 고난도 디버깅
- **6.4 AST(구상구문트리) & Ripgrep 기반 정밀 주입**: 전체 코드가 아닌 필요한 함수 인터페이스만 발췌 주입
- **6.5 비용 절감 실전 사례**: 월 \$1,200에서 \$150로 비용을 87% 감축한 프로덕션 최적화 사례

### Chapter 07. 병렬화 : Grok Bot · Jev · Git Worktree
- **7.1 순차적(Sequential) 코딩의 한계**: AI가 타이핑하는 동안 멈춰있는 개발자
- **7.2 Git Worktree의 혁신**: 브랜치 스위칭 없는 디렉토리 분리 동시 작업 환경
- **7.3 Multi-Agent 병렬 분업 체계**: 기획 에이전트 + 코딩 에이전트 + 테스트 에이전트의 협동
- **7.4 비동기 백그라운드 태스크 러너 (Jev, Grok Bot)**: 긴 배치성 리팩토링과 테스트 비동기 위임
- **7.5 브랜치 머지 및 충돌(Conflict) 자동 해결 파이프라인**: 변경점 통합 및 자동 회귀 테스트

### Chapter 08. 가드레일 : RLS 누수 · 민감정보 격리
- **8.1 바이브 코딩의 어두운 이면**: "일단 돌아가니 안전하겠지"가 초래하는 데이터 참사
- **8.2 Supabase RLS 누수 취약점**: 클라이언트 직접 쿼리 시 모든 row가 노출되는 보안 홀과 자동 감사 스크립트
- **8.3 Sandbox 실행 및 환경변수/Secret 격리**: 에이전트가 `.env`를 외부에 유출하거나 깃에 커밋하지 못하게 하는 격리 체계
- **8.4 공급망 공격(Supply Chain Attack) 방어**: AI가 지어낸 가짜 패키지(Typosquatting) 설치 차단
- **8.5 프로덕션 배포 전 Security Gate**: 정적 분석 + RLS 검증 + 시크릿 스캐닝 자동화
