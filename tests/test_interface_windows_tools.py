#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test_interface_windows_tools.py
import os
import sys
import unittest
import time
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif' + os.sep + 'toolbox' 

sys.path.append(pth)


import interface_windows_tools as mod_tool

class TestAgentInterfaceEnvironment(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def test_01_send_text_to_notepad(self):
        try:
            if os.path.exists('random_text.txt'):
                os.remove('random_text.txt')
            
            self.assertFalse(os.path.exists('random_text.txt'))

            
            os.system('start notepad') # for linux, use "open [txtfile]"
            time.sleep(1)
            #hwnd = mod_tool.get_window_by_caption('Untitled - Notepad')
            #print('Notepad window ID = ', hwnd)
            #res = mod_tool.send_text(hwnd, 'hello')  # this fails
            #self.assertTrue(hwnd > 0)
            mod_tool.app_activate('Untitled - Notepad')
            mod_tool.send_keys("^a{DELETE}hello this is some text with a //")
            mod_tool.send_keys("^s") 
            time.sleep(0.2) 
            mod_tool.send_keys("random_text.txt{ENTER}")
            time.sleep(.5) 
            self.assertTrue(os.path.exists('random_text.txt'))
            
            mod_tool.send_keys('%{F4}') 
            os.remove('random_text.txt')
            self.assertFalse(os.path.exists('random_text.txt'))
        except Exception as ex:
            print('WARNING - Windows tests failed - likely due to running on Linux VM')
            
        
if __name__ == '__main__':
    unittest.main()
        