import re

char = '[0-9a-zA-Z]'
p = re.compile(f'.*({char}{{8}}-{char}{{4}}-{char}{{4}}-{char}{{4}}-{char}{{12}}).*')


def get_film_id(url):
    match = p.match(url)
    if match:
        return match.group(1)
    else:
        return ''


def aggregate(films, peoples):
    # Build a map of film_id -> film for easy searching
    film_map = {}
    for film in films:
        # Replace broken people record by an array that we will populate later
        film['people'] = []
        film_map[film['id']] = film
        # Remove redundant id field
        film.pop('id', None)

    for people in peoples:
        # Get film ids from film urls and remove 'films' object from people
        for film_id in [get_film_id(film_url) for film_url in people.pop('films', None)]:
            if film_id in film_map:
                film_map[film_id]['people'].append(people)

    return film_map
