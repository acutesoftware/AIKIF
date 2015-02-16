# test_toolbox_image_tools.py   written by Duncan Murray 1/7/2014

import unittest
import os
import sys
import csv
import PIL
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )

import image_tools as cl

test_file1 = root_folder + os.sep + 'doc' + os.sep + 'web-if-progs-v01.jpg'
test_file2 = root_folder + os.sep + 'doc' + os.sep + 'web-if-v01.jpg'

                    
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
    
    