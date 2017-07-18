#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_data_root.py
import os
import sys
import unittest
import time
import yaml

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
data_path = os.path.join(root_folder, 'aikif', 'data', 'core')
yaml_file = os.path.join(data_path, 'root.yaml')
#yaml_file = os.path.join(data_path, 'projects.yaml')
sys.path.append(data_path)  # dont need this




print('yaml_file = ', yaml_file)
 
class TestDataRoot(unittest.TestCase):

    
    def test_01_read_file(self):
        """
        read the yaml file - example for use is in comments below
        
        print(self.yaml_data)
        
        for core in self.yaml_data:
            print(core)
            for item in self.yaml_data[core]:
                print(' - ' + item)

        """
        with open(yaml_file, 'r') as stream:
            self.yaml_data =  yaml.load(stream)
        
        self.assertEqual(len(self.yaml_data), 4)
        
        self.assertEqual(len(self.yaml_data['Interface']), 6)
        self.assertTrue('Toolbox' in self.yaml_data['Interface'])
        
        self.assertEqual(len(self.yaml_data['Environment_types']), 14)
        self.assertTrue('Grid 2D' in self.yaml_data['Environment_types'])
        
        self.assertEqual(len(self.yaml_data['Agent_types']), 5)
        self.assertTrue('Explorer' in self.yaml_data['Agent_types'])
        
        self.assertEqual(len(self.yaml_data['Toolbox_imports']), 2)
        self.assertTrue('aikif.toolbox' in self.yaml_data['Toolbox_imports'])
        
        #print(self.yaml_data)
        
        #for core in self.yaml_data:
        #    print(core)
        #    for item in self.yaml_data[core]:
        #        print(' - ' + item)
       
        
         
if __name__ == '__main__':
    unittest.main()
