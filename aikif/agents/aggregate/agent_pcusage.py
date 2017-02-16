#!/usr/bin/python3
# -*- coding: utf-8 -*-
# agent_pcusage.py

import os
import sys

agent_root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(agent_root_folder)
import agent as agt


class PCUsageAgent(agt.Agent):
    """
    agent that explores a world (2D grid)
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        #agt.Agent.__init__(self, *arg)
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL
        self.num_steps = 0
        self.num_climbs = 0
        
 