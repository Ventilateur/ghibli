import redis
import pickle
import logging

logger = logging.getLogger(__name__)


class DB:

    def __init__(self, host, port, timeout, key_all_films):
        self.redis = redis.Redis(host=host, port=port, socket_timeout=timeout)
        self.key_all_films = key_all_films
        logger.info(f'Redis configured: {host}:{port}')
        try:
            self.redis.ping()
        except TimeoutError or ConnectionError:
            logger.error('Cannot connect to redis')

    def get_all(self):
        films = self.redis.get(self.key_all_films)
        return pickle.loads(films) if films is not None else None

    def get_film(self, film_id):
        film = self.redis.get(film_id)
        return pickle.loads(film) if film is not None else None

    def ping(self):
        return self.redis.ping()
