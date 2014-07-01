# test_toolbox_image_tools.py   written by Duncan Murray 1/7/2014

import unittest
import os
import sys
import csv
sys.path.append("..\\AI\\toolbox")
import image_tools as cl

test_file1 = "..\\doc\\web-if-progs-v01.jpg"
test_file2 = "..\\doc\\web-if-v01.jpg"

#test_files = get_sample_file_list()

def get_sample_file_list():
    """
    returns a list of valid files to test
    """
    return [
        "..\\doc\\web-if-progs-v01.jpg", 
        "..\\doc\\web-if-v01.jpg"
    ]

					
class TestClassCollect(unittest.TestCase):
 
    def setUp(self):
        pass

    def test_image_tools_start(self):
        img = cl.get_img_hash(test_file1)  
        self.assertEqual(len(img), 5404) 
        
           

    
if __name__ == '__main__':
	unittest.main()