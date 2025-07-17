# app/routers/slots.py

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.models import Slot
from app.db.session import get_session

router = APIRouter(prefix="/slots", tags=["slots"])

@router.get("/")
async def get_slots(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Slot))
    return result.scalars().all()

@router.get("/available")
async def get_available_slots(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Slot).where(Slot.is_available == True))
    return result.scalars().all()
