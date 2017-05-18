# test_agent_learn_aixi.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif"  + os.sep + "agents" + os.sep + "learn")
test_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_results" + os.sep + "log")
sys.path.append(root_fldr)
import agent_learn_aixi as mod_aixi

class AgentLearnAixiTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.ax = mod_aixi.Aixi('this is a test', test_fldr)
        
    def tearDown(self):
        """ called once at the end of this test class """
        unittest.TestCase.tearDown(self)

    def test_01_instantiate_class(self):
        self.assertTrue(len(str(self.ax)) > 10)

    def test_02_run_as_bat(self):
        try:
            print(('deleting logfile - ' + mod_aixi.log_file))
            os.remove(mod_aixi.log_file)
        except: 
            pass
        self.ax.do_your_job()
        self.assertTrue(os.path.getsize(mod_aixi.log_file) > 10000)

        
if __name__ == '__main__':
    unittest.main()