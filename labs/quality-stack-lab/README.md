# Python Quality Stack 5대 하네스 실습 팩

본 실습 팩은 바이브 코딩(AI 코드 생성) 시 Python의 동적 타이핑과 런타임 취약점을 방어하기 위해 설계된 **5대 품질 하네스(Quality Stack)** 실전 프로젝트입니다.

---

## 🛠️ 5대 도구 및 개별 테스트 명령어

### 1. 패키지 & 환경 관리 (`uv`)
초고속 가상환경 구성 및 의존성 동기화
```bash
uv sync
```
실행 데모:
```bash
uv run python -m src.api.main
```

### 2. 초고속 정적 린터 (`Ruff`)
코드 스타일, 미사용 import, 위험 구문 0.01초 검사 및 자동 수정
```bash
uv run ruff check
# 자동 교정 시:
uv run ruff check --fix
```

### 3. 엄격한 정적 타입 체커 (`Pyright`)
None 역참조, 잘못된 속성 접근, 타입 불일치 배포 전 차단
```bash
uv run pyright
```

### 4. 아키텍처 계층 수호 (`import-linter`)
계층 침범(Domain이 UI를 역참조하는 스파게티 의존성) 원천 차단
단방향 계층 강제: `src.api` ➔ `src.services` ➔ `src.domain`
```bash
uv run lint-imports
```

### 5. 런타임 스키마 & 단위 테스트 (`Pydantic` + `Pytest`)
LLM의 JSON 환각 차단 및 자율 자가치유 단위 테스트
```bash
# Pydantic 런타임 스키마 검증만 집중 실행:
uv run pytest tests/test_pydantic.py -v

# 전체 단위 테스트 실행:
uv run pytest -v
```

---

## 🚀 5대 하네스 한 번에 일괄 실행
```bash
./run_checks.sh
```
또는
```bash
uv run ruff check && uv run pyright && uv run lint-imports && uv run pytest
```
