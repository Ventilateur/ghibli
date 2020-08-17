import config
import time
import logging
from data_aggregate import DataAggregate
from ghibli_client import GhibliClient
from database import Database

logging.basicConfig(level=config.LOG['level'])

ghibli = GhibliClient(
    config.GHIBLI['url'],
    config.GHIBLI['films_path'],
    config.GHIBLI['people_path'],
    config.GHIBLI['timeout']
)

db = Database(
    config.REDIS['host'],
    config.REDIS['port'],
    config.REDIS['timeout'],
    config.REDIS['key_all_films']
)

aggregator = DataAggregate(
    ghibli.films_url,
    config.GHIBLI['id_key'],
    config.GHIBLI['films_key'],
    config.GHIBLI['people_key']
)


def collect_data():
    try:
        films = ghibli.get_films()
        people = ghibli.get_people()
        films_map = aggregator.aggregate(films, people)
        db.push(films_map)
    except ConnectionError:
        # We have already logged errors before
        pass


if __name__ == '__main__':
    rate = config.RATE_SEC
    while True:
        collect_data()
        time.sleep(rate)
