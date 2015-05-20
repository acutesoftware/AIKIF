# test_network_tools.py

import unittest
import sys
import os
import time
import aikif.config as mod_cfg

from aikif.toolbox import network_tools as mod_net

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
        try:
            os.remove(fname)
        except:
            pass
        url = 'http://gdeltproject.org/data/lookups/CAMEO.country.txt'
        mod_net.download_file_no_logon(url, fname)
        self.assertEqual(os.path.isfile(fname), True)
        time.sleep(1)
        os.remove(fname)
        
    def test_04_read_username_password(self):
        pass
        #username, password = mod_net.load_username_password(creditionals_file)
        #self.assertEqual(username, 'dummy_username')
        #self.assertEqual(password, 'dummy_password')

    def test_05_download_file_password_protected(self):
        """
        download a file from a password protected site
        print('NOTE - replace line below with your own creditionals file')
        private_file = mod_cfg.fldrs['pers_credentials'] + os.sep + 'regnow.cred' 
        username, password = mod_net.load_username_password(private_file)
        #self.assertEqual(username, '3580')
        url = 'https://admin.mycommerce.com/vendorpriv/orders.cgi'
        login_page = 'https://admin.mycommerce.com/app/cp/login/vendor'
        op_file = mod_cfg.fldrs['pers_credentials'] + os.sep + 'regnow.html'
        try:
            os.remove(op_file)
        except:
            pass
        print('downloading....')
        mod_net.download_file('regnow', url, op_file, username, password)
        self.assertEqual(os.path.isfile(op_file), True)
        """
        pass
        

		
if __name__ == '__main__':
	unittest.main()