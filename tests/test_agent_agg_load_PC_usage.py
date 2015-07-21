#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_agg_load_PC_usage.py

import unittest
import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr + os.sep + "agents" + os.sep + "aggregate")

import load_PC_usage as mod_usage

diary_folder = os.getcwd() + os.sep + 'test_results'
op_file = os.getcwd() + os.sep + 'test_results' + os.sep + 'summary_diary.dat'

    
class AgentAggLoadPCUsageTest(unittest.TestCase):

    def test_01_process_all(self):
        mod_usage.process_all(diary_folder, op_file)
        
        self.assertEqual(os.path.exists(op_file), True)
        
 
 
 
if __name__ == '__main__':
    unittest.main()