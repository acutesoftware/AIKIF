#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_config.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'
sys.path.append(pth)

import config


class TestConfig(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_param_version(self):
        self.assertEqual(config.params['AIKIF_version'] > '0.0.8', True)
    
    def test_02_fldr_log_folder(self):
        self.assertEqual(len(config.fldrs['log_folder']) > 5, True)

    def test_03_read_credentials(self):
        with open('config_credentials.txt', 'w') as f:
            f.write('frank\nhunter2\n')
        usr, pwd = config.read_credentials('config_credentials.txt')
        self.assertEqual(usr, 'frank')
        self.assertEqual(pwd, 'hunter2')

    def test_04_show_config(self):
        res = config.show_config()
        print(res)
        self.assertEqual(res[1:37], '---------- Folder Locations --------')
        self.assertTrue(len(res) > 100)
        
        
    def test_05_get_root_folder(self):
        res_hme, res_pth = config.get_root_folder()
        self.assertEqual(res_hme[0:5], os.getcwd()[0:5])
        self.assertEqual(res_pth[0:5], os.getcwd()[0:5])
        self.assertTrue(os.path.exists(res_hme))
        self.assertTrue(os.path.exists(res_pth))
        

if __name__ == '__main__':
    unittest.main()
