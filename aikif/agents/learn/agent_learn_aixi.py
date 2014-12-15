# agent_learn_aixi.py		written by Duncan Murray	14/12/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." ) 
sys.path.append(root_folder)
print("agent_learn_aixi : root_folder = " + root_folder)
import aikif.agents.agent as agt
import cls_log

try:		
    from pyaixi import agent, agents, environment, environments, util
    from pyaixi.agent import Agent
    from pyaixi.agents import *
    from pyaixi.environment import Environment
    from pyaixi.environments import *
except:
    sys.exit("you need to install pyaixi")

def TEST():
    agt = Aixi('test aixi', root_folder, True, 1)
    print(agt)
        
class Aixi(agt.Agent):
    """
    test agent to run pyaixi
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL

        
    def __str__(self):
        res = ''
        res += self.name
        return res
        
TEST()