
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_session
from app.models.models import Court
from sqlalchemy.future import select


router = APIRouter(prefix="/courts", tags=["courts"])

@router.get("/")
async def get_all_courts(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Court))
    return result.scalars().all()

@router.post("/")
async def create_court(court: Court, session: AsyncSession = Depends(get_session)):
    session.add(court)
    await session.commit()
    await session.refresh(court)
    return court

@router.get("/{court_id}")
async def get_court(court_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Court).where(Court.id == court_id))
    court = result.scalar_one_or_none()
    if not court:
        raise HTTPException(status_code=404, detail="Court not found")
    return court

