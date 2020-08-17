import os

LOG = {
    'level': os.environ.get('LOG_LEVEL', 'INFO')
}

REDIS = {
    'host': os.environ.get('REDIS_HOST', 'localhost'),
    'port': os.environ.get('REDIS_PORT', 6379),
    'timeout': os.environ.get('REDIS_TIMEOUT', 1),
    'key_all_films': os.environ.get('REDIS_KEY_ALL_FILMS', 'all')
}
