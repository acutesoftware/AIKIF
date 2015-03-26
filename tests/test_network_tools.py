# test_network_tools.py

import unittest
import sys
import os
import time

from aikif.toolbox import network_tools as mod_net
				
class NetworkToolsTest(unittest.TestCase):

    def test_01_get_user_name(self):
        self.assertEqual(mod_net.get_user_name(), 'Duncan')  # comment this out if you try this elsewhere
        self.assertEqual(len(mod_net.get_user_name()) > 1, True)

    def test_02_get_host_name(self):
        self.assertEqual(mod_net.get_host_name(), 'Treebeard')  # comment this out if you try this elsewhere
        self.assertEqual(len(mod_net.get_host_name()) > 1, True)

    def test_03_download_file1(self):
        fname = os.getcwd() + os.sep + 'test_country.txt'
        try:
            os.remove(fname)
        except:
            pass
        url = 'http://gdeltproject.org/data/lookups/CAMEO.country.txt'
        mod_net.download_file_no_logon(url, fname)
        self.assertEqual(os.path.isfile(fname), True)
        time.sleep(2)
        os.remove(fname)
        

"""
def TEST():
	print(" \n --- Testing network functions  --- ")
	print(" ---------------------------------- ")
	print('username = ' + get_user_name())
	print('hostname = ' + get_host_name())
	print('downloading file http://gdeltproject.org/data/lookups/CAMEO.country.txt to test_country.txt')
	download_file_no_logon('http://gdeltproject.org/data/lookups/CAMEO.country.txt', 'test_country.txt')
	print('done')
"""


		
if __name__ == '__main__':
	unittest.main()