# test_goal.py

import unittest
import os
import sys

root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'
sys.path.insert(0, root_fldr)

from aikif.lib.cls_goal import Goal
from aikif.lib.cls_goal_time import GoalTime
from aikif.lib.cls_goal_money import GoalMoney
                
class GoalTest(unittest.TestCase):

    def setUp(self):
        """ called once at the start of this test class """
        unittest.TestCase.setUp(self)
        self.mygoal = Goal()
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    """ 
    tests for goals go below - use mygoal instantiated object
    """
    def test_01_new_goal(self):
        result = self.mygoal.get_name()
        self.assertEqual(result, 'New Goal')

    def test_02_success(self):
        result = self.mygoal.check_for_success()
        print(self.mygoal)
        self.assertEqual(str(self.mygoal), 'New Goal')
        self.assertEqual(result, False)

    def test_03_time_goal(self):
        timeGoal = GoalTime(True, 5,2)
        result = timeGoal.check_for_success()
        self.assertEqual(result, False)
        
    def test_04_money_goal(self):
        moneyGoal = GoalMoney(True, 100,50)
        result = moneyGoal.check_for_success()
        self.assertEqual(result, False)
        moneyGoal.current_val = 200
        moneyGoal.maximise = False
        result = moneyGoal.check_for_success()
        self.assertEqual(result, True)
        
        moneyGoal.current_val = 4
        result = moneyGoal.check_for_success()
        self.assertEqual(result, False)
        
    
    def test_05_find_best_plan(self):
        g2 = Goal(name='Goal with Plan', plans=['1','2'])
        g2.find_best_plan()
        
        g_time = GoalTime(maximise=True, current_val=20, target_val=100)
        g_time.find_best_plan()
        

    def test_06_money_goal_best_plan(self):
        m = GoalMoney(True, 100,50)
        m.name = 'Money Goal - fudge, TODO'
        m.plans = ['1','2']
        print(m)
        result = m.find_best_plan()
        self.assertEqual(result, None)

        
if __name__ == '__main__':
    unittest.main()