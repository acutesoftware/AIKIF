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
ip_file = os.getcwd() + os.sep + 'diary_duncan.txt'
op_file = os.getcwd() + os.sep + 'summary_diary.txt'


    
class AgentAggLoadPCUsageTest(unittest.TestCase):

    def test_01_instantiate(self):
        """
        load the class and read mapping file
        """
        p = mod_usage.PCUsageAgent('PCUsage', os.getcwd(), False, 3)
        print(p)
        self.assertEqual(str(p)[0:52], '\n--------- Agent Summary ---------\nName    : PCUsage')
        

 
    def test_02_instant_map(self):
        """
        start the map_usage object
        """
        map_file = os.path.join(root_fldr, 'data', 'ref','map_pc_usage.csv')
        #print('loading map file ', map_file)
        m = mod_usage.MapUsage(map_file)
        #print(m.maps)
        self.assertEqual(len(m.maps), 36)
        self.assertEqual(m.maps[1], ['Application', 'Right', ' - Message (HTML)', 'Outlook', 'Email', 'Work\n'])
        self.assertEqual(m.maps[12], ['Application', 'Left', 'C:\\', 'Windows Explorer', 'File Mgt', 'Any\n'])
        
 
if __name__ == '__main__':
    unittest.main()