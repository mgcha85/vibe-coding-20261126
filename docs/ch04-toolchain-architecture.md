# Chapter 04. 툴체인(Toolchain) & 하네스(Harness) 아키텍처

> **"프롬프트 엔지니어링의 시대는 끝났다. 이제는 헌법과 도구, 그리고 기억을 장착하는 인프라의 시대다."**

본 문서는 강의 슬라이드 Chapter 04에서 다룬 **바이브 코딩 에이전트 툴체인(Toolchain) 및 하네스(Harness) 시스템의 핵심 개념과 설계 원칙**을 엔지니어링 관점에서 체계적으로 정리한 기술 명세서입니다.

---

## 1. 개요 및 패러다임 전환

과거의 AI 코딩은 단일 채팅창에 수백 줄의 프롬프트를 복사-붙여넣기하며 문법과 규칙을 사람이 매 턴 설명해야 했습니다. 그러나 이러한 방식은 대화가 길어질수록 **컨텍스트 오염(Context Drift)**과 **망각(Amnesia)**, **연쇄 환각(Cascading Hallucination)**을 피할 수 없습니다.

2026 현대 바이브 코딩 에이전트는 프롬프트 작문술이 아닌 **5대 하네스 인프라**로 에이전트의 지능과 행동반경을 구속(Constrain)하고 가이드합니다:

1. **헌법 (Constitution)**: 매 턴 시스템 최상단에 자동 주입되는 단일 진실 공급원(`AGENTS.md`)
2. **절차 기억 (Procedural Skills)**: 작업 의도(Intent)를 감지하여 온디맨드로 적재되는 도구 팩(`.cursor/skills/`)
3. **제약 및 검증 (Rules & Grill-me)**: 계층적 제약 사규와 맹종을 방지하는 능동적 역질문 체계
4. **실행 가드레일 (Lifecycle Hooks)**: 도구 호출 전후로 쉘 명령을 가로채는 이벤트 주도형 방화벽
5. **영속 기억 (Central LLM-Wiki)**: 세션이 끊겨도 지식이 누적되는 3계층 컴파일 지식 베이스

---

## 2. AGENTS.md : 매 턴 주입되는 프로젝트 헌법

### 2.1 동작 메커니즘
`AGENTS.md`는 대화창에 수동으로 복사해 넣는 프롬프트가 아닙니다. Cursor, Windsurf, Antigravity IDE 등 최신 에이전트 런타임의 프롬프트 파이프라인에서 **모든 턴(Every-turn)마다 사용자 입력 바로 앞에 최우선 순위로 자동 주입(Prepend)**되는 시스템 레벨 단일 진실 공급원(SSOT)입니다.

```
[User Turn Input]
      ↓ (Every-Turn Prompt Pipeline)
+-----------------------------------------------------------+
| 📜 /AGENTS.md (최상단 자동 프리펜드 - 시스템 헌법)          |
|  1. 프로젝트 정체성 & 미션 (PBMC 3k scRNA-seq Vibe Lab)    |
|  2. 기술 스택 & 런타임 제약 (Python 3.12, DuckDB, Astro 5) |
|  3. 디렉토리 소유권 (data/raw 불변, backend, frontend)    |
|  4. 품질 검증 게이트 (import pandas 금지, ruff, Astro 빌드)|
+-----------------------------------------------------------+
      ↓
[Agent LLM Reasoning & Tool Call Execution]
```

### 2.2 핵심 구성 4대 요소
1. **Mission & Scope**: 단일세포 전사체 파이프라인 및 대시보드 구축 범위와 원시 데이터 불변 원칙 선언
2. **Directory & Module Ownership**: `data/raw/`(읽기 전용), `data/warehouse/`(DuckDB SSOT), `backend/`, `frontend/` 책임 격리
3. **Code Quality Gates**: `import pandas` 실패(ImportError) 검증, `ruff check backend/`, `npm run build` 정적 빌드 통과 의무화
4. **Environment & Safe Change Policy**: `.env` 비밀키 격리, 원본 및 DB 임의 삭제 엄금, `LESSON_AND_LEARN.md` 오답 노트 의무화

---

## 3. Skills 아키텍처 : 폴더 구조와 네이밍 전략

### 3.1 디렉토리 표준 레이아웃
에이전트 스킬은 `.cursor/skills/`, `.agents/skills/`, `.opencode/skills/` 등 런타임 표준 경로에 배치됩니다. 서로 다른 에이전트 도구를 번갈아 사용하더라도 동일한 스킬을 동작시키기 위해 **심볼릭 링크(Symlink)**로 단일화합니다.

```
pbmc3k-vibe-lab/
├── AGENTS.md                           # 프로젝트 헌법 (Every-turn 주입)
├── .cursor/skills/                     # (또는 .agents/skills)
│   ├── db-duckdb-schema/               # DuckDB 웨어하우스 SSOT 스킬
│   │   ├── SKILL.md                    # genes/cells/counts 스키마 및 적재 규칙
│   │   └── REFERENCE.md                # 필요 시 호출하는 SQL 쿼리 가이드
│   ├── data-analytics-dimreduce-cluster/# 차원축소 & Leiden 군집 스킬
│   │   └── SKILL.md                    # HVG 2000, PCA 50, Leiden igraph
│   ├── ui-echarts/                     # Apache ECharts 5 차트 스킬
│   │   └── SKILL.md                    # UMAP 산점도 및 custom violin 플롯
│   └── ops-pipeline-orchestration/     # 파이프라인 전체 실행 & 품질 게이트
│       └── SKILL.md
```

### 3.2 의도 기반 라우팅(Intent-based Routing) 네이밍
스킬 디렉토리명과 `SKILL.md`의 `name`은 에이전트가 사용자의 작업 의도를 감지하는 1차 라우팅 키입니다:
- **도메인 접두사 규칙**: `ui-`, `db-`, `api-`, `ops-`, `test-` 등 작업 영역을 명확히 분리
- **명사+역할 조합**: `ui-dashboard`, `db-migration-pg`, `sec-rls-guardrails`
- **구체적인 설명(Description)**: 프런트매터의 description에 에이전트가 "언제 이 스킬을 활성화해야 하는지" 명확한 트리거 조건을 명시

---

## 4. 문서 설계학 : SKILL.md vs REFERENCE.md 분리

모든 규칙과 코드 예제를 단일 파일에 작성하면 토큰이 폭발하고 모델의 주의력(Attention)이 분산됩니다. 따라서 **2단계 계층형 문서 구조**를 필수로 적용합니다.

| 구분 | Level 1 : `SKILL.md` | Level 2 : `REFERENCE.md` |
| :--- | :--- | :--- |
| **성격** | 실행 강령 & 트리거 헌법 | 심층 참고 레퍼런스 & 규격서 |
| **로딩 시점** | 관련 작업 감지 시 **즉시 컨텍스트에 자동 로드** | 에이전트가 추가 세부 정보 필요 시 **온디맨드(On-Demand) 호출** |
| **적정 분량** | 50 ~ 100줄 이내 (초경량 유지) | 수백 ~ 수천 줄의 심층 코드 예제, API 명세, 색상 토큰 |
| **필수 요소** | YAML Frontmatter (`name`, `description`) | 목차, 세부 코드 스니펫, 엣지케이스 가이드 |
| **핵심 목적** | 빠른 행동 지침 제시 및 토큰 절감 | 복잡한 도메인 지식의 정확한 전달 |

---

## 5. Rules 체계와 Grill-me : 능동적 정렬 메커니즘

### 5.1 계층적 Rules 우선순위 (Hierarchical Precedence)
스킬이 "어떻게 구현할 것인가(How)"를 다룬다면, 룰(Rules)은 **"무엇을 절대 넘지 말아야 하는가(Constraint)"**를 통제합니다.

1. **Global Rules (`~/.gemini/config`, `~/.cursorrules`)**: 개인 개발 환경의 기본 거버넌스 (한국어 응답, 불필요한 미사여구 금지 등)
2. **Project Rules (`.cursor/rules/*.md`, `.agents/rules/`)**: 프로젝트 레포지토리 전반에 통용되는 강제 표준 (Python 3.12, DuckDB SSOT, Astro 5, `import pandas` 전면 금지)
3. **Directory Rules (하위 폴더별 `AGENTS.md`)**: 특정 디렉토리 한정 최우선 룰 (예: `data/raw/` 원본 h5ad 파일 수정 절대 금지, `backend/` 내 `import pandas` 엄금)

### 5.2 /grill-me : 맹종(Blind Compliance) 방지 역질문 인터뷰
사용자의 모호한 한마디 지시에 AI가 즉시 코딩을 시작하면 90% 이상 엉뚱한 아키텍처가 생성됩니다. `/grill-me` 패턴은 **에이전트가 작업을 착수하기 전 개발자에게 3~5가지 핵심 아키텍처 결정을 역질문**하여 상호 정렬을 마친 뒤 실행하도록 강제합니다.

```
[User: "PBMC 3k 군집 분석 파이프라인 만들어줘"]
      ↓ (Grill-me 인터뷰 가동)
[Agent: "코딩 착수 전에 3가지 설계를 먼저 확정하겠습니다:
  1. 클러스터링 알고리즘: Leiden resolution=1.0 (igraph) vs Louvain?
  2. 고변동 유전자(HVG): Seurat top 2000 기준 적용 여부?
  3. 결과 저장소: DuckDB 테이블 적재 후 Astro용 JSON export 일괄 갱신 여부?"]
      ↓ (연구자/개발자 답변 완료 후 원샷 구현 착수)
```

---

## 6. Lifecycle Hooks : 이벤트 주도형 자동 가드레일

에이전트가 도구를 호출하거나 실행을 종료할 때, 사람의 감시 없이도 백그라운드 쉘 스크립트가 실행되어 안전을 보장합니다 (`hooks.json`).

| Hook 이벤트 | 실행 시점 | 주요 활용 사례 |
| :--- | :--- | :--- |
| **PreInvocation** | LLM 프롬프트 생성 전 | 최신 Git 상태, 동적 환경변수, 활성 브랜치 정보를 컨텍스트에 자동 주입 |
| **PreToolUse** | 도구(쉘, 파일 수정) 실행 직전 | `rm -rf`, `git push --force`, `DROP TABLE` 등 파괴적 명령어 사전 차단 (보안 방화벽) |
| **PostToolUse** | 도구 실행 완료 직후 | 코드 작성 즉시 백그라운드에서 `ruff format`, `prettier`, `go fmt` 자동 실행 |
| **PostInvocation** | 에이전트 턴 완료 시점 | 전체 테스트(`pytest`, `go test`) 자동 구동 및 컴파일 에러 발생 시 즉각 자가 치유 루프 유도 |

---

## 7. 공통 모듈 vs 프로젝트 특화 분리

모든 레포지토리에 똑같은 룰과 스킬을 복사하면 유지보수 부채가 발생합니다. **중앙 사규 저장소**와 **프로젝트 개별 룰**을 이원화합니다.

```
+------------------------------------+       +------------------------------------+
|  중앙 전사 사규 레포지토리        |       |  개별 서비스 프로젝트 레포지토리   |
|  (harness-collection / governance) |       |  (pbmc3k-vibe-lab)                 |
+------------------------------------+       +------------------------------------+
| • AGENTS.md (공통 헌법)             | =====>| • AGENTS.md (심볼릭 링크 연결)      |
| • skills/uiux-governance           | (Sub- | • skills/ (공통 스킬 팩 링크)       |
| • skills/deployment-operations     | module| • PROJECT.md (단일세포 전사체 특화)|
| • skills/security-guardrails       |  Link)| • data/warehouse/pbmc3k.duckdb     |
+------------------------------------+       +------------------------------------+
```

- **공통 헌법 (`AGENTS.md`)**: 시크릿 관리, 배포 게이트, 커밋 컨벤션, 파괴적 명령어 금지 (Git Submodule/링크)
- **프로젝트 특화 문서 (`PROJECT.md`)**: 단일세포 전사체(PBMC 3k) 도메인, DuckDB 스키마, HVG/PCA/Leiden 분석 표준, 마커 패널 정의

---

## 8. 토큰의 실체 : 컨텍스트 윈도우 조립 파이프라인

LLM은 이전 대화를 스스로 기억하는 뇌가 없습니다. 완전한 **상태 비저장(Stateless)** 엔진입니다.
에이전트가 '기억하고 작업하는 것'처럼 보이는 실체는, 매 턴마다 **'1장의 빈 문서'에 5대 독립 원천 자산을 실시간 모듈러 조립**하여 API로 전송하는 파이프라인 덕분입니다.

```
[원천 1] 프로젝트 헌법 (/AGENTS.md) ─────────────────┐
[원천 2] 강제 제약 규정 (.cursor/rules/*.md) ──────────┼─> [단 1장의 빈 문서 (Context Window)]
[원천 3] 의도 감지 스킬 (.cursor/skills/*/SKILL.md) ───┤   - System Instructions
[원천 4] 압축된 세션 상태 (PLAN / LESSON_AND_LEARN) ────┤   - Project Constitution & Rules
[원천 5] 현재 턴 사용자 프롬프트 (User Prompt) ───────┘   - Active Skills & Dynamic Context
                                                           - Compaction History & User Intent
                                                                      ↓
                                                           [LLM API 1회 완결 호출]
```

---

## 9. 세션 변경과 망각을 이기는 3대 상태 문서

새 대화창을 열거나 세션 컨텍스트가 200k 토큰에 달해 요약이 일어날 때 발생하는 **'컨텍스트 절벽(Context Cliff)'**을 3대 문서로 극복합니다.

```
                  ┌─────────────────────────────────────────┐
                  │          SESSION RECOVERY SSoT          │
                  └────────────────────┬────────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
 🩹 LESSON_AND_LEARN.md         📋 PLAN.md                     🎯 INTENT.md
 (일화 기억 · Episodic)        (작업 상태 · Working)          (연구 의도 · Semantic)
 동일 버그 재발 방지           현재 진행 단계 & 체크리스트    파이프라인 본질적 이유 & 인수 기준
```

### 9.1 `LESSON_AND_LEARN.md` (오답 노트 / 일화 기억)
동일한 에러로 에이전트가 반복 삽질하며 토큰을 날리는 것을 방지합니다:
- **실전 사례 1 (ECharts 차트 일원화)**: 손수 SVG 차트 4종이 제각각이라 상호작용 및 유지보수 비용 급증 → `echarts@5.6.0` + custom violin series로 통일. `ui-echarts`가 차트 SSoT.
- **실전 사례 2 (Scanpy Leiden igraph 백엔드)**: `sc.tl.leiden`이 leidenalg 미설치로 실패 → `flavor="igraph", n_iterations=2`로 고정하여 단번에 통과.
- **실전 사례 3 (pandas 금지와 AnnData)**: AnnData `.obs`/`.var`의 pandas DataFrame 변환 유혹 → AnnData는 임시 수치 객체로만 쓰고 표 산출은 즉시 DuckDB/Polars로 이관, 코드 내 `import pandas` 전면 금지.
- **실전 사례 4 (리보솜 유전자 필터링)**: T cell 군집 top DEG가 RPS/RPL만 나옴 → 하우스키핑 유전자 제외 후 canonical marker 평균으로 세포타입 판정.

### 9.2 `PLAN.md` (작업 나침반 / 작업 기억)
대규모 리팩토링이나 롱호라이즌(Long-horizon) 태스크 시 작업 위치를 잃지 않도록 동기화합니다:
- **Phase 0 (Harness)**: 헌법/문서/스킬 심볼릭 링크 및 원본 h5ad 캐시 배치
- **Phase 1 (Warehouse)**: `backend/ingest`로 DuckDB에 2,700 세포 × 32,738 유전자 적재
- **Phase 2 (QC + Astro)**: `backend/qc` 필터링 및 Astro `/qc` 시각화 페이지 구축
- **Phase 3 (Cluster)**: HVG 2,000, PCA 50, UMAP 산점도 및 Leiden 9개 군집 추출
- **Phase 4 (Markers & Annotation)**: Wilcoxon DEG 마커 탐색 및 세포타입(T, B, Monocyte 등) 판정
- **Phase 5 (Export & Polish)**: Astro용 JSON 일괄 내보내기 및 ruff / Astro 빌드 게이트 통과

### 9.3 `INTENT.md` (의도 헌장 / 의미 기억)
코드가 수십 번 리팩토링되어도 연구/제품의 원래 목적이 변질되지 않도록 고정합니다:
- **Why**: 10x Genomics PBMC 3k 단일세포 전사체 파이프라인 재현 및 자연어 AI(AutoBA/scChat) 분석 연동.
- **Persona**: 생물정보학 입문 연구자 + 바이브 코딩 실습생. 한국어 UI로 QC·UMAP·마커를 한 흐름으로 탐색.
- **인수 기준**: 원시 데이터 재다운로드 없이 DuckDB 적재, `import pandas` 전면 금지, ECharts 기반 시각화, 마커 숫자 근거로 세포타입 판정.

---

## 10. 중앙 집중형 LLM-Wiki : 3계층 정제 아키텍처

사내 또는 개인의 수많은 프로젝트가 지식을 공유하고 지속적으로 똑똑해지도록 **3계층 컴파일 지식 베이스(LLM-Wiki)**를 운영합니다.

```
[Layer 1. Raw Sources (불변 원본)]
  /raw/ 논문, 공식 API 문서, 회의록, 장애 로그, DB 덤프 (읽기 전용)
      ↓ (AI Ingest & Markdown Linter 컴파일)
[Layer 2. Schema & Governance (정제 헌법)]
  AGENTS.md, 엔티티/결정 템플릿, 지식 작성 표준 헌법
      ↓ (Cross-linking & Semantic Indexing)
[Layer 3. Compiled Wiki & Skills (영속 지식)]
  /concepts/ (도메인 개념) · /decisions/ (ADR 결정) · /skills/ (실행 도구)
```

- **RAG를 초월한 지속 축적**: 단순 벡터 유사도 검색이 아닌, 위키 간 상호 링크(`[[concept]]`)와 요약을 통해 고차원 아키텍처 맥락 제공
- **허브 앤 스포크(Hub-and-Spoke)**: 모든 프로젝트는 중앙 위키를 Submodule 또는 읽기 전용 MCP 도구로 연결하여 동일한 수준의 최신 지능 발휘

---

## 11. 토큰 레버리지 (Token Leverage) 플라이휠

하네스와 위키가 갖춰진 환경에서는 **개발자의 프롬프트 지시량이 줄어들수록 산출물의 품질과 범위는 10배 이상 비약**합니다.

```
[위키가 없는 일반 개발자 (Zero Leverage)]
- 프롬프트 2,000 토큰 소모:
  "Astro 5 써주고, 라이트 테마 쓰고, 차트는 Apache ECharts 5 쓰고, DuckDB 웨어하우스에 넣고, 
   pandas는 쓰지 말고, Leiden 군집은 igraph 백엔드로 해주고..."
  ➔ 토큰 낭비, 3턴 뒤 규칙 망각, pandas 임포트 사고 발생

[LLM-Wiki & 하네스 보유자 (10x Token Leverage)]
- 프롬프트 30 토큰 소모:
  "PLAN.md 3단계 UMAP 군집 시각화 컴포넌트 구현해줘"
  ➔ 에이전트가 AGENTS.md, ui-viz-umap 스킬, ui-echarts 토큰을 스스로 인출하여
     1,970 토큰 분량의 완벽한 프로덕션 엔지니어링 코드 완성!
```

---

## 12. 결론 및 실전 체크리스트

1. [ ] 루트 디렉토리에 프로젝트 헌법인 `AGENTS.md`를 정의하였는가?
2. [ ] 자주 사용하는 작업 룰을 `.cursor/skills/` 아래 `SKILL.md`와 `REFERENCE.md`로 계층 분리하였는가?
3. [ ] 모호한 요구사항에 대해 에이전트가 `/grill-me` 역질문을 던지도록 유도하였는가?
4. [ ] 치명적 실수(`rm -rf`, `DROP TABLE`)를 막는 `hooks.json` 가드레일을 장착하였는가?
5. [ ] 세션 복구 및 망각 방지를 위한 3대 상태 문서(`LESSON_AND_LEARN`, `PLAN`, `INTENT`)를 기록하고 있는가?
6. [ ] 축적된 지식을 재사용하여 프롬프트 토큰을 아끼는 토큰 레버리지를 실현하고 있는가?

위 6가지 인프라가 갖추어졌을 때, 에이전트는 더 이상 제멋대로 동작하는 환각 생성기가 아니라 **시니어 엔지니어의 규율을 100% 준수하는 믿음직한 페어 프로그래머**로 거듭납니다.
