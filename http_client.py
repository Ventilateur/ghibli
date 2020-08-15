import requests


class GhibliClient:
    def __init__(self, ghibli_url, films_path, people_path):
        self.films_url = ghibli_url + films_path
        self.people_url = ghibli_url + people_path

    def get_films(self):
        return requests.get(self.films_url).json()

    def get_people(self):
        return requests.get(self.people_url).json()


if __name__ == "__main__":
    client = GhibliClient('https://ghibliapi.herokuapp.com', '/films', '/people')
    print(client.get_films())
    print(client.get_people())
