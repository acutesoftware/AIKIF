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
	def test_new_goal(self):
		result = self.mygoal.get_name()
		self.assertEqual(result, 'New Goal')

	def test_success(self):
		result = self.mygoal.check_for_success()
		self.assertEqual(result, False)

	def test_time_goal(self):
		timeGoal = GoalTime(True, 5,2)
		result = timeGoal.check_for_success()
		self.assertEqual(result, False)
		
	def test_money_goal(self):
		moneyGoal = GoalMoney(True, 100,50)
		result = moneyGoal.check_for_success()
		self.assertEqual(result, False)
		
		
if __name__ == '__main__':
	unittest.main()