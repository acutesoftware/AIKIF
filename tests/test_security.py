# test_security.py     written by Duncan Murray 6/8/2014
# unit testing for AIKIF - test the security module

import unittest
import os
import sys
sys.path.append('..//AI')
import security as sec


class TestSecurity(unittest.TestCase):
 
    def test_01_private_files(self):
        self.assertEqual( len(sec.privateFiles), 2)	
        
    def test_02_work_files(self):
        self.assertEqual( len(sec.workFiles), 1)
        
    def test_03_security_mappings(self):
        sec.MapSecurityLevel(sec.workFiles, 'WORK')
        sec.MapSecurityLevel(sec.privateFiles, 'FAMILY')
        self.assertEqual( len(sec.securityMappings), 3)	
    
    def test_04_show_security(self):
        self.assertEqual( len(sec.show_security()), 171)
     
if __name__ == '__main__':
    unittest.main()