import unittest
import requests
import json

class TestFlaskAPIs(unittest.TestCase):
    def test_allen_nlp(self):
        response = requests.get("http://127.0.0.1:5050/get_model", data=json.dumps({"token":"testToken", "text":"My name is dale smith what is yours?"}))
        # Unit test to verify response data is a (JSON) dictionary object
        self.assertEqual(type(response.text), dict)


if __name__ == '__main__':
    unittest.main()
