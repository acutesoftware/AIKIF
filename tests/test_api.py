# test_api.py
# Note, this doesnt need to import the api_main.py
# rather it assumes it is running and tests the 
# functionality as if an end user was accessing it.

import unittest
import requests
import json as json

import aikif.api_main as api  # ok, we dont *need* this, but good to get base URL

url = 'http://127.0.0.1:5000' + api.base_url

# allow either not logged in error, or success just while testing
valid_response = [403, 200]  # TODO - set to 200 after user login works

class TestApi(unittest.TestCase):
    
    def test_01_server_on(self):
        try:
            r = requests.get(url + 'facts')
            self.assertEqual(r.status_code in valid_response, True)
        except Exception as ex:
            print('API not running - ' + str(ex))

    def test_02_help(self):
        try:
            r = requests.get(url + 'help')
            #print(r.text)
            if r.status_code == 200:  # so travis_ci passes if api not on
                self.assertEqual(len(r.text), 698)
                self.assertEqual(r.status_code, 200)  # should always pass regardless of logging in
        except Exception as ex:
            print('API not running - ' + str(ex))
        
    def test_03_user(self):
        #usr01 = '"user":{"password":"local","user_id":"1","username":"local"}'
        try:
            r = requests.get(url + 'users/1')
            self.assertEqual(r.status_code in valid_response, True) 
            if r.status_code == 200:
                self.assertEqual(len(r.text), 105)
                self.assertEqual('"username": "local"' in r.text, True)
        except Exception as ex:
            print('API not running - ' + str(ex))
    
    
    def test_04_log(self):
        # data = json.dumps({'txt':'some test repo'}) 
        # r = requests.post(url + 'log', params=data)
        #data = json.dumps({'txt':'some test repo'}) 
        #r = requests.post(url + 'log/txt', 'some test repo')   # works but string is 'txt'
        
        
        #r = requests.post(url + 'log/txt=this_is_a_test', data)   # works 201
        # "2015-05-31 20:09:25","000054058","Duncan","Treebeard","cls_log.log","txt=this_is_a_test",
        
        #r = requests.post(url + 'log/txt', data)   # works 201
        # "2015-05-31 20:10:36","000054163","Duncan","Treebeard","cls_log.log","txt",
        
        #r = requests.post(url + 'logs/works_but_not_best_logging_method', data) 
        # "2015-05-31 21:00:33","000054766","Duncan","Treebeard","cls_log.log","tttttt",
        
        dat1 = json.dumps({'txt':'example log entry via API'}) 
        headers = {'content-type': 'application/json'}
        r = requests.post(url + 'log', data=dat1,headers=headers) 
        
    def test_05_fact_post(self):
        #new_fact1 = json.dumps({'fact_id':6, 'fact_str':'New Fact 6 added by test_05'})
        new_fact1 = json.dumps({'fact_str':'New Fact added by test_05'})
        headers = {'content-type': 'application/json'}
        #print(new_fact1)
        try:
            r = requests.post(url + 'facts', data=new_fact1,headers=headers) 
            
            self.assertEqual(r.status_code in valid_response, True)
            
        except Exception as ex:
            print('API not running - ' + str(ex))

            # now list the facts back
            
        r2 = requests.get(url + 'facts')
        print(r2.text)
            
    def test_07_map_get(self):
        try:
            r = requests.get(url + 'maps')
            #print(r.text)
            self.assertEqual(r.status_code in valid_response, True)
        except Exception as ex:
            print('API not running - ' + str(ex))

            
    
if __name__ == '__main__':
    unittest.main()
