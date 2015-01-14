# test_agent_email.py     written by Duncan Murray 13/1/2015
# unit testing for agent email class

"""
NOTE - for Gmail, you may need to activate unsecure app access for this to work. 
Email recieved: 
--------------------------------------------
Hi Duncan, 

We recently blocked a sign-in attempt to your Google Account [acutesoftware@gmail.com]. 

Sign in attempt details
Date & Time: Tuesday, January 13, 2015 1:59:22 PM UTC 
Location: Adelaide SA, Australia 

If this wasn't you
Please review your Account Activity page at https://security.google.com/settings/security/activity 
to see if anything looks suspicious. Whoever tried to sign in to your account knows your password; 
we recommend that you change it right away. 

If this was you
You can switch to an app made by Google such as Gmail to access your account (recommended) 
or change your settings at https://www.google.com/settings/security/lesssecureapps so that 
your account is no longer protected by modern security standards. 

To learn more, see https://support.google.com/accounts/answer/6010255. 

Sincerely,
The Google Accounts team
--------------------------------------------

Switched to unsecure access, and got the email confirmation, but still not working:

You recently changed your security settings so that your Google Account 
[acutesoftware@gmail.com] is no longer protected by modern security standards. 


"""

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)
import config as mod_cfg

import agents.gather.agent_email as email_agt
                    
class AgentEmailTest(unittest.TestCase):
    def setUp(self): #setUp
        with open(mod_cfg.fldrs['localPath'] + 'ac.txt', 'r') as f:
            self.username = f.readline().strip('\n')
            self.password = f.readline().strip('\n')
        self.account = email_agt.GmailAccount(self.username, self.password)  
        self.agt = email_agt.EmailAgent('TEST_email_agent', root_folder, True, 1 , self.account)
        print('class instantiated for testing...')

    def test_01_parameters(self):
        self.assertEqual(len(str(self.agt)),343)
        self.assertEqual(self.account.username, self.username)
        self.assertEqual(self.account.password, self.password)
        self.assertEqual(self.account.send_server_name, 'smtp.gmail.com:587')
        self.assertEqual(self.account.rec_server_name[0], 'imap.gmail.com')
        self.assertEqual(self.account.rec_server_name[1],  993)

    def test_02_connect_and_disconnect(self):
        # doing this in one test rather than logon and off 8 times (causing scope error)
        print(self.account)
        self.account.connect()
        self.assertEqual(self.account.status, 'CONNECTED')
        tot_emails = self.account.get_inbox_count()
        print('tot_emails = ' + str(tot_emails))
        self.assertEqual(tot_emails > 9, True)
        
        self.account.send('djmurray@gmail.com', subject='test from AIKIF ', msg='this is a test')
        self.assertEqual(self.account.status, 'CONNECTED')
        self.account.disconnect()
        self.assertEqual(self.account.status, 'DISCONNECTED')
        

         
if __name__ == '__main__':
    unittest.main()