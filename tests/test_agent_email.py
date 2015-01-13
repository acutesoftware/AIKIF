# test_agent_email.py     written by Duncan Murray 6/9/2014
# unit testing for agent email class

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)

import agents.gather.agent_email as agt
                    
class AgentEmailTest(unittest.TestCase):
         
    def test_01_instantiation(self):
        account = agt.GmailAccount('username', 'password')   
        email = agt.EmailAgent('TEST_email_agent', root_folder, True, 1 , account)
        self.assertEqual(email.account.send_server, 'smtp.gmail.com:587')
        
if __name__ == '__main__':
    unittest.main()