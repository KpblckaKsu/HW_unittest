import unittest
from unittest.case import TestCase
from main import get_unique_ids, get_stats, transformation_list
from main_2 import create_new_folder, TOKEN
import requests

class TestMain(TestCase):
    def setUp(self) -> None:
        self.test_ids = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, 54, 119, 119, 119],
            'user3': [213, 98, 98, 35]
                    }
        self.test_queries = [
            'one',
            'two words',
            'three another words',
            'four another words'
        ]
        self.test_list = [7, 'one', True, 'two words', 159]

    def test_unique_ids(self):
        res = get_unique_ids(self.test_ids)
        self.assertEqual(res, [98, 35, 15, 213, 54, 119])
        self.assertEqual(res.count(213), 1)
        self.assertIn(98 and 15, res)
        self.assertIsInstance(res, list)

    def test_get_stats(self):
        res = get_stats(self.test_queries)
        self.assertEqual(len(res), 3)
        self.assertIn(3, res.keys())
        self.assertEqual(sum(res.values()), 100)
        self.assertEqual(res[3], 50)

    def test_transformation_list(self):
        res = transformation_list(self.test_list)
        self.assertEqual(res, {7: {'one': {True: {'two words': 159}}}})
        self.assertEqual(len(res), 1)
        self.assertNotIsInstance(res, list)
        self.assertIsInstance(res, dict)


class TestMain2(TestCase):
    def setUp(self) -> None:
        self.token = TOKEN
        self.name = 'New folder'
        self.wrong_token = '123'

    def test_create_new_folder(self):
        res = create_new_folder(self.token, self.name)
        res_2 = create_new_folder(self.token, self.name)
        self.assertEqual(res_2, 409)
        self.assertEqual(res, 201)

    @unittest.expectedFailure
    def test_expect_error(self):
        res = create_new_folder(self.token, self.name)
        self.assertEqual(res, 413)

    def test_wrong_token(self):
        res = create_new_folder(self.wrong_token, self.name)
        self.assertEqual(res, 401)

    def tearDown(self) -> None:
        url = f"https://cloud-api.yandex.net/v1/disk/resources?path={self.name}"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        requests.delete(url, headers=headers)

