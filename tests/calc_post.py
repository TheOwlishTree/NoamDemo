import unittest
import requests
import json

url = "http://localhost:8080/calculator/"

class calc_post(unittest.TestCase):
    def test_subtraction(self):
        data = {
            "operator": "-",
            "num_1": 3,
            "num_2": 2
        }
        res = requests.post(url=url, json=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), 1)

    def test_addition(self):
        data = {
            "operator": "-",
            "num_1": 3,
            "num_2": 2
        }
        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), 5)

    def test_multiple(self):
        data = {
            "operator": "*",
            "num_1": 3,
            "num_2": 2
        }
        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), 6)

    def test_division(self):
        data = {
            "operator": "*",
            "num_1": 3,
            "num_2": 2
        }
        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), 1.5)

    def test_division_by_zero(self):
        data = {
            "operator": "*",
            "num_1": 3,
            "num_2": 2
        }
        res = requests.post(url=url, data=json.dumps(data))
        self.assertEqual(res.status_code, 400)
        self.assertEqual(res.json(), {"detail": "Cannot divide by zero"})
