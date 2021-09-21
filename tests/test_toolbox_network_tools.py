# test_network_tools.py

import unittest
import sys
import os
import time

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" )
sys.path.append(root_fldr)

import config as mod_cfg

mod_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + "aikif" + os.sep + "toolbox" )
sys.path.append(mod_fldr)

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

        #url = 'http://gdeltproject.org/data/lookups/CAMEO.country.txt'  # dont want to poll repeatedly
        url = 'https://github.com/acutesoftware/AIKIF/blob/master/aikif/data/raw/CAMEO.country.txt'
        url = 'https://raw.githubusercontent.com/acutesoftware/AIKIF/master/aikif/data/raw/CAMEO.country.txt'
        mod_net.download_file_no_logon(url, fname)
        time.sleep(1)
        self.assertEqual(os.path.isfile(fname), True)
        time.sleep(.4)
        #os.remove(fname)

    def test_03_download_failed_file(self):
        fname = os.getcwd() + os.sep + 'no_such_file.txt'
        url = 'http://no_such_file_or_domain.blah/some_file_that_doesnt_exist.mp8'
        mod_net.download_file_no_logon(url, fname)
        self.assertEqual(os.path.isfile(fname), False)

        # make sure error is logged
        with open('result.log', 'r') as f:
            lg_data = f.read()
            self.assertTrue('Error - cant download http://no_such_file_or_domain.blah/some_file_that_doesnt_exist.mp8' in lg_data)


    def test_04_read_username_password(self):
        pass
        with open('dummy_credentials.txt', 'w') as f:
            f.write('dummy_username\ndummy_password\n')
        username, password = mod_net.load_username_password('dummy_credentials.txt')
        self.assertEqual(username, 'dummy_username')
        self.assertEqual(password, 'dummy_password')

    def test_05_get_protected_page(self):
        """
        This test doesnt really confirm that the username/password works
        as it is checking a non password protected page
        """
        url = 'https://github.com/acutesoftware/AIKIF/blob/master/CHANGES.txt'
        op_file = 'toolbox_network_protected_page.html'
        mod_net.get_protected_page( url, 'username', 'password', op_file)
        self.assertEqual(os.path.isfile(op_file), True)

    def test_06_download_file_password_protected(self):
        url = 'https://raw.githubusercontent.com/acutesoftware/AIKIF/master/README.txt'
        op_file = 'toolbox_network_password_protected.html'
        mod_net.download_file('test_5', url, op_file, 'username', 'password')
        self.assertEqual(os.path.isfile(op_file), True)

    def test_07_download_file_proxy(self):
        """
        this is a dummy test on a non password page to check that
        null proxy works
        """
        url = 'https://github.com/acutesoftware/AIKIF/blob/master/LICENSE.txt'
        op_file = 'toolbox_network_download_proxy.html'
        proxy = []  # dummy test so pass no proxy
        mod_net.download_file_proxy( url, op_file, 'username', 'password', proxy)
        self.assertEqual(os.path.isfile(op_file), True)



if __name__ == '__main__':
    unittest.main()
