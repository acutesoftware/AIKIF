# test_toolbox_image_detection_tools.py

import unittest
import os
import sys
import csv
import PIL
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )

import image_detection_tools as cl

test_file1 = root_folder + os.sep + 'doc' + os.sep + 'AIKIF-Overview.jpg'
test_file2 = root_folder + os.sep + 'doc' + os.sep + 'web-if-v02.jpg'

                    
class TestClassImageTools(unittest.TestCase):

    def test_01_load_image(self):
        cl.TEST(test_file1)
        print('ERROR - TODO implement these tests, once code written')
        self.assertEqual(1,1) 
       
        
if __name__ == '__main__':
    unittest.main()
    
    