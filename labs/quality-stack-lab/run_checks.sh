#!/usr/bin/env bash
set -e

echo "=================================================="
echo "🛡️ Python Quality Stack 5대 하네스 자동 검증"
echo "=================================================="

echo ""
echo "[1/5] uv 패키지 환경 동기화 (Package & Venv Manager)"
uv sync --quiet
echo "  ✓ uv 환경 준비 완료"

echo ""
echo "[2/5] Ruff 린트 & 코드 스타일 검사 (Fast Rust Linter)"
uv run ruff check src/ tests/
echo "  ✓ Ruff 린트 통과 (오류 0건)"

echo ""
echo "[3/5] Pyright 정적 타입 체커 (Strict Type Safety)"
uv run pyright
echo "  ✓ Pyright 타입 검사 통과 (오류 0건)"

echo ""
echo "[4/5] import-linter 아키텍처 계층 검사 (Layer Enforcement)"
uv run lint-imports
echo "  ✓ import-linter 계층 규칙 통과 (역참조 0건)"

echo ""
echo "[5/5] Pytest & Pydantic 스키마 검증 (Unit Tests & Schema Validation)"
uv run pytest -v
echo "  ✓ Pytest 단위 테스트 & Pydantic 스키마 전체 통과"

echo ""
echo "=================================================="
echo "🎉 5대 Quality Stack 하네스 전체 통과 (ALL GREEN)"
echo "=================================================="
