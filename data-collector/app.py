import config
import time
import logging
from data_aggregate import DataAggregate
from ghibli_client import GhibliClient
from redis_client import Cache

logging.basicConfig(level=config.LOG['level'])

ghibli = GhibliClient(
    config.GHIBLI['url'],
    config.GHIBLI['films_path'],
    config.GHIBLI['people_path']
)

cache = Cache(
    config.REDIS['host'],
    config.REDIS['port'],
    config.REDIS['key_all_films']
)

aggregator = DataAggregate(
    ghibli.films_url,
    config.GHIBLI['id_key'],
    config.GHIBLI['films_key'],
    config.GHIBLI['people_key']
)


def collect_data():
    films = ghibli.get_films()
    people = ghibli.get_people()
    films_map = aggregator.aggregate(films, people)
    cache.push(films_map)


if __name__ == '__main__':
    while True:
        collect_data()
        time.sleep(config.RATE_SEC)
