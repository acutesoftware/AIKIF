# test_goal.py

import unittest
import sys
sys.path.append("..\\AI\\lib")
from cls_plan import Plan

class PlanTest(unittest.TestCase):

    def setUp(self):
        """ called once at the start of this test class """
        unittest.TestCase.setUp(self)
        self.myplan = Plan('New Plan', '')
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    """ 
    tests for plans go below - use myplan instantiated object
    """
    def test_new_plan(self):
        result = self.myplan.get_name()
        self.assertEqual(result, 'New Plan')

    def test_get_plan_str(self):
        result = str(self.myplan)
        self.assertEqual(result, '---==  Plan ==---- \nNew Plan')
        
if __name__ == '__main__':
    unittest.main()