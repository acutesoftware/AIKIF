# test_agent.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")
sys.path.append(root_fldr)
import agents.agent as mod_agent

class AgentTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.agt = mod_agent.Agent('test_agent_number_685848')
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_str(self):
        self.assertEqual(len(str(self.agt)), 113)

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
    
    def test_99(self):
        """ prints the test to screen to make sure all is ok """
        #print(str(self.agt))
        pass
    
if __name__ == '__main__':
    unittest.main()