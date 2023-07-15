import asyncio

from tortoise import Tortoise

from src.config import settings


async def init():
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


if __name__ == '__main__':
    asyncio.run(init())
