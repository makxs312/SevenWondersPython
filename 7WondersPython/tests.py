import unittest
import json
from runserver import app
from werkzeug.datastructures import MultiDict, ImmutableMultiDict

class SevenWonders_tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    def test_home_data(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the response data
        self.assertEqual(result.status_code, 200)

    def test_get_cities(self):
        result = self.app.get('/api/Cities/GetCities')
        self.assertEqual(result.status_code, 200)

    def test_get_city(self):
        result = self.app.get('/api/Cities/GetCity', query_string={'id':'29'}, content_type='application/json',
            environ_base={
                'HTTP_USER_AGENT': 'Chrome',
                'REMOTE_ADDR': '127.0.0.1'
            })
        self.assertEqual(result.status_code, 200)

    def test_add_city(self):
        result = self.app.post('/api/Cities/AddCity', data=json.dumps(dict(Id='7777', Name='Gondolin', CountryId='2', IsDeleted='False')),
                              content_type='application/json',
            environ_base={
                'HTTP_USER_AGENT': 'Chrome',
                'REMOTE_ADDR': '127.0.0.1'
            })
        self.assertEqual(result.status_code, 200)

    def test_delete_city(self):
        result = self.app.post('/api/Cities/DeleteCity', data=json.dumps(5),
                              content_type='application/json',
            environ_base={
                'HTTP_USER_AGENT': 'Chrome',
                'REMOTE_ADDR': '127.0.0.1'
            })
        self.assertEqual(result.status_code, 200)
if __name__ == '__main__':
    unittest.main()
