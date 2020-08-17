import redis
import pickle
import logging
from functools import wraps

logger = logging.getLogger(__name__)


def log_err(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except redis.RedisError as e:
            logger.error(f'Cannot connect to redis: {e}')
            raise ConnectionError
    return wrapper


class Database:

    def __init__(self, host, port, timeout, key_all_films):
        self.redis = redis.Redis(host=host, port=port, socket_timeout=timeout)
        self.key_all_films = key_all_films
        logger.info(f'Redis configured: {host}:{port}')

    @log_err
    def push(self, films_map):
        self.redis.set(self.key_all_films, pickle.dumps(films_map))
        for k, v in films_map.items():
            self.redis.set(k, pickle.dumps(v))
        logger.info(f'Pushed {len(films_map)} films to cache')
