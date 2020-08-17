import redis
import pickle
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def log_err(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs), 200
        except redis.TimeoutError or redis.ConnectionError as e:
            logger.error(f'Cannot connect to redis: {e}')
            return None, 500
    return wrapper


class Controller:

    def __init__(self, host, port, timeout, key_all_films):
        self.redis = redis.Redis(host=host, port=port, socket_timeout=timeout)
        self.key_all_films = key_all_films
        logger.info(f'Redis configured: {host}:{port}')
        self.ping()

    @log_err
    def get_all(self):
        films = self.redis.get(self.key_all_films)
        return pickle.loads(films) if films is not None else None

    @log_err
    def get_film(self, film_id):
        film = self.redis.get(film_id)
        return pickle.loads(film) if film is not None else None

    @log_err
    def ping(self):
        return self.redis.ping()
