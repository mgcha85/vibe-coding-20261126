#!/usr/bin/env bash
set -e

ENV_MODE="${1:-${ENV_TYPE:-dev}}"
ENV_FILE=".env.${ENV_MODE}"

echo "🛑 Stopping presentation slides..."

if [ -f "$ENV_FILE" ]; then
    export $(grep -v '^#' "$ENV_FILE" | xargs)
fi

if command -v podman-compose &> /dev/null; then
    podman-compose down
elif command -v docker-compose &> /dev/null; then
    docker-compose down
else
    # Python 서빙 중지
    pkill -f "python3 -m http.server" || true
fi

echo "✅ Presentation slides stopped."
