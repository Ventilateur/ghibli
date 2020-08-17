import os

RATE_SEC = os.environ.get('RATE_SEC', 5)

LOG = {
    'level': os.environ.get('LOG_LEVEL', 'INFO')
}

REDIS = {
    'host': os.environ.get('REDIS_HOST', 'localhost'),
    'port': os.environ.get('REDIS_PORT', 6379),
    'timeout': os.environ.get('REDIS_TIMEOUT_SEC', 1.0),
    'key_all_films': os.environ.get('REDIS_KEY_ALL_FILMS', 'all')
}

GHIBLI = {
    'films_url': os.environ.get('GHIBLI_FILMS_URL', 'ghibliapi.herokuapp.com/films'),
    'people_url': os.environ.get('GHIBLI_PEOPLE_URL', 'ghibliapi.herokuapp.com/people'),
    'timeout': os.environ.get('GHIBLI_TIMEOUT_SEC', 1.0)
}
