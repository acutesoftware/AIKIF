#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' 
sys.path.append(pth)

import tools


class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_instantiate_class(self):
        tools.main()
        self.assertEqual(os.path.exists('tools.txt'), True)


if __name__ == '__main__':
    unittest.main()
