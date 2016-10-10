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
        msg = 'This is a raw text message'
        #secret = crypto_tools.encrypt_AES('key123', msg, 'ERTE66TERTiv456')
        #result = crypto_tools.decrypt_AES('key123', secret, 'ERTE66TERTiv456')
        #self.assertEqual(msg, result)
        print('test_02_AES:original message = ' + msg)
        #print('test_02_AES:encrypted = ' + secret)
        #print('test_02_AES:decrypted = ' + result)

        
        
    def test_03_base64(self):
        poorly_enrcrypted_text = crypto_tools.encode64('hi')
        print(poorly_enrcrypted_text)
        self.assertEqual('aGk=', poorly_enrcrypted_text)
        
    def test_10_pprint_binary(self):
        pprint_renames = [
            ['0b010', '0000-010'],
            ['0b01001', '0001-001'],
            ['0b01101011', '0110-1011'],
        ]
        
        for rename in pprint_renames:
            self.assertEqual(crypto_tools.pprint_binary(rename[0]), rename[1])

        

if __name__ == '__main__':
    unittest.main()
