#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_agg_load_PC_usage.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(os.path.join(root_fldr, "agents", "aggregate"))

import agent_pcusage as mod_usage

diary_folder = os.getcwd() 
op_file = os.getcwd() + os.sep + 'summary_diary.dat'

    
class AgentAggLoadPCUsageTest(unittest.TestCase):

    def test_01_process_all(self):
        """
        
        """
        print('testing new version...')
        #mod_usage.process_all(diary_folder, op_file)
        
        #self.assertEqual(os.path.exists(op_file), True)
        

 
if __name__ == '__main__':
    unittest.main()