# test_plan_search.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "lib")
sys.path.append(lib_fldr)
import cls_plan_search as mod_plan

goal =  ['1','2','3','4','5','6','7','8','0']
start = ['2','7','1','3','5','0','6','8','4']

class PlanSearchTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.myplan = mod_plan.Plan('8 Puzzle', [], goal, start)
        

    """ 
    tests for plans go below - use myplan instantiated object
    """
    def test_01_new_plan(self):
        self.assertEqual(self.myplan.nme, '8 Puzzle')

 
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        print(str(self.myplan))
        pass
    
if __name__ == '__main__':
    unittest.main()