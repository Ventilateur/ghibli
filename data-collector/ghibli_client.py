import requests
import logging
import time

logger = logging.getLogger(__name__)


class GhibliClient:

    def __init__(self, ghibli_url, films_path, people_path, scheme='https'):
        self.scheme = scheme
        self.films_url = f'{scheme}://{ghibli_url}/{films_path}'
        self.people_url = f'{scheme}://{ghibli_url}/{people_path}'
        logger.info(f'Ghibli http client configured: films at {self.films_url}, people at {self.people_url}')

    def get_films(self):
        logger.info(f'Getting films at {self.films_url}')
        start = time.time_ns()
        films = requests.get(self.films_url).json()
        end = time.time_ns()
        logger.info(f'Got {len(films)} films, took {(end - start)/10e5}ms')
        return films

    def get_people(self):
        logger.info(f'Getting people at {self.films_url}')
        start = time.time_ns()
        people = requests.get(self.people_url).json()
        end = time.time_ns()
        logger.info(f'Got {len(people)} people, took {(end - start)/10e5}ms')
        return people


if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)
    client = GhibliClient('ghibliapi.herokuapp.com', 'films', 'people')
    print(client.get_films())
    print(client.get_people())
