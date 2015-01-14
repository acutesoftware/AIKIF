# agent_email.py		written by Duncan Murray	12/10/2014


import os
import sys
import random
import imaplib
import smtplib
import email

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
    
    account.connect()
    print('Total Emails = ', account.get_inbox_count())  # works if this is just after connect (20 emails)
    search_str = "(SUBJECT Flight)"
    search_str = "ALL"
    account.get_all_emails_containing(100, search_str)
    # tok account.send('djmurray@gmail.com', subject='test from AIKIF ', msg='this is a test')

            
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
    def __init__(self, username, password, send_server_name, rec_server_name):
        self.username = username
        self.password = password
        self.send_server_name = send_server_name
        self.rec_server_name = rec_server_name
        self.status = 'NONE'
        self.server_snd = smtplib.SMTP(self.send_server_name)
        self.server_snd.starttls()
        self.server_rec = imaplib.IMAP4_SSL(self.rec_server_name[0], self.rec_server_name[1])
        
    def __str__(self):
        res = ' Account ---\n'
        res += 'username    = ' + self.username + '\n'
        res += 'password    = ' + self.password + '\n'
        res += 'send_server = ' + self.send_server_name + '\n'
        res += 'rec_server  = ' + self.rec_server_name[0] + ':' + str(self.rec_server_name[1]) + '\n'
        return res
        
        
    def connect(self):
        print('connecting with ', self.username,self.password )
        self.server_snd.login(self.username,self.password)
        self.server_rec.login(self.username,self.password)
        #self.server_snd.ehlo()
        #self.server_rec.ehlo()
        self.status = 'CONNECTED'
        print(self.status)
    
    def disconnect(self):
        self.server_snd.quit()
        self.server_rec.close()
        self.server_rec.logout()
        self.status = 'DISCONNECTED'
        print(self.status)

    def send(self, toaddr, subject='', msg=''):
        fromaddr = self.username
        headers = ["From: " + fromaddr,
                   "Subject: " + subject,
                   "To: " + toaddr,
                   "MIME-Version: 1.0",
                   "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        #self.server_snd.ehlo()
        #self.server_snd.starttls()
        self.server_snd.sendmail(fromaddr, toaddr, headers + "\r\n\r\n" + msg)
    
    def get_inbox_count(self):
        return int(self.server_rec.select('Inbox')[1][0])

    def get_all_emails_containing(self, max_emails, search_criteria="ALL"):
        """
        Downloads all (up to max_emails) messages to EML format in local AIKIF drive
        Works fine on both accounts though search fails if there are more than 10k bytes
        search string contains things as follows:
            '(FROM user@domain.com)'
            '(OR (TO "tech163@fusionswift.com") (FROM "tech163@fusionswift.com"))'
            'ALL' -> returns everything 
        """
        count_emails = 0
        response, data = self.server_rec.search(None, search_criteria)
        for num in data[0].split():
            response, data = self.server_rec.fetch(num, '(RFC822)')
            count_emails += 1
            if count_emails > max_emails:
                break
            print('Saving message # ', count_emails)
            with open(mod_cfg.fldrs['localPath'] + 'pers_data' + os.sep + 'email' + os.sep + str(count_emails) + '.eml', 'wb') as f:
                f.write(data[0][1])
 
class GmailAccount(EmailAccount):
    def __init__(self, username, password):
        EmailAccount.__init__(self, username, password, 'smtp.gmail.com:587', ['imap.gmail.com', 993])
        
    def __str__(self):
        return '--- Gmail' + str(EmailAccount.__str__(self))

class Message():
    pass
        
if __name__ == '__main__':
    TEST()	
  		

	