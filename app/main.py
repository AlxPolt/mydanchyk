from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import courts, recommendations
from app.routers import health
from dotenv import load_dotenv
from pathlib import Path
from app.routers import slots, clicklog
import sys

import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(dotenv_path=Path('.') / '.env')
print("📦 CURRENT DB URL:", os.getenv("DATABASE_URL"))
app = FastAPI(title="Adaptive Pickleball Platform")

templates = Jinja2Templates(directory="app/templates")

app.include_router(courts.router)
app.include_router(recommendations.router)
app.include_router(health.router)
app.include_router(slots.router)
app.include_router(clicklog.router)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


print("📡 DATABASE_URL:", os.getenv("DATABASE_URL"))
