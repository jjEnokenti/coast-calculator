from src.config.config import settings


TORTOISE_ORM = {
    'connections': {'default': settings.DATABASE_URL},
    'apps': {
        'models': {
            'models': ['src.models', 'aerich.models'],
            'default_connection': 'default',
        }
    },
}
