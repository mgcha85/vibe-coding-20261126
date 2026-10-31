<!-- Snippet to inject into AGENTS.md or .cursorrules / .opencode/rules -->
## Security & Production Guardrails (MANDATORY)

1. **Zero Secret Leaks**:
   - NEVER output, echo, or commit `.env`, `.env.dev`, `.env.prod`, or secret tokens.
   - All production keys must reside in `.env.*` and be excluded by `.gitignore`.
   - Never prefix backend-only secrets with `VITE_` or `NEXT_PUBLIC_`.

2. **Database Row Level Security (RLS)**:
   - When generating DDL SQL, ALWAYS append `ALTER TABLE <table_name> ENABLE ROW LEVEL SECURITY;`.
   - Implement comprehensive `FOR ALL` policies with `(auth.uid() = user_id)` for both `USING` and `WITH CHECK`.
   - Never inject `service_role` superuser key into client/frontend code.

3. **Safe Command Execution (Human Approval Gate)**:
   - Safe to auto-run: `ls`, `git status`, `git diff`, `ruff check`, `pytest`, `cargo check`.
   - Requires explicit confirmation before running: `rm -rf`, `DROP TABLE`, `kill`, `git push --force`.

4. **Supply Chain Defense (No Slopsquatting)**:
   - Do NOT invent or install phantom dependencies. Verify package existence on PyPI/npm before adding.
   - Always install via lockfiles: `uv sync --frozen`, `npm ci`, `cargo build --locked`.
