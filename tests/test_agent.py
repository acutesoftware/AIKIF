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

class AgentTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.agt = mod_agent.Agent(name='test_agent_number_685848', fldr=os.getcwd())
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_str(self):
        #print(str(self.agt))
        self.assertTrue(len(str(self.agt)) > 99)

    def test_02_name(self):
        self.assertEqual(self.agt.name, 'test_agent_number_685848')
        
    def test_03_start_agent(self):
        self.agt.start()
        self.assertEqual(self.agt.status, 'RUNNING')
        self.assertEqual(self.agt.check_status(), 'RUNNING')
        
    def test_04_stop_agent(self):
        self.agt.stop()
        self.assertEqual(self.agt.status, 'STOPPED')
        self.assertEqual(self.agt.check_status(), 'STOPPED')
    
    
if __name__ == '__main__':
    unittest.main()
