# test_core_data.py

import unittest
import sys
import os
import aikif.core_data as mod_core

test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")

class CoreDataTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.c = mod_core.CoreData('test') 
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.c = None

    def test_01_instantiate(self):
        print(self.c)
        self.assertEqual(len(str(self.c)) , 4) 
 
    def test_02_object(self):
        f = mod_core.Object('Food')
        self.assertEqual(str(f) , 'Food') 
        f.expand('List', ['Apples', 'Chops', 'Cheese'])
        self.assertEqual(str(f.drill_down()[0]) , 'Apples') 
        self.assertEqual(str(f.drill_down()[1]) , 'Chops') 
        self.assertEqual(str(f.drill_down()[2]) , 'Cheese') 
    
        
if __name__ == '__main__':
    unittest.main()