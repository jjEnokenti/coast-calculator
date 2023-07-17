import uvicorn
from tortoise.contrib.fastapi import register_tortoise

from src.config.config import settings
from src.endpoints import app


register_tortoise(
    app=app,
    db_url=settings.DATABASE_URL,
    modules={'models': ['src.models', 'aerich.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


def start():
    uvicorn.run(app=app, host='0.0.0.0', port=8000)


if __name__ == '__main__':
    start()
