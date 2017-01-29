#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_agent_image_metadata.py
import os
import sys
import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
mod_path = root_folder + os.sep + 'aikif' + os.sep + 'agents' + os.sep + 'gather' 
sys.path.append(mod_path)

import agent_image_metadata as mod_img
import aikif.lib.cls_filelist as fl 
 
"""
    ip_file = cfg.fldrs['log_folder'] + os.sep + 'filelist' + os.sep + 'cur_files.txt'
    #ip_file = cfg.fldrs['log_folder'] + os.sep + 'filelist' + os.sep + 'all_pics.txt'
    ip_file = cfg.fldrs['log_folder'] + os.sep + 'filelist' + os.sep + 'lst.txt'
    #op_file = cfg.fldrs['log_folder'] + os.sep + 'filelist' + os.sep + 'all_pics_metadata.csv'
    op_file = cfg.fldrs['log_folder'] + os.sep + 'filelist' + os.sep + 'lst_metadata.csv'
    agt = ImageMetadataAgent('image_metadata_agent', ip_file, op_file)
    print(agt.report())

"""


class TestAgentImageMetadata(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

        
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_01_collect_filelist(self):
        fl_docs = fl.FileList([root_folder + os.sep + 'doc'], ['*.jpg'], [], 'filelist_images.csv')
        for f in fl_docs.get_list():
            #print(f)
            pass
            
        fl_docs.save_filelist('filelist_images.csv', [])
        self.assertEqual(os.path.exists('filelist_images.csv'), True)

    
    def test_02_agent_image(self):
        agt = mod_img.ImageMetadataAgent('image_metadata_agent', 'filelist_images.csv', 'filelist_image_metadata.csv')
        print(agt)
        self.assertEqual(os.path.exists('filelist_image_metadata.csv'), True)
        self.assertEqual(len(str(agt))> 120, True)
        self.assertEqual(str(agt)[0:20], '\n--------- Agent Sum')


if __name__ == '__main__':
    unittest.main()
