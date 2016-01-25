#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_interface_environment.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'agents' 

sys.path.append(pth)


import agent_interface_env as mod_agt

class TestAgentInterfaceEnvironment(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_01_instantiate_base_class(self):
        res = mod_agt.AgentInterfaceEnv('Agent Enviroment Interface')
        self.assertEqual(str(res),'Agent Enviroment Interface is RUNNING')
        

    def test_02_instantiate_env_win(self):
        res = mod_agt.AgentInterfaceWindows('Windows Interface')
        self.assertEqual(str(res),'Windows Interface is RUNNING')
    

    def test_10_send_key_via_baseclass(self):
        res = mod_agt.AgentInterfaceEnv('Agent Enviroment Interface')
        self.assertEqual(res.send_string('blah', 'some text'),'WARNING - dont run this from base class')

    def test_11_send_key_via_env_windows(self):
        res = mod_agt.AgentInterfaceWindows('Windows Interface')
        self.assertEqual(res.send_string('blah', 'some text'),True)
        print(res)


        
if __name__ == '__main__':
    unittest.main()
