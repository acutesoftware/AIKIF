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
from subprocess import call


# setup logging at the top (same for all Agents)
log_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + ".." + os.sep + 'data' + os.sep + 'log') 
current_folder = os.path.dirname(os.path.abspath(__file__))
pyaixi_folder = 'T:\\user\\dev\\src\\python\\pyaixi'  # temp - using existing pyaixi main
print('log_folder = ' + log_folder)
print('current_folder = ' + current_folder)

try:		
    from pyaixi import agent, agents, environment, environments, util
    from pyaixi.agent import Agent
    from pyaixi.agents import *
    from pyaixi.environment import Environment
    from pyaixi.environments import *
except:
    sys.exit("you need to install pyaixi")

    
    

    
def TEST():
    agt = Aixi('pyaixi_oscillator', log_folder)
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
        self.lg.record_command('Initialise pyaixi - oscillator', 'agent_learn_aixi.py')

        """
        # options copied from - https://github.com/gkassel/pyaixi/blob/release-1.1.0/aixi.py
        self.default_options = {}
        self.default_options["agent"]             = "mc_aixi_ctw"
        self.default_options["agent-horizon"]     = 5
        self.default_options["ct-depth"]          = 30
        self.default_options["compare"]           = ""
        self.default_options["environment"]       = "coin_flip"
        self.default_options["exploration"]       = 0.0    # Do not explore.
        self.default_options["explore-decay"]     = 1.0    # Exploration rate does not decay.
        self.default_options["learning-period"]   = 0      # Learn forever.
        self.default_options["mc-simulations"]    = 300
        self.default_options["non-learning-only"] = False  # Whether to record statistics gathered in the non-learning period only.
        self.default_options["profile"]           = False  # Whether to profile code.
        self.default_options["terminate-age"]     = 0      # Never die.
        self.default_options["verbose"]           = False
        """
        
        self.start()
        
       
    def __str__(self):
        res = ''
        res += self.name
        return res
    
    def do_your_job(self):
        """
        Run pyaixi, logging results - sample output is below:
        
        ------------------------
        -- Output from pyaixi --
        ------------------------
            OPTION: 'mc-simulations' = '10'
            OPTION: 'oscillator-delay' = '1'
            OPTION: 'explore-decay' = '1'
            OPTION: 'non-learning-only' = 'False'
            OPTION: 'learning-period' = '500'
            OPTION: 'terminate-age' = '1000'
            OPTION: 'compare' = 'aixi_uniform_random'
            OPTION: 'agent' = 'mc_aixi_ctw'
            OPTION: 'environment' = 'oscillator'
            OPTION: 'exploration' = '1'
            OPTION: 'ct-depth' = '30'
            OPTION: 'profile' = 'False'
            OPTION: 'verbose' = 'True'
            OPTION: 'random-seed' = '0'
            OPTION: 'agent-horizon' = '5'
            cycle, observation, reward, action, explored, explore_rate, total reward, average reward, time, model size
            Agent is trying an action at random...
            A: 1, 0, 0, 1, True, 1.000000, 0, 0.000000 (stdev 0.000000), 0:00:00, 3
            B: 1, 0, 0, 0, True, 1.000000, 0, 0.000000 (stdev 0.000000), 0:00:00, 0
            A: cycle: 1
            average reward: 0.000000 (stdev 0.000000)
            B: cycle: 1
            average reward: 0.000000 (stdev 0.000000)
            explore rate: 1.000000

            A: action = high, observation = high, reward = right! (1)
            B: action = low, observation = high, reward = wrong (0)
            Agent is trying an action at random...
            A: 2, 1, 1, 1, True, 1.000000, 1, 0.500000 (stdev 0.000000), 0:00:00, 6
            B: 2, 1, 0, 0, True, 1.000000, 0, 0.000000 (stdev 0.000000), 0:00:00, 0
            A: cycle: 2
            average reward: 0.500000 (stdev 0.000000)
            B: cycle: 2
            average reward: 0.000000 (stdev 0.000000)
            explore rate: 1.000000
        
        """
        self.lg.record_source('pyaixi - oscillator.conf', 'agent_learn_aixi.py')
        print('Running Aixi agent via BAT file..')
        with open('go.bat', 'w') as bat:
            bat.write('T:\n')
            bat.write('cd ' + pyaixi_folder + '\n')
            bat.write("python aixi.py -v conf/oscillator.conf -c aixi_uniform_random -o random-seed=0 > results_oscil.log\n")
        call(['go.bat'])
        self.lg.record_result('result = results_oscil.log', 'agent_learn_aixi.py')
        sum = mod_log.LogSummary(self.lg, log_folder)
        sum.summarise_events()
        print(sum)
        
TEST()