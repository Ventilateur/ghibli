import requests
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def log_err(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except requests.exceptions.Timeout or requests.exceptions.ConnectionError as e:
            logger.error(f'{f.__name__}: Cannot connect to Ghibli API: {e}')
            raise ConnectionError
    return wrapper


class GhibliClient:

    def __init__(self, ghibli_url, films_path, people_path, timeout, scheme='https'):
        self.timeout = timeout
        self.films_url = f'{scheme}://{ghibli_url}/{films_path}'
        self.people_url = f'{scheme}://{ghibli_url}/{people_path}'
        logger.info(f'Ghibli http client configured: films at {self.films_url}, people at {self.people_url}')

    @log_err
    def get_films(self):
        films = requests.get(self.films_url, timeout=self.timeout).json()
        logger.info(f'Got {len(films)} films')
        return films

    @log_err
    def get_people(self):
        people = requests.get(self.people_url, timeout=self.timeout).json()
        logger.info(f'Got {len(people)} people')
        return people
