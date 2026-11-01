---
name: uiux-governance
description: Enterprise UI/UX Design System and Governance standard for modern web applications. The Single Source of Truth (SSoT) for UI architecture — supersedes generic styling suggestions. Enforces icon-first status, auto-collapse on completion, panel-level scrolling, thin header chrome, action gating, and Korean-first copy.
---

# UI/UX Governance (SSoT)

모든 엔터프라이즈 및 운영 지원 웹 애플리케이션(Svelte, Tailwind CSS 등)의 UI/UX 설계와 구현 결과를 통제하는 **Single Source of Truth (SSoT)** 표준 지침입니다.

---

## 1. 핵심 철학 (3 Core Principles)

1. **Unified Experience (일관된 경험)**:
   - 시스템 전반의 컴포넌트, 색상, 타이포그래피, 상태 표현을 단일 디자인 토큰 체계로 통일합니다.
2. **Approach with One-Click (원클릭 접근)**:
   - 사용자가 목적하는 데이터와 핵심 액션에 도달하는 클릭 뎁스를 최소화하고, 필드 옆 인라인 액션을 적극 배치합니다.
3. **Catch on One-Page (원페이지 종결)**:
   - 잦은 화면 이동 없이 단일 뷰 내에서 맥락(Context)을 유지하며 조회·편집·승인·발송 등 일련의 업무를 완결합니다.

---

## 2. 상시 상호작용 패턴 (Always UX Interaction Patterns)

모든 화면 구현 시 **예외 없이 반드시 준수**해야 하는 10대 상호작용 규칙입니다.

| 번호 | 패턴 | 핵심 규칙 | Do (권장) | Don't (금지) |
|---|---|---|---|---|
| **1** | **아이콘 우선 (Icon-First Status)** | 상태·헬스·진행도는 텍스트 배지 나열 대신 **컬러 아이콘 칩**으로 표시 | 연결/정상 상태는 녹색/파란색 아이콘 칩 + 툴팁 (`title`) | 헤더나 테이블에 긴 한글 텍스트 배지(`연결 완료`, `대기 중`) 나열 |
| **2** | **인라인 액션 (Inline Actions)** | 입력·조회와 직결된 액션은 해당 필드 우측에 **인라인 아이콘**으로 배치 | 셀렉트/입력 우측에 '새로고침', '복사', '외부링크' 아이콘 배치 | 필드 아래에 별도 텍스트 버튼 행(`[새로고침]`, `[링크열기]`) 추가 |
| **3** | **완료 시 자동 접힘 (Auto-Collapse)** | 설정 완료, 연결 성공 시 상세 폼은 자동으로 접히고 요약 카드로 전환 | 완료 후 `Accordion` 형태로 접히고 우측 Chevron으로 재열기 제공 | 작업 완료 후에도 거대한 입력 폼을 그대로 방치하여 화면 공간 낭비 |
| **4** | **패널 단위 독립 스크롤 (Panel Scroll)** | 전체 창(body) 스크롤을 금지하고, 셸(헤더/사이드바) 고정 후 **패널 내부 스크롤** | `h-screen flex flex-col overflow-hidden`, 내부 패널 `overflow-y-auto` | 전체 브라우저 윈도우 스크롤이 생겨 헤더나 사이드바가 함께 위로 밀려 올라감 |
| **5** | **얇은 크롬 (Thin Chrome)** | 헤더는 48~56px 단일 행으로 최소화하여 업무 공간 극대화 | 1행 헤더에 브랜드 + 탭/내비 + 우측 상태 아이콘 칩 배치 | 상단에 장황한 설명 배너나 부제 텍스트 영역을 크게 차지 |
| **6** | **전제조건 액션 게이트 (Action Gating)** | 필수 조건이 만족되지 않은 버튼은 비활성화(`disabled`) | 필수 입력/유효성 미충족 시 버튼 `disabled` + 툴팁으로 사유 안내 | 미완성 상태인데도 클릭을 열어두고 클릭 후 경고 팝업 띄우기 |
| **7** | **작업 이력 및 영속성 (History Persistence)** | 중요한 작업 상태나 선택 내역은 로컬/세션에 유지 | 최근 조회 문서, 선택 필터, 작업 탭 상태를 새로고침 후에도 복원 | 브라우저 새로고침 한 번에 작성 중인 데이터나 탐색 위치가 초기화됨 |
| **8** | **기본 언어 한국어 (Korean Default)** | UI 텍스트, 라벨, 상태, 안내 문구는 한국어를 기본으로 제공 | `html lang="ko"`, "접수 완료", "발주 대기", "정상 연결" | UI 버튼이나 상태를 불필요하게 영문("Pending", "Success") 혼용 |
| **9** | **초기 번쩍임 방지 (No Premature Flash)** | 비동기 데이터 로딩 중 기본 fallback 문구를 조기 노출하지 않음 | 스켈레톤(Skeleton UI) 또는 초기화 가드(`isLoaded`)로 부드럽게 전환 | 0.5초 동안 "데이터 없음" 문구를 깜빡였다가 실제 데이터로 교체 |
| **10** | **외부 클릭 자동 닫기 (Click-Outside Collapse)** | 팝오버, 드롭다운 메뉴는 외부 영역 클릭 시 즉시 닫힘 | 문서 영역 클릭 시 열려 있던 드롭다운 자동 닫기 리스너 적용 | 팝오버를 닫으려면 반드시 원래 버튼을 다시 눌러야 하는 불편함 방치 |

---

## 3. 디자인 토큰 & 스타일 가이드 (Tailwind CSS 기준)

### 3.1 상태 팔레트 (Status Palette)
상태 표현은 의미론적 컬러 토큰을 일관되게 사용합니다:
- **Success / Done / Active**: `emerald-600` (배경 `emerald-50`, 테두리 `emerald-200`)
- **Info / In-Progress**: `blue-600` (배경 `blue-50`, 테두리 `blue-200`)
- **Warning / Pending**: `amber-600` (배경 `amber-50`, 테두리 `amber-200`)
- **Danger / Error / Blocked**: `rose-600` (배경 `rose-50`, 테두리 `rose-200`)
- **Neutral / Idle / Default**: `slate-600` (배경 `slate-100`, 테두리 `slate-200`)

### 3.2 타이포그래피 & 레이아웃
- **기본 폰트**: `Pretendard`, `-apple-system`, `BlinkMacSystemFont`, `system-ui`, `sans-serif`
- **헤더 높이**: `h-14` (56px) 또는 `h-12` (48px)
- **카드/패널 테두리**: `border border-slate-200 dark:border-slate-800 rounded-lg shadow-sm`
- **테이블 헤더**: `bg-slate-50 dark:bg-slate-800/60 text-xs font-medium text-slate-500 uppercase tracking-wider`

---

## 4. 프론트엔드 구현 체크리스트

1. [ ] 루트 레이아웃이 `h-screen flex flex-col overflow-hidden` 구조인가?
2. [ ] 스크롤이 필요한 콘텐츠 영역에 `flex-1 overflow-y-auto`가 지정되어 있는가?
3. [ ] 상태 표시가 긴 텍스트 대신 직관적인 아이콘 칩과 툴팁으로 구성되었는가?
4. [ ] 드롭다운과 모달에 Click-Outside 닫기 로직이 적용되었는가?
5. [ ] 필수 입력이 누락되었을 때 CTA 버튼이 적절히 비활성화되는가?
6. [ ] 비동기 로딩 중 스켈레톤 혹은 스피너가 표시되어 레이아웃 번쩍임이 없는가?
7. [ ] 모든 사용자 노출 문구가 자연스러운 한국어로 작성되었는가?
