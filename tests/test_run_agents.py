#!/usr/bin/python3
# coding: utf-8
# test_run_agents.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif")

sys.path.append(root_fldr)
import run_agents as mod_agent

class AgentTest(unittest.TestCase):
    
    def test_01_run_agents(self):
        #print(str(self.agt))
        mod_agent.main()
        self.assertTrue(999 > 99)


    
if __name__ == '__main__':
    unittest.main()
