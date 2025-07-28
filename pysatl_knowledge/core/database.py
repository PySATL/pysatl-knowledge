from requests import session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from pysatl_knowledge.core.config import settings

engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    async with AsyncSession() as s:
        yield s
