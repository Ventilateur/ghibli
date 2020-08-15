import redis
import pickle


class Cache:

    ALL_FILMS_KEY = 'all'

    def __init__(self, host, port):
        self.redis = redis.Redis(host=host, port=port)

    def push(self, film_map):
        self.redis.set(self.ALL_FILMS_KEY, pickle.dumps(film_map))
        for k, v in film_map.items():
            self.redis.set(k, pickle.dumps(v))

    def get_all(self):
        return pickle.loads(self.redis.get(self.ALL_FILMS_KEY))

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
