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

    film_fields = ('id', 'title', 'description', 'director', 'producer', 'release_date', 'rt_score')
    people_fields = ('id', 'name', 'gender', 'age', 'eye_color', 'hair_color', 'films')

    def __init__(self, films_url, people_url, timeout, scheme='https'):
        self.timeout = timeout
        self.films_url = f'{scheme}://{films_url}?fields={",".join(GhibliClient.film_fields)}'
        self.people_url = f'{scheme}://{people_url}?fields={",".join(GhibliClient.people_fields)}'
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
