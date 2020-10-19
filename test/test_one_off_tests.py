import unittest
import json

class RandomTests(unittest.TestCase):
    def test_json_convert(self):
        obj = {
            'username': 'testuser',
            'password': 'testpass'
        }

        expected = "{\"username\": \"testuser\", \"password\": \"testpass\"}"
        actual = json.dumps(obj)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
