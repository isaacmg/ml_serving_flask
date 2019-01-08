import unittest
import requests
import json

class TestFlaskAPIs(unittest.TestCase):
    def test_allen_nlp(self):
        response = requests.get("http://0.0.0.0:5000/get_model", params={"token":"testToken", "text":"My name is dale smith what is yours?"})
        data = json.loads(json.loads(response.text))
        print(type(data))
        # Prroblem loading JSON data weird bug investigate tomorrow. WTF?????
        # Unit test to verify response data is a (JSON) dictionary object
        self.assertEqual(type(data), dict)

if __name__ == '__main__':
    unittest.main()
