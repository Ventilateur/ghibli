import config
import time
import logging
import data_aggregate
from ghibli_client import GhibliClient
from database import Database

logging.basicConfig(level=config.LOG['level'])

ghibli = GhibliClient(
    config.GHIBLI['films_url'],
    config.GHIBLI['people_url'],
    config.GHIBLI['timeout']
)

db = Database(
    config.REDIS['host'],
    config.REDIS['port'],
    config.REDIS['timeout'],
    config.REDIS['key_all_films']
)


def collect_data():
    try:
        films = ghibli.get_films()
        people = ghibli.get_people()
        films_map = data_aggregate.aggregate(films, people)
        db.push(films_map)
    except ConnectionError:
        # We have already logged errors before
        pass


if __name__ == '__main__':
    rate = config.RATE_SEC
    while True:
        collect_data()
        time.sleep(rate)
