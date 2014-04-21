# agg_context.py		written by Duncan Murray	21/4/2014
# program to create a list and weightings of contexts
# from usage data to determine what is happening
# other programs in the learn folder will decide what the list
# of contexts mean (so this only aggregates the data)

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
		
import os, sys
sys.path.append('T:\\user\\dev\\src\\python\\AI\\AI')  # why is this needed when called from run_agents in root??
#from agent import Agent
from agents.agent import Agent

class AggContext(Agent):
	def __init__(self, *arg):
		Agent.__init__(self, *arg)

	def do_your_job(self, *arg):
		print('AggContext... ')
		self.results.append('This is your agent code here - TODO')
	
	
def main():
	test = AggContext('agg_context',  'T:\\user\\AIKIF', True)
	print(test.report())

		
		
if __name__ == '__main__':
	main()
	
	