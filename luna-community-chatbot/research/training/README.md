# Luna — Smart Community Chatbot Platform


> On‑platform AI for communities: classify messages (BERT), summarize long threads/PDFs, run polls, assign roles & gamify, and view engagement trends.


![Hero](docs/hero.png)


## ✨ Features
- **Message Categorization**: announcement / important / spam / casual / greeting
- **Summarize Threads**: one‑click summary of long chats
- **Polls**: quick decisions with live vote counts
- **Roles & Gamification**: Newbie → Contributor → Mentor → Legend
- **Trends**: top active members, trending topics


## 🧱 Tech Stack
- **Backend**: FastAPI, Transformers (BERT, BART), WebSockets
- **Frontend**: React + Vite + Tailwind
- **Storage**: SQLite (demo), Redis (counters)


## 🚀 Quickstart (Docker Compose)
```bash
cp .env.example .env
docker compose up --build
# Web: http://localhost:5173 | API: http://localhost:8000/docs