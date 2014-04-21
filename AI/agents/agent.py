# Agent.py	written by Duncan Murray 21/4/2014
# Base class for agents in AIKIF
# This class manages the starting and stopping of agents, 
# so it is the interface to whatever method will be used
#  (e.g. mail, http, # subprocess, ?)
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
#import sys
#sys.path.append('..//..//AI')
#sys.path.append('..//..//..//aspytk')
#import AI.AIKIF_utils as aikif
#import AI.fileMapping as filemap 
		
agent_status = [  	'NONE',				# agent was never instantiated (then how would it report this?)
					'RUNNING', 			# agent is running
					'STOPPED', 		    # agent was stopped - not sure if it finished or not
					'FINISHED', 		# agent has finished performing its task, ready to report
					'READY', 			# agent has reported its results back, and is ready for next command
					'WAITING', 			# agent is running, but waiting on other input
					'ERROR', 			# agent has encountered an error it cannot handle
			]
				
class Agent(object):
	"""
	Class for Agents in AIKIF, all agents base class this
	"""
	def __init__(self, name=None,  fldr=None, running=False):
		self.name = name
		self.fldr = fldr
		self.running = running
		self.results = []
		self.status = 'READY'
		print('Agent.py	: Creating Agent', self.name)
		if self.running is True:
			self.start()

	def start(self):
		"""
		Starts an agent with standard logging
		"""
		self.running = True
		self.status = 'RUNNING'
		print('Agent.py	: starting', self.name)
		#self.results.append('The answer is 7')
		self.do_your_job()	# starts the process
	
	def do_your_job(self):
		"""
		Main method which does the actual work required.
		This method needs to be subclassed in your agents
		code, but should also call this for the logging and
		status updates.
		"""
		#aikif.LogProcess(self.name, 'agent.py')
		print('use aikif.LogProcess .... [buggy with module loading - TODO]')

	
	def stop(self):
		"""
		Stops an agent with standard logging
		"""
		self.running = False
		self.status = 'STOPPED'
		#print('Agent.py	: starting', self.name)
		
	def check_status(self):
		"""
		Requests an agent to report its status as a single string 
		(see allowed strings in agent_status
		"""
		return self.status
		
	def report(self):
		"""
		Requests an agent to report its results as a dictionary
		"""
		return self.results
		

def TEST():
	myAgent = Agent('TEST Agent', 'T:\\user\\dev\\src\\python\\AI', True)
	manualAgent = Agent('manual', 'T:\\user\\dev\\src\\python\\AI', False)
	manualAgent.start()
	manualAgent.stop()
	print(manualAgent.check_status())
	print(manualAgent.report())
	
if __name__ == '__main__':
	TEST()
	print('Agent.py - TEST was about to be called')
	
	