import asyncio
from app.db.session import engine
from app.models import models

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    print("✅ Database tables created successfully.")

if __name__ == "__main__":
    asyncio.run(init_models())
