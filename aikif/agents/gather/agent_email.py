# agent_email.py		written by Duncan Murray	12/10/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 

sys.path.append(root_folder + os.sep + "aikif")  # should not be needed once published
import cls_log as mod_log
import config as mod_cfg
sys.path.append(root_folder)
#print('agent_email, root_folder = ', root_folder)
import aikif.agents.agent as agt
#print( mod_cfg.fldrs['log_folder'])

def TEST():
    
    email_credentials = input('file containing email credentials - eg ac.txt or press enter to get prompted : ',)
    if email_credentials == '':
        username = input('gmail username : ',)
        password = input('gmail password : ')
    else:
        with open(mod_cfg.fldrs['localPath'] + email_credentials, 'r') as f:
            username = f.readline().strip('\n')
            password = f.readline().strip('\n')
            
    account = GmailAccount(username, password)   
    
    agt = EmailAgent('email_agent', root_folder, True, 1 , account)
    print(agt)

            
class EmailAgent(agt.Agent):
    """
    agent that logs emails. [using AIKIF logging].
    """
    
    def __init__(self, name,  fldr, running, LOG_LEVEL, account):
        agt.Agent.__init__(self, name,  fldr, running)
        """
        takes a folder which contains the list of email PST files for logging
        """
        self.LOG_LEVEL = LOG_LEVEL
        self.root_folder = fldr
        self.account = account
        self.log_folder = mod_cfg.fldrs['log_folder']
        self.fl_opname = self.log_folder + os.sep + name + '.csv'
        if running == True:
            self.do_your_job()

    def __str__(self):
        """
        display the current class summary
        """
        res = '--- Email Agent---\n'
        res += 'self.LOG_LEVEL   = ' + str(self.LOG_LEVEL) + '\n'
        res += 'self.root_folder = ' + self.root_folder + '\n'
        res += 'self.log_folder  = ' + self.log_folder + '\n'
        res += 'self.fl_opname   = ' + self.fl_opname + '\n'
        res += str(self.account)
        
        return res
            
    def do_your_job(self, *arg):
        """
        the goal of the email agent is to parse emails and index
        """ 
        lg = mod_log.Log(self.log_folder)
        lg.record_command('email_collect.txt', 'email agent - checking folder - ' + self.root_folder)

class EmailAccount:
    """
    base class for email account - server details based when sub-classed
    """
    def __init__(self, username, password, send_server, rec_server):
        self.username = username
        self.password = password
        self.send_server = send_server
        self.rec_server = rec_server

    def __str__(self):
        res = ' Account ---\n'
        res += 'username    = ' + self.username + '\n'
        res += 'password    = ' + self.password + '\n'
        res += 'send_server = ' + self.send_server + '\n'
        res += 'rec_server  = ' + self.rec_server[0] + '\n'
        return res
 
class GmailAccount(EmailAccount):
    def __init__(self, username, password):
        EmailAccount.__init__(self, username, password, 'smtp.gmail.com:587', ['imap.gmail.com', 993])
        
    def __str__(self):
        return '--- Gmail' + str(EmailAccount.__str__(self))
 
if __name__ == '__main__':
    TEST()	
  		

	