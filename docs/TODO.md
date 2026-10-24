# 바이브 코딩 튜토리얼 프로젝트 TODO 리스트

## 진행 상황
- [x] 학술대회 포스터 분석 및 3시간(180분) 타임테이블 기획
- [x] Chapter 01 ~ Chapter 08 세부 서브챕터(Sub-chapters) 기획 및 명세 작성 (`docs/curriculum.md`)
- [x] 16:9 비율의 인터랙티브 HTML 프레젠테이션 슬라이드 초안 구현 (`index.html`)
  - [x] 키보드 단축키 지원 (방향키, Space, F: 전체화면, M: 목차)
  - [x] 모달 목차 탐색기 (Table of Contents)
  - [x] 진행률 표시 바 및 슬라이드 카운터
  - [x] 38장 규모의 챕터별 카드 및 다이어그램 슬라이드 구성
- [x] `.env.example`, `.env.dev`, `.env.prod` 및 `.gitignore` 구성
- [x] `podman-compose.yml`, `start.sh`, `stop.sh` 구동/정지 환경 구축
- [x] GitHub Actions 배포 파이프라인 구성 (`.github/workflows/deploy.yml`)

## 향후 고도화 작업 (TODO)
- [ ] 각 챕터별 실습용 코드 스니펫 및 데모 리포지토리 링크 추가
  - [ ] Ch 03: Supabase RLS 예제 SQL 및 Stripe Checkout 미니 예제
  - [ ] Ch 04: Skills 폴더 템플릿 및 MCP 설정 파일 (`claude_desktop_config.json` 등)
  - [ ] Ch 07: Git Worktree 실습 자동화 쉘 스크립트
- [ ] 오프라인 프레젠테이션 지원을 위한 로컬 폰트 및 CSS 에셋 번들링 옵션 검토
- [ ] 슬라이드 내 라이브 코드 에디터 또는 터미널 애니메이션 인터랙션 추가
