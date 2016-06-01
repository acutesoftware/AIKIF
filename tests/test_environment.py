#!/usr/bin/python3
# coding: utf-8
# test_environment.py

import unittest
import aikif.environments.environment as mod_env

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