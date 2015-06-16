#!/usr/bin/python3
# test_agent_agg_context.py

import os
import unittest
import aikif.agents.aggregate.agg_context as mod_agg
class TestAgentAggContext(unittest.TestCase):
    def test_01_(self):
        #mod_agg.do_your_job()
        #mod_agg.results
        
        agentFileList = mod_agg.AggContext()
        agentFileList.start()
        print(agentFileList.report())
            
        
        print(agentFileList.results)
        self.assertEqual(1,1)
    
if __name__ == '__main__':
    unittest.main()
