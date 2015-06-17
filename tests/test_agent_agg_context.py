#!/usr/bin/python3
# test_agent_agg_context.py

import os
import sys
import unittest
root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
print('Running unit test for - ' + root_fldr)
sys.path.insert(0, root_fldr)

import aikif.agents.aggregate.agg_context as mod_agg

class TestAgentAggContext(unittest.TestCase):
    def test_01_(self):
        agentFileList = mod_agg.AggContext()
        agentFileList.start()
        self.assertEqual(mod_agg.fileListSrc,'file_sample.csv')
        self.assertEqual(agentFileList.report(),[])
    
if __name__ == '__main__':
    unittest.main()
