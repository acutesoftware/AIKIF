#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_webapp_page_agents.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = os.path.join(root_folder,'aikif','web_app')
  
sys.path.append(web_app_path)

import page_agents


class TestWebAppPageAgent(unittest.TestCase):

    def test_01_get_list_of_files(self):
        res = page_agents.get_page()
        #print(res)
        self.assertEqual(len(res) > 40, True)
        self.assertEqual(res[0:36], '\nAgent:test_agent_number_685848\n<BR>')



if __name__ == '__main__':
    unittest.main()
