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
        self.assertNotEqual(msg,b)
        self.assertFalse(msg in b)
        self.assertEqual(msg,crypto_tools.bin2txt(b))
        
    def test_02_AES(self):
        """
        wont work unless crypto installed
        """
        pass
        
        
    def test_03_base64(self):
        poorly_enrcrypted_text = crypto_tools.encode64('hi')
        print(poorly_enrcrypted_text)
        self.assertEqual('aGk=', poorly_enrcrypted_text)
        
        

if __name__ == '__main__':
    unittest.main()
