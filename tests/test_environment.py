#!/usr/bin/python3
# coding: utf-8
# test_environment.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'environments' 
sys.path.append(pth)

import environment as mod_env

class TestEnvironment(unittest.TestCase):
    
    def test_01_instantiation(self):
        e = mod_env.Environment('unit_test')
        self.assertEqual(str(e), 'Environment: unit_test\n')

    
        e.create(1) # make one environment
        res = str(e)
        print(res)
        e.destroy()
        
        self.assertEqual(res, 'Environment: unit_test\n')

    
if __name__ == '__main__':
    unittest.main()