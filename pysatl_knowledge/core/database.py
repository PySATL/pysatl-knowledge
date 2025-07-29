from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from pysatl_knowledge.core.config import settings


engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

async_session = sessionmaker(  # type: ignore
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_session():
    async with async_session() as session:
        yield session
