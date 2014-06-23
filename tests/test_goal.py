# test_goal.py

import unittest
import sys
sys.path.append("..\\AI\\lib")
from cls_goal import Goal

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
		from cls_goal_time import GoalTime
		timeGoal = GoalTime(True, 5,2)
		result = timeGoal.check_for_success()
		self.assertEqual(result, False)
		
	def test_money_goal(self):
		from cls_goal_money import GoalMoney
		moneyGoal = GoalMoney(True, 100,50)
		result = moneyGoal.check_for_success()
		self.assertEqual(result, False)
		
		
if __name__ == '__main__':
	unittest.main()