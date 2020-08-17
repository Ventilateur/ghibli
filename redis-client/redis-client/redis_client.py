import redis
import pickle
import logging

logger = logging.getLogger(__name__)


class Cache:

    def __init__(self, host, port, key_all_films):
        self.redis = redis.Redis(host=host, port=port)
        self.key_all_films = key_all_films

    def push(self, films_map):
        logger.info(f'Pushing {len(films_map)} films to cache')
        self.redis.set(self.key_all_films, pickle.dumps(films_map))
        for k, v in films_map.items():
            self.redis.set(k, pickle.dumps(v))
        logger.info('Done')

    def get_all(self):
        return pickle.loads(self.redis.get(self.key_all_films))

    def get_film(self, film_id):
        return pickle.loads(self.redis.get(film_id))
