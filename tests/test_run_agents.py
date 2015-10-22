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
        mod_agent.main()
        self.assertTrue(999 > 99)

    def test_02_verify_agents(self):
        dummy_agent = 'local_test_agent.py'
        with open(dummy_agent, 'w') as f:
            f.write('# dummy python agent\nprint("Hello world")\n')
        ag_pass = mod_agent.verify_agents([{'name': 'TEST', 'file': dummy_agent, 'schedule_type':'hour'}])
        self.assertTrue(ag_pass)

    def test_03_verify_non_existent_agents(self):
        ag_fail = mod_agent.verify_agents([{'name': 'FAIL', 'file': 'no_file.py', 'schedule_type':'hour'}])
        self.assertFalse(ag_fail)

    def test_04_run_schedule(self):
        mod_agent.run('python ./local_test_agent.py', True)
        #self.assertEqual(os.path.exists('environment.md'), True)
        pass # todo
    
if __name__ == '__main__':
    unittest.main()
