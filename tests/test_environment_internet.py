#!/usr/bin/python3
# coding: utf-8
# test_environment_internet.py

import os
import sys
import unittest


root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." )
sys.path.append(os.path.join(root_fldr, 'aikif', 'environments'))
print(root_fldr)

import internet as mod_int

class TestEnvironment(unittest.TestCase):
    
    def test_01_instantiation(self):
        e = mod_int.Internet('Virtual Internet',  'Simulation of several websites')
        e.create(5)
        print(e)
        e.destroy()
        
        self.assertTrue(len(str(e)) > 50)
        self.assertEqual(len(e.websites), 5)
        
        self.assertTrue(str(e.websites[0])[0:6], '127.0.')
        self.assertTrue(len(str(e.websites[0])) > 5)
        self.assertEqual(str(e.websites[0].pages[0]), 'Test page')
        
    def test_02_mid_size(self):
        e = mod_int.Internet('Med Internet',  'Simulation of 8000 websites')
        e.create(800)
        self.assertEqual(len(e.websites), 800)
        
    def test_03_large_size(self):
        e = mod_int.Internet('Med Internet',  'Simulation of 200000 websites')
        e.create(200000)
        self.assertEqual(len(e.websites), 200000)
        
    
if __name__ == '__main__':
    unittest.main()