from fastapi import APIRouter, Body
from fastapi.exceptions import HTTPException
from typing import List, Optional, Dict
from fastapi.responses import HTMLResponse, RedirectResponse, StreamingResponse
from pathlib import Path
from agents import SQLiteSession
from src.agent.main import runagent, clear_session_data, get_session_data

router = APIRouter()
session: Optional[SQLiteSession] = None
db_path = Path(__file__).resolve().parent.parent / 'db' / 'conversation.db'


@router.get('/', response_class=HTMLResponse)
async def login_page():
    template_path = Path(__file__).resolve().parent.parent / 'pages' / 'login.html'
    if not template_path.exists():
        raise HTTPException(status_code=404, detail=f"Template not found: {template_path}")
    try:
        content = template_path.read_text(encoding='utf-8')
    except OSError as e:
        raise HTTPException(status_code=500, detail=f"Error reading template: {e}")
    return HTMLResponse(content)


@router.get('/chat-app', response_class=HTMLResponse)
async def chat_app():
    template_path = Path(__file__).resolve().parent.parent / 'pages' / 'app.html'
    if not template_path.exists():
        raise HTTPException(status_code=404, detail=f"Template not found: {template_path}")
    try:
        content = template_path.read_text(encoding='utf-8')
    except OSError as e:
        raise HTTPException(status_code=500, detail=f"Error reading template: {e}")
    return HTMLResponse(content)


@router.get('/login/{user}')
async def login(user: str):
    print('redirecting to app')
    return RedirectResponse(url='http://127.0.0.1:8000/app/chat-app')


@router.delete('/clear-history/{user}')
async def clear_history(user: str):
    print(f'clearing user history for {user}')
    await clear_session_data(SQLiteSession(user, str(db_path)))
    return {"status": "cleared"}


@router.get('/history/{user}')
async def get_history(user: str):
    print('fetching user history')
    data = await get_session_data(SQLiteSession(user, str(db_path)))
    return data


@router.post('/chat/{user}')
async def chat(user: str, payload: dict = Body(...)):
    print('handling chat request')

    user_input = None
    if isinstance(payload, dict):
        user_input = payload.get('input') or payload.get('message')
    else:
        raise HTTPException(status_code=400, detail='Invalid payload')

    if not user_input:
        raise HTTPException(status_code=400, detail='Missing "input" or "message" in request body')

    try:
        result = await runagent(str(user_input), SQLiteSession(user, str(db_path)))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"response": result}

