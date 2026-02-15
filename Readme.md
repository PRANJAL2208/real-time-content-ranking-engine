# Real-Time Intelligent Content Ranking Engine

A distributed-ready semantic news aggregation and ranking backend system.

## Features

- News ingestion via API
- PostgreSQL storage
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- FastAPI REST interface
- Automatic vector index building on startup

## Tech Stack

- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Sentence Transformers
- FAISS

## Setup Instructions

### 1. Clone the repository

git clone <repo_url>
cd news_engine

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate  (Windows)

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create PostgreSQL database

CREATE DATABASE newsdb;

Update DATABASE_URL in storage/db.py accordingly.

### 5. Initialize database

python init_db.py

### 6. Ingest articles

python -m ingestion.crawler

### 7. Run API

uvicorn api.main:app --reload

Open browser:
http://127.0.0.1:8000/docs

## Architecture

Crawler → PostgreSQL → Embedding Model → FAISS → FastAPI

## Future Enhancements

- Kafka event-driven ingestion
- Elasticsearch BM25 ranking
- Hybrid search
- Distributed deployment
- Caching layer
- Monitoring & benchmarking

