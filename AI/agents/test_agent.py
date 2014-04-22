# test_agent.py		written by Duncan Murray	21/4/2014
# program to demonstrate how to use the Agent class
# USAGE - e.g. test_agent.py
		# from agent import Agent
		# class TestAgent(Agent):
		# 	def __init__(self, *arg):
		# 		Agent.__init__(self, *arg)
		#
		# def main():
		# 	test = TestAgent('hello',  os.getcwd())
		# 	test.start()
		# 	print(test.check_status())
		# 	print(test.report())
		
import os
from agent import Agent

class TestAgent(Agent):
	def __init__(self, *arg):
		Agent.__init__(self, *arg)

	def do_your_job(self, *arg):
		print(' ---- your agents code goes here ---- ')
		self.results.append('answer = 15.665')
	
	
def main():
	test = TestAgent('test_agent',  'T:\\user\\AIKIF', True)
	print(test.report())

 		
		
if __name__ == '__main__':
	main()
	
	