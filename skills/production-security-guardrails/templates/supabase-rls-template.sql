-- ====================================================================
-- Production Security Guardrail: Golden RLS Template for PostgreSQL / Supabase
-- ====================================================================

-- 1. Example Table Creation
CREATE TABLE IF NOT EXISTS public.user_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    payload JSONB DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ DEFAULT now() NOT NULL,
    updated_at TIMESTAMPTZ DEFAULT now() NOT NULL
);

-- 2. MANDATORY: Enable Row Level Security (RLS is OFF by default in PostgreSQL!)
ALTER TABLE public.user_items ENABLE ROW LEVEL SECURITY;

-- 3. Comprehensive CRUD Policy (FOR ALL covering SELECT, INSERT, UPDATE, DELETE)
-- Prevents unauthorized reading (USING) AND unauthorized writing/tampering (WITH CHECK)
CREATE POLICY "Users can only access their own items"
ON public.user_items
FOR ALL
TO authenticated
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- 4. Public Read-Only Policy Example (e.g. Published Blog Posts)
-- CREATE POLICY "Public read for published articles"
-- ON public.articles
-- FOR SELECT
-- TO anon, authenticated
-- USING (is_published = true);

-- 5. Verification Query: Ensure RLS is active
-- SELECT tablename, rowsecurity FROM pg_tables WHERE schemaname = 'public';
