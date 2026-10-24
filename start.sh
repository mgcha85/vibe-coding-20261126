#!/usr/bin/env bash
set -e

# 환경 변수 결정 (기본값: dev, 인자 또는 ENV_TYPE 환경변수로 prod 지정 가능)
ENV_MODE="${1:-${ENV_TYPE:-dev}}"

ENV_FILE=".env.${ENV_MODE}"
if [ ! -f "$ENV_FILE" ]; then
    echo "⚠️  $ENV_FILE 파일이 존재하지 않습니다. .env.example을 복사하여 생성합니다."
    cp .env.example "$ENV_FILE"
fi

echo "🚀 Starting presentation slides in [$ENV_MODE] mode using $ENV_FILE..."

# export variables from env file
export $(grep -v '^#' "$ENV_FILE" | xargs)

if command -v podman-compose &> /dev/null; then
    podman-compose --env-file "$ENV_FILE" up -d
elif command -v docker-compose &> /dev/null; then
    docker-compose --env-file "$ENV_FILE" up -d
else
    # Fallback: Python 간단 웹서버 실행
    echo "ℹ️  podman-compose/docker-compose가 없어 로컬 python 웹 서버(포트: ${PORT:-8080})로 실행합니다."
    python3 -m http.server "${PORT:-8080}"
fi

echo "✅ Slides running at http://localhost:${PORT:-8080}"
