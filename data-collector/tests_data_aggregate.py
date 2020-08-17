import unittest
from data_aggregate import DataAggregate


class TestDataAggregate(unittest.TestCase):
    def test_get_film_id(self):
        data_aggregate = DataAggregate('https://localhost:9000/films')
        self.assertEqual('1234', data_aggregate.get_film_id('https://localhost:9000/films/1234'))
        self.assertEqual('', data_aggregate.get_film_id('https://localhost:9000/films/'))
        self.assertEqual('', data_aggregate.get_film_id('https://localhost:9000/films'))
        self.assertEqual('', data_aggregate.get_film_id('invalid:9000/films/1234'))
        self.assertEqual('', data_aggregate.get_film_id('alongerthanexpectedurl:9000/films/1234'))

    def test_aggregate(self):
        films = [
            {'id': '1', 'people': ['unusable value'], 'value': 'film 1'},
            {'id': '2', 'people': ['unusable value'], 'value': 'film 2'},
            {'id': '3', 'people': ['unusable value'], 'value': 'film 3'}
        ]

        people = [
            {'id': '1', 'films': ['/films/1', '/films/2'], 'value': 'people 1'},
            {'id': '2', 'films': ['/films/2', '/films/3'], 'value': 'people 2'},
            {'id': '3', 'films': ['/films/1', '/films/2', '/films/3'], 'value': 'people 3'}
        ]

        aggregated = {
            '1': {'id': '1', 'value': 'film 1', 'people': [
                {'id': '1', 'value': 'people 1'},
                {'id': '3', 'value': 'people 3'}
            ]},
            '2': {'id': '2', 'value': 'film 2', 'people': [
                {'id': '1', 'value': 'people 1'},
                {'id': '2', 'value': 'people 2'},
                {'id': '3', 'value': 'people 3'}
            ]},
            '3': {'id': '3', 'value': 'film 3', 'people': [
                {'id': '2', 'value': 'people 2'},
                {'id': '3', 'value': 'people 3'}
            ]},
        }

        data_aggregate = DataAggregate('/films')
        self.assertEqual(aggregated, data_aggregate.aggregate(films, people))


if __name__ == '__main__':
    unittest.main()
