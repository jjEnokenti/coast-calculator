import os

from dotenv import load_dotenv


__all__ = (
    'settings',
)

load_dotenv()


class BaseConfig:
    DB_USER = os.environ.get('DB_USER', 'postgres')
    DB_NAME = os.getenv('DB_NAME', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '5432')

    DATABASE_URL = f'asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


settings = BaseConfig()
