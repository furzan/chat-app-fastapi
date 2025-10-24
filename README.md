# chat-app-fastapi

Minimal FastAPI chat service using an `agents` SDK with a Gemini-compatible Chat Completions API. Serves simple HTML pages and stores chat history in SQLite.

### Prerequisites
- Python 3.10+
- Install deps: `pip install -r requirements.txt`

### Run
```bash
fastapi dev src/
```

### Open
- Login: `http://127.0.0.1:8000/app/`
- Chat: `http://127.0.0.1:8000/app/chat-app`

### API
- `GET /app/` → login page
- `GET /app/chat-app` → chat page
- `GET /app/history/{user}` → list messages
- `DELETE /app/clear-history/{user}` → clear messages
- `POST /app/chat/{user}` → send `{ "input": "Hello" }`

