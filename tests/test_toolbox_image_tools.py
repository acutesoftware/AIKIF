# test_toolbox_image_tools.py   written by Duncan Murray 1/7/2014

import unittest
import os
import sys
import csv
import PIL
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'toolbox' )

import image_tools as cl

test_file1 = root_folder + os.sep + 'doc' + os.sep + 'AIKIF-Overview.jpg'
test_file2 = root_folder + os.sep + 'doc' + os.sep + 'web-if-v02.jpg'

                    
class TestClassImageTools(unittest.TestCase):

    def test_01_load_image(self):
        image = cl.load_image(test_file1)
        self.assertEqual(type(image), PIL.JpegImagePlugin.JpegImageFile)   
        #image = None        
        
    def test_02_image_hash(self):
        image = cl.load_image(test_file1)
        img = cl.get_img_hash(image)  
        self.assertEqual(len(img), 16) 
       
    def test_03_image_metadata(self):       
        metadata = cl.get_metadata_as_dict(test_file1)
        self.assertEqual(metadata['basename'], 'AIKIF-Overview.jpg')   
        self.assertEqual(metadata['path'], root_folder + os.sep + 'doc')   
        self.assertEqual(metadata['size'], '270240')   
        self.assertEqual(metadata['format'], 'JPEG')   
        self.assertEqual(metadata['palette'], 'None')   
        self.assertEqual(metadata['height'], '826')   
        self.assertEqual(metadata['width'], '1416')   
        #self.assertEqual(metadata['sum'], '287910356.0,288202246.0,279748839.0,')   
        #self.assertEqual(metadata['mean'], '246.15801767417682,246.40757821370434,239.18007192104076,')   
        #self.assertEqual(metadata['var'], '1927.892721349111,1920.204495654775,2483.0614587628343,')   
        #self.assertEqual(metadata['sum2'], '73126336674.0,73261119374.0,69814575843.0,')   
        #self.assertEqual(metadata['count'], '1169616,1169616,1169616,')   
        #self.assertEqual(metadata['median'], '255,255,255,')   
        #self.assertEqual(metadata['stddev'], '43.90777518104409,43.82013801501286,49.83032669733196,')   
        #self.assertEqual(metadata['rms'], '250.0433210198374,250.27364842667234,244.31571431841436,')   
        self.assertEqual(metadata['lat'], 'None')   
        self.assertEqual(metadata['lon'], 'None')   

        """
        for k,v in metadata.items():
            print(k,v)
        """
        
if __name__ == '__main__':
    unittest.main()
    
    