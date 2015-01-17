# test_plan_search.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "lib")
sys.path.append(lib_fldr)
import cls_plan_search as mod_plan

class PlanSearchTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.myplan = mod_plan.Plan('New Plan', [[0,0],[1,2]], [1,2,3,4,67,3], 40, 0)
        

    """ 
    tests for plans go below - use myplan instantiated object
    """
    def test_01_new_plan(self):
        self.assertEqual(self.myplan.nme, 'New Plan')

 
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        print(str(self.myplan))
        pass
    
if __name__ == '__main__':
    unittest.main()