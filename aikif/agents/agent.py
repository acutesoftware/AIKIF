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
import os
import sys
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  )
sys.path.append(root_fldr)
import cls_log
import config as mod_cfg
        
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
    def __init__(self, name=None,  fldr='', running=False):
        self.name = name
        self.fldr = fldr
        self.running = running
        self.results = []
        self.status = 'READY'
        if fldr == '':
            fldr = mod_cfg.fldrs['log_folder']
        if fldr == '':
            print('ERROR - no log folder found')
            exit(1)
        self.mylog = cls_log.Log(fldr)
        self.mylog.record_command('agent', self.name + ' - initilising')
        
        if self.running is True:
            self.start()

    def __str__(self):
        """
        returns an agent summary for console mainly
        """
        txt = '\n--------- Agent Summary ---------\n'
        txt += 'Name    : ' + self.name + '\n'
        txt += 'Folder  : ' + self.fldr + '\n'
        txt += 'Status  : ' + self.status + '\n'
        if self.running == True:
            txt += 'Running : True\n'
        else:
            txt += 'Running : False\n'
        return txt
        
    def start(self):
        """
        Starts an agent with standard logging
        """
        self.running = True
        self.status = 'RUNNING'
        self.mylog.record_process('agent', self.name + ' - starting')
    
    def do_your_job(self):
        """
        Main method which does the actual work required.
        This method needs to be subclassed in your agents
        code, but should also call this for the logging and
        status updates.
        """
        self.mylog.record_process(self.name, 'agent.py')

    
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
    myAgent = Agent('TEST Agent', 'T:\\user\\AIKIF\\log', True)
    manualAgent = Agent('manual', 'T:\\user\\AIKIF\\log', False)
    manualAgent.start()
    manualAgent.stop()
    print(manualAgent.check_status())
    print(manualAgent.report())
    
if __name__ == '__main__':
    TEST()
    print('Agent.py - TEST was about to be called')
    
    