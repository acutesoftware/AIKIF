# test_install_data.py


import unittest
import os
import sys
import aikif.install_data as inst

root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__))) 
              
class TestClassFile(unittest.TestCase):
    def test_01_check_cur_folder(self):
        self.assertEqual(inst.cur_path, os.getcwd())

    def test_02_check_config_file_name(self):
        self.assertEqual(inst.config_file[-14:], 'pers_config.py') 

    def test_03_create_folders(self):
        inst.setup_folders()
        inst.create_sample_data()
        if os.path.isfile(inst.config_file):
            self.assertEqual(inst.config_file, inst.config_file) #"File Exists") 
        else:
            self.assertEqual(inst.config_file, "File Not Found") 
        
        
if __name__ == '__main__':
    unittest.main()