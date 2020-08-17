import unittest
import data_aggregate


class TestDataAggregate(unittest.TestCase):
    def test_get_film_id(self):
        uuid = 'ba924631-068e-4436-b6de-f3283fa848f0'
        self.assertEqual(uuid, data_aggregate.get_film_id(f'https://localhost:9000/films/{uuid}'))
        self.assertEqual(uuid, data_aggregate.get_film_id(uuid))
        self.assertEqual(uuid, data_aggregate.get_film_id(f'https://{uuid}:9000/films'))
        self.assertEqual('', data_aggregate.get_film_id('invalid:9000/films/ba924631-068e-4436-b6de-f3283fa848f'))
        self.assertEqual('', data_aggregate.get_film_id('invalid:9000/films/1234'))

    def test_aggregate(self):
        uuid = [
            '00000000-0000-0000-0000-000000000000',
            '11111111-1111-1111-1111-111111111111',
            '22222222-2222-2222-2222-222222222222'
        ]
        films = [
            {'id': uuid[0], 'people': ['unusable value'], 'value': 'film 0'},
            {'id': uuid[1], 'people': ['unusable value'], 'value': 'film 1'},
            {'id': uuid[2], 'people': ['unusable value'], 'value': 'film 2'}
        ]

        people = [
            {'id': '1', 'films': [f'/films/{uuid[0]}', f'/films/{uuid[1]}'], 'value': 'people 1'},
            {'id': '2', 'films': [f'/films/{uuid[1]}', f'/films/{uuid[2]}'], 'value': 'people 2'},
            {'id': '3', 'films': [f'/films/{uuid[0]}', f'/films/{uuid[1]}', f'/films/{uuid[2]}'], 'value': 'people 3'}
        ]

        aggregated = {
            uuid[0]: {'value': 'film 0', 'people': [
                {'id': '1', 'value': 'people 1'},
                {'id': '3', 'value': 'people 3'}
            ]},
            uuid[1]: {'value': 'film 1', 'people': [
                {'id': '1', 'value': 'people 1'},
                {'id': '2', 'value': 'people 2'},
                {'id': '3', 'value': 'people 3'}
            ]},
            uuid[2]: {'value': 'film 2', 'people': [
                {'id': '2', 'value': 'people 2'},
                {'id': '3', 'value': 'people 3'}
            ]},
        }

        self.assertEqual(aggregated, data_aggregate.aggregate(films, people))


if __name__ == '__main__':
    unittest.main()
