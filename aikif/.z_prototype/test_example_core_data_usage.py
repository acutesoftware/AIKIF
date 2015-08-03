# test_example_core_data_usage.py

import unittest
import sys
import os
import time
import aikif.config as mod_cfg

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
web_app_path = root_folder + os.sep + 'aikif' + os.sep + 'examples' 
sys.path.append(web_app_path)

import core_data_usage

class CoreDataUsage(unittest.TestCase):
    def test_01_init(self):
        c = core_data_usage.root
        print(c)
        self.assertEqual(len(str(c)) > 0, True)


        
if __name__ == '__main__':
	unittest.main()
