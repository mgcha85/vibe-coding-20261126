#!/usr/bin/env bash
# ==============================================================================
# Production Security Guardrails Audit Script
# Validates .env git isolation, RLS on SQL migrations, and frontend secret leaks
# ==============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

ERRORS=0

echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}🛡️ Running Production Security Guardrails Audit...${NC}"
echo -e "${BLUE}====================================================${NC}\n"

# 1. Check .gitignore for .env protection
echo -e "🔍 [Check 1] Verifying .gitignore for .env file exclusion..."
if [ -f ".gitignore" ] && grep -E '^\.env' .gitignore > /dev/null 2>&1; then
    echo -e "  ${GREEN}✓ .gitignore properly excludes .env files${NC}"
else
    echo -e "  ${RED}✗ FAILED: .gitignore does not contain .env exclusion rule!${NC}"
    ERRORS=$((ERRORS + 1))
fi

# 2. Check if any real secret .env files are tracked by Git (excluding .env.example/.template)
echo -e "\n🔍 [Check 2] Scanning Git tracking index for tracked .env files..."
TRACKED_ENV=$(git ls-files | grep -E '^\.env(\..+)?$' | grep -vE '\.(example|template)$' || true)
if [ -z "$TRACKED_ENV" ]; then
    echo -e "  ${GREEN}✓ No secret .env files are tracked in Git index.${NC}"
else
    echo -e "  ${RED}✗ CRITICAL: Tracked secret .env files found in Git!${NC}"
    echo "$TRACKED_ENV"
    ERRORS=$((ERRORS + 1))
fi

# 3. Check for SQL files missing Row Level Security
echo -e "\n🔍 [Check 3] Inspecting SQL DDL migrations for ENABLE ROW LEVEL SECURITY..."
SQL_FILES=$(find . -maxdepth 3 -name "*.sql" -not -path "*/.*" 2>/dev/null || true)
if [ -n "$SQL_FILES" ]; then
    MISSING_RLS=0
    for sql in $SQL_FILES; do
        if grep -qi "CREATE TABLE" "$sql" && ! grep -qi "ENABLE ROW LEVEL SECURITY" "$sql"; then
            echo -e "  ${YELLOW}⚠️  Warning: $sql contains CREATE TABLE but missing ENABLE ROW LEVEL SECURITY!${NC}"
            MISSING_RLS=$((MISSING_RLS + 1))
        fi
    done
    if [ "$MISSING_RLS" -eq 0 ]; then
        echo -e "  ${GREEN}✓ All SQL tables properly enforce RLS.${NC}"
    else
        echo -e "  ${YELLOW}⚠️ Found $MISSING_RLS SQL file(s) requiring RLS review.${NC}"
    fi
else
    echo -e "  ${BLUE}ℹ No standalone SQL files found in root.${NC}"
fi

# 4. Check for frontend bundle secret prefix leak
echo -e "\n🔍 [Check 4] Scanning frontend files for private secret keys in VITE_/NEXT_PUBLIC_..."
LEAK_FOUND=0
if grep -rnE '(VITE_|NEXT_PUBLIC_).*(SECRET|PRIVATE|SERVICE_ROLE)' src/ 2>/dev/null; then
    echo -e "  ${RED}✗ CRITICAL: Secret key exposed with frontend public prefix!${NC}"
    ERRORS=$((ERRORS + 1))
else
    echo -e "  ${GREEN}✓ No private secrets found with public frontend prefixes.${NC}"
fi

echo -e "\n----------------------------------------------------"
if [ "$ERRORS" -eq 0 ]; then
    echo -e "${GREEN}🎉 Guardrail Audit PASSED: System meets production security baseline.${NC}"
    exit 0
else
    echo -e "${RED}🚨 Guardrail Audit FAILED: $ERRORS critical issue(s) detected. Fix before deploying!${NC}"
    exit 1
fi
