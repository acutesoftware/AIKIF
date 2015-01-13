# test_agent_email.py     written by Duncan Murray 13/1/2015
# unit testing for agent email class

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)

import agents.gather.agent_email as email_agt
                    
class AgentEmailTest(unittest.TestCase):
    def setUp(self):
        self.account = email_agt.GmailAccount('username', 'password')   
        self.agt = email_agt.EmailAgent('TEST_email_agent', root_folder, True, 1 , self.account)
          
    def test_01_instantiation(self):
        self.assertEqual(len(str(self.agt)),319)
      
    def test_02_username(self):
        self.assertEqual(self.account.username, 'username')

    def test_03_password(self):
        self.assertEqual(self.account.password, 'password')

    def test_04_send_server(self):
        self.assertEqual(self.account.send_server, 'smtp.gmail.com:587')

    def test_05_rec_server(self):
        self.assertEqual(self.account.rec_server[0], 'imap.gmail.com')
        self.assertEqual(self.account.rec_server[1],  993)

        
if __name__ == '__main__':
    unittest.main()