# test_goal.py

import unittest
import sys
import os
lib_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "AI" + os.sep + "lib")
#print(lib_fldr)  # C:\DATA\Duncan\git\AIKIF\AI\lib  (on laptop)
sys.path.append(lib_fldr)
from cls_plan import Plan

class PlanTest(unittest.TestCase):
    
    def setUp(self):
        """ Note, this gets called for EACH test """
        unittest.TestCase.setUp(self)
        self.myplan = Plan('New Plan', '')
        self.myplan.beliefs.add('The house contains 2 bedrooms, a hallway and a kitchen')
        self.myplan.beliefs.add('The kitchen is joined to the hallway and bedroom1')
        self.myplan.beliefs.add('bedroom2 is connected to the hallway')
        self.myplan.beliefs.add('The chair is in bedroom1')
        self.myplan.beliefs.add('The ball is red')
        self.myplan.beliefs.add('The ball is not in bedroom1')
        self.myplan.desires.add('Find the ball')
        self.myplan.desires.add('Move the ball to bedroom1')
        self.myplan.intentions.add('interate each room, check for ball')
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    """ 
    tests for plans go below - use myplan instantiated object
    """
    def test_01_new_plan(self):
        result = self.myplan.get_name()
        self.assertEqual(result, 'New Plan')

    def test_02_get_plan_str(self):
        result = str(self.myplan)
        self.assertEqual(result[0:42], '---==  Plan ==---- \nname        : New Plan')
    
    def test_03_count_beliefs(self):
        self.assertEqual(len(self.myplan.beliefs.list()), 6)

    def test_04_count_desires(self):
        self.assertEqual(len(self.myplan.desires.list()), 2)
        
    def test_05_count_intentions(self):
        self.assertEqual(len(self.myplan.intentions.list()), 1)
    
    def test_06_plan_string_size(self):
        self.assertEqual(len(str(self.myplan)), 475)

    def test_10_save_plan(self):    
        self.myplan.save_plan('plan_test.txt')
    
    def test_11_reload_plan(self):
        plan2 = Plan('', '')
        plan2.load_plan('plan_test.txt')
        self.assertEqual(len(str(plan2)), 475)
    
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.myplan))
        pass
    
if __name__ == '__main__':
    unittest.main()