#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_toolbox_crypto_tools.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 
sys.path.append(pth)

import crypto_tools


msg = 'this is my amazing password to be encrypted'

class TestTemplate(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    
    def test_01_txt2bin(self):
        b = crypto_tools.txt2bin(msg)
        print('encode64 : ' + msg )
        print('binary   : ' + b)
        print('decode64 : ' + crypto_tools.bin2txt(b))
        self.assertEqual(msg,crypto_tools.bin2txt(b))

if __name__ == '__main__':
    unittest.main()
