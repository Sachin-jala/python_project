from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def index():
    return Path("static/index.html").read_text(encoding="utf-8")

@app.post("/chat")
async def chat(req: Request):
    data = await req.json()
    msg = (data.get("message") or "").strip().lower()
    # Simple rule-based bot
    if "hello" in msg or "hi" in msg:
        reply = "Hello! How can I help you today?"
    elif "name" in msg:
        reply = "I'm a tiny FastAPI chatbot 🤖."
    elif "time" in msg:
        import datetime as dt
        reply = f"Current server time: {dt.datetime.now()}"
    else:
        reply = f"You said: {data.get('message','')}"
    return JSONResponse({"reply": reply})