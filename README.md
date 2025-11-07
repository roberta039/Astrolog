# Astrolog - Fullstack Natal Chart App (Template)

This repository is a starter template for a natal chart application:
- Frontend: Next.js (TypeScript) – deploy on Vercel
- Backend: FastAPI + Swiss Ephemeris – deploy on Render
- Database: Supabase (Postgres)

## Quickstart (local)

### Backend
1. Create a virtualenv and install requirements:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```
2. Copy `backend/.env` to `.env` and fill in your Supabase values.
3. Run uvicorn:
   ```bash
   uvicorn backend.main:app --reload --port 8000
   ```

### Frontend
1. Install dependencies in `frontend/` and run dev:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## Deploy
- Frontend: push to GitHub and connect to Vercel (set environment variables in Vercel dashboard)
- Backend: deploy on Render (Docker or Python service) and set env vars
- Supabase: run `supabase/schema.sql` and `supabase/seed_data.sql` in SQL editor
