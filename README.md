# 말이 코드가 되는 시대 : 바이브 코딩(Vibe Coding)의 이상과 현실, 그리고 프로덕션 엔지니어링

**한국지능시스템학회 2026 추계학술대회 (KIIS 2026) 3시간 튜토리얼 발표 슬라이드**

## 1. 개요
- **일시**: 2026년 11월 26일(목) 13:00 ~ 16:00 (3시간)
- **장소**: 김포대학교 글로벌캠퍼스 211-B호
- **강사**: 차민규 AI Engineer (LG AI & Big Data Group, Agentic AI 팀)

## 2. 파일 구조 (모듈러 슬라이드 아키텍처)
```text
├── index.html               # 빌드된 16:9 반응형 슬라이드 (더블클릭 실행 가능)
├── template.html            # 프레젠테이션 엔진 템플릿 (16:9 프레임, 단축키 이벤트 등)
├── build.py                 # slides/ 컴포넌트들을 index.html로 0.01초 만에 합쳐주는 초경량 빌더
├── slides/                  # 챕터별 독립 슬라이드 컴포넌트 (각 파일 30~50줄)
│   ├── 00-intro/            # 표지, 강사 소개, 로드맵, 전체 아젠다
│   ├── 01-lineage/          # Ch 01 계보 (AutoGPT 실패, 2024 논문 대폭발, SWE-bench)
│   ├── 02-essence/          # Ch 02 본질 (Karpathy 선언, Intent 합성, 현실 점검)
│   ├── 03-launch/           # Ch 03 런칭 (Vercel, Supabase, Stripe, 1시간 데모)
│   ├── 04-toolchain/        # Ch 04 툴체인 (CoALA 인지 아키텍처 실무 매핑)
│   └── 99-summary/          # 요약 및 다음 세션 예고
├── start.sh                 # 자동 컴파일 & 구동 스크립트
├── stop.sh                  # 정지 스크립트
├── podman-compose.yml       # 컨테이너 기반 정적 호스팅 명세
├── .github/workflows/
│   └── pages.yml            # GitHub Pages 자동 빌드 & 배포 워크플로우
└── docs/
    ├── curriculum.md        # 3시간 타임테이블 및 챕터 1~8 상세 강의계획서
    └── TODO.md              # 프로젝트 현황 및 향후 계획
```

## 3. 슬라이드 실행 방법

### 로컬 브라우저에서 바로 열기
`index.html` 파일을 크롬이나 사파리, 엣지 등 현대적인 브라우저에서 더블 클릭하여 바로 열 수 있습니다.

### start.sh 로 기동하기
```bash
# 개발 모드 (기본 포트 8080)
./start.sh dev

# 프로덕션 모드 (기본 포트 80)
./start.sh prod
```

### 단축키 안내
- **다음 슬라이드**: `→` (오른쪽 화살표), `Space`, `PageDown`
- **이전 슬라이드**: `←` (왼쪽 화살표), `PageUp`
- **전체화면 토글**: `F`
- **전체 목차 열기/닫기**: `M`
- **첫/마지막 슬라이드**: `Home` / `End`
