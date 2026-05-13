# Create database fundament

import contextlib

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)

from src.conf.config import config


engine = create_async_engine(config.DB_URL)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


@contextlib.asynccontextmanager
async def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        await session.close()