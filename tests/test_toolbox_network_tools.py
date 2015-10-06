# test_network_tools.py

import unittest
import sys
import os
import time
import aikif.config as mod_cfg

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "toolbox" )
sys.path.append(root_fldr)

import network_tools as mod_net

creditionals_file = mod_cfg.fldrs['pers_credentials'] + os.sep + 'dummy.cred'
                
class NetworkToolsTest(unittest.TestCase):

    def test_01_get_user_name(self):
        #self.assertEqual(mod_net.get_user_name(), 'Duncan')  # comment this out if you try this elsewhere
        self.assertEqual(len(mod_net.get_user_name()) > 1, True)

    def test_02_get_host_name(self):
        #self.assertEqual(mod_net.get_host_name(), 'Treebeard')  # comment this out if you try this elsewhere
        self.assertEqual(len(mod_net.get_host_name()) > 1, True)

    def test_03_download_file1(self):
        fname = os.getcwd() + os.sep + 'test_country.txt'
        if os.path.exists(fname):
            os.remove(fname)

        url = 'http://gdeltproject.org/data/lookups/CAMEO.country.txt'
        mod_net.download_file_no_logon(url, fname)
        self.assertEqual(os.path.isfile(fname), True)
        time.sleep(1)
        os.remove(fname)
        
    def test_04_read_username_password(self):
        pass
        with open('dummy_credentials.txt', 'w') as f:
            f.write('dummy_username\ndummy_password\n')
        username, password = mod_net.load_username_password('dummy_credentials.txt')
        self.assertEqual(username, 'dummy_username')
        self.assertEqual(password, 'dummy_password')

    def test_05_download_file_password_protected(self):
        username, password = mod_net.load_username_password('dummy_credentials.txt')
        self.assertEqual(username, 'dummy_username')
        
        url = 'http://www.acutesoftware.com.au/about.html'
        op_file = 'secret.html'
        #mod_net.download_file('test_5', url, op_file, username, password)
        #mod_net.get_protected_page( url, None, None, op_file)
        #self.assertEqual(os.path.isfile(op_file), True)
        

        
if __name__ == '__main__':
    unittest.main()
