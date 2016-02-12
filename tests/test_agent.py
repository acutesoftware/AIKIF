#!/usr/bin/python3
# coding: utf-8
# test_agent.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "agents" )
test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")
sys.path.append(root_fldr)
import agent as mod_agent

agt = mod_agent.Agent(name='test_agent_number_685848', fldr=os.getcwd())

class AgentTest(unittest.TestCase):

    def test_01_str(self):
        #print(str(self.agt))
        self.assertTrue(len(str(agt)) > 99)

    def test_02_name(self):
        self.assertEqual(agt.name, 'test_agent_number_685848')
        
    def test_03_start_agent(self):
        agt.start()
        self.assertEqual(agt.status, 'RUNNING')
        self.assertEqual(agt.check_status(), 'RUNNING')
        
    def test_04_stop_agent(self):
        agt.stop()
        self.assertEqual(agt.status, 'STOPPED')
        self.assertEqual(agt.check_status(), 'STOPPED')
    
    def test_05_agent_coords(self):
        self.assertEqual(agt.get_coords(), {'x':0, 'y':0, 'z':0, 't':0})
        agt.set_coords({'x':546.343, 'y':-1, 'z':6949395996, 't':9})
        self.assertEqual(agt.get_coords(), {'x':546.343, 'y':-1, 'z':6949395996, 't':9})
        
    
    
if __name__ == '__main__':
    unittest.main()
