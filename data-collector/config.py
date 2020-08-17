import os

RATE_SEC = os.environ.get('RATE_SEC', 5)

LOG = {
    'level': os.environ.get('LOG_LEVEL', 'INFO')
}

REDIS = {
    'host': os.environ.get('REDIS_HOST', 'localhost'),
    'port': os.environ.get('REDIS_PORT', 6379),
    'key_all_films': os.environ.get('REDIS_KEY_ALL_FILMS', 'all')
}

GHIBLI = {
    'url': os.environ.get('GHIBLI_URL', 'ghibliapi.herokuapp.com'),
    'films_path': os.environ.get('GHIBLI_FILMS_PATH', 'films'),
    'people_path': os.environ.get('GHIBLI_PEOPLE_PATH', 'people'),
    'id_key': os.environ.get('GHIBLI_ID_KEY', 'id'),
    'films_key': os.environ.get('GHIBLI_FILMS_KEY', 'films'),
    'people_key': os.environ.get('GHIBLI_PEOPLE_KEY', 'people')
}
