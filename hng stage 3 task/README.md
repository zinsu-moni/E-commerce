# Insighta Labs Demographic Intelligence API

## Overview
A FastAPI backend for demographic intelligence with advanced filtering, sorting, pagination, and rule-based natural language search. Uses PostgreSQL, SQLAlchemy, Alembic, and UUID v7.

## Features
- Profiles table with strict schema
- Filtering, sorting, and pagination on `/api/profiles`
- Rule-based natural language search on `/api/profiles/search`
- CORS enabled
- Data seeding script for 2026 profiles

## Natural Language Parsing Approach
- **Rule-based only** (no AI/LLM)
- Maps keywords like `young`, `adult`, `teenager`, `male`, `female`, `from [country]`, `above`, `below`, `between`, etc. to filters
- Example mappings:
  - "young males" → gender=male, min_age=16, max_age=24
  - "females above 30" → gender=female, min_age=30
  - "people from angola" → country_id=AO
  - "adult males from kenya" → gender=male, age_group=adult, country_id=KE
  - "male and female teenagers above 17" → age_group=teenager, min_age=17
- Returns error if query cannot be parsed

## Limitations
- Only supports explicit keywords and mappings listed above
- Does not handle ambiguous or complex queries
- No AI/LLM interpretation

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up PostgreSQL and update `.env` if needed
3. Run Alembic migrations to create tables
4. Seed the database with the provided JSON file
5. Start the server: `uvicorn app.main:app --reload`

## Endpoints
- `GET /api/profiles` — Filtering, sorting, pagination
- `GET /api/profiles/search` — Natural language search

## Error Handling
All errors follow:
```
{ "status": "error", "message": "<error message>" }
```

## CORS
CORS is enabled for all origins.
