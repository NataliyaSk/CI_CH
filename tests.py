import unittest
# src/tests.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import main as tested_app
import json

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    def test_get_api_endpoint(self):
        r = self.app.get('/api')
        self.assertEqual(r.json, {'status': 'test'})

    def test_mult_success(self):
        r = self.app.get('/mult?a=2&b=3')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'6.0')
##
###
if __name__ == '__main__':
    unittest.main()