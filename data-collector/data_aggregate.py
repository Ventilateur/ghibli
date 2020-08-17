

class DataAggregate:

    def __init__(self, films_url, id_key='id', films_key='films', people_key='people'):
        self.films_url = films_url
        self.id_key = id_key
        self.films_key = films_key
        self.people_key = people_key

    def get_film_id(self, url):
        if self.films_url not in url:
            return ''
        else:
            return url[len(self.films_url) + 1:]

    def aggregate(self, films, peoples):
        # Build a map of film_id -> film for easy searching
        film_map = {}
        for film in films:
            # Replace broken people record by an array that we will populate later
            film[self.people_key] = []
            film_map[film[self.id_key]] = film

        for people in peoples:
            # Get film ids from film urls and remove 'films' object from people
            for film_id in [self.get_film_id(film_url) for film_url in people.pop(self.films_key, None)]:
                if film_id in film_map:
                    film_map[film_id][self.people_key].append(people)

        return film_map
