

class DataAggregate:

    ID_KEY = 'id'
    FILMS_KEY = 'films'
    PEOPLE_KEY = 'people'

    def __init__(self, films_url):
        self.films_url = films_url

    def get_film_id(self, url):
        return url[len(self.films_url) + 1:]

    def aggregate(self, films, peoples):
        # Build a map of film_id -> film for easy searching
        film_map = {}
        for film in films:
            # Replace broken people record by an array that we will populate later
            film[self.PEOPLE_KEY] = []
            film_map[film[self.ID_KEY]] = film

        for people in peoples:
            # Get film ids from film urls and remove 'films' object from people
            for film_id in [self.get_film_id(film_url) for film_url in people.pop(self.FILMS_KEY, None)]:
                if film_id in film_map:
                    film_map[film_id][self.PEOPLE_KEY].append(people)

        return film_map


if __name__ == '__main__':
    from http_client import GhibliClient
    client = GhibliClient('https://ghibliapi.herokuapp.com', '/films', '/people')
    aggregate = DataAggregate(client.films_url)
    print(aggregate.aggregate(client.get_films(), client.get_people()))
