#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_template.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'web_app' 
sys.path.append(web_app_path)

import web_aikif


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        self.assertEqual(1,1)


if __name__ == '__main__':
    unittest.main()
