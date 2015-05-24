# test_api.py
# Note, this doesnt need to import the api_main.py
# rather it assumes it is running and tests the 
# functionality as if an end user was accessing it.

import unittest
import requests

import aikif.api_main as api  # ok, we dont *need* this, but good to get base URL

url = 'http://127.0.0.1:5000' + api.base_url

# allow either not logged in error, or success just while testing
valid_response = [403, 200]  # TODO - set to 200 after user login works

class TestApi(unittest.TestCase):
    
    def test_01_server_on(self):
        r = requests.get(url + 'facts')
        self.assertEqual(r.status_code in valid_response, True)

    def test_02_help(self):
        r = requests.get(url + 'help')
        self.assertEqual(len(r.text), 393)
        self.assertEqual(r.status_code, 200)  # should always pass regardless of logging in
        
    def test_02_user(self):
        #usr01 = '"user":{"password":"local","user_id":"1","username":"local"}'
        r = requests.get(url + 'users/1')
        self.assertEqual(len(r.text), 105)
        self.assertEqual('"username": "local"' in r.text, True)
        
        self.assertEqual(r.status_code, 200)  # should always pass regardless of logging in
        
if __name__ == '__main__':
    unittest.main()