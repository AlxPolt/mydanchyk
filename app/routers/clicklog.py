# app/routers/clicklog.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import ClickLog
from app.db.session import get_session

router = APIRouter(prefix="/clicklog", tags=["clicklog"])

@router.post("/")
async def log_click(click: ClickLog, session: AsyncSession = Depends(get_session)):
    session.add(click)
    await session.commit()
    await session.refresh(click)
    return {"status": "success", "click_id": click.id}
