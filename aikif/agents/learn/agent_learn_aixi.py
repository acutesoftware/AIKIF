# agent_learn_aixi.py		written by Duncan Murray	14/12/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." ) 
sys.path.append(root_folder)
print("agent_learn_aixi : root_folder = " + root_folder)
import aikif.agents.agent as mod_agt
import aikif.cls_log as mod_log
import aikif.config as mod_cfg


# setup logging at the top (same for all Agents)
log_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + ".." + os.sep + 'data' + os.sep + 'log') 
print('log_folder = ' + log_folder)

try:		
    from pyaixi import agent, agents, environment, environments, util
    from pyaixi.agent import Agent
    from pyaixi.agents import *
    from pyaixi.environment import Environment
    from pyaixi.environments import *
except:
    sys.exit("you need to install pyaixi")

def TEST():
    agt = Aixi('pyaixi_tictactoe', log_folder)
    agt.do_your_job()
        
class Aixi(mod_agt.Agent):
    """
    test agent to run pyaixi
    """
    def __init__(self, name,  fldr):
        """
        First setup aikif logging then initialise pyaixi
        """
        mod_agt.Agent.__init__(self, name,  fldr)
        self.lg = mod_log.Log(fldr)
        self.lg.record_command('Initialise pyaixi - tic tac toe', 'agent_learn_aixi.py')
        #print(self.lg)
        self.start()
        
       
    def __str__(self):
        res = ''
        res += self.name
        return res
    
    def do_your_job(self):
        """
        overrides method in Agent class in agent.py
        """
        self.lg.record_source('passing parameters NNNN', 'agent_learn_aixi.py')
        
        print('Running Aixi agent - TODO, actually *run* the agent here')
        
        
        self.lg.record_result('result = ', 'agent_learn_aixi.py')
        
        
        sum = mod_log.LogSummary(self.lg, 'T:\\user\\AIKIF\\log')
        sum.summarise_events()
        print(sum)
        
TEST()