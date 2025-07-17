from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from sqlalchemy import text

router = APIRouter()

@router.get("/health/db")
async def health_check_db(session: AsyncSession = Depends(get_session)):
    try:
        await session.execute(text("SELECT 1")) 
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}