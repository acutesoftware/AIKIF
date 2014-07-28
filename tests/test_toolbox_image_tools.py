# test_toolbox_image_tools.py   written by Duncan Murray 1/7/2014

import unittest
import os
import sys
import csv
import PIL
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

                    
class TestClassImageTools(unittest.TestCase):

    def test_1_load_image(self):
        image = cl.load_image(test_file1)
        self.assertEqual(type(image), PIL.JpegImagePlugin.JpegImageFile)     
        
    def test_2_image_hash(self):
        image = cl.load_image(test_file1)
        img = cl.get_img_hash(image)  
        self.assertEqual(len(img), 16) 
        
           

    
if __name__ == '__main__':
    unittest.main()
    
    