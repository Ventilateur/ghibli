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


if __name__ == '__main__':
    cache = Cache('localhost', 6379)
    fm = {
        'film 1': ['laputa', 'incognito'],
        'film 2': ['atupal', 'otingocni'],
    }
    cache.push(fm)
    print(cache.get_all())
    print(cache.get_film('film 1'))
    print(cache.get_film('film 2'))
