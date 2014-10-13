# agent_email.py		written by Duncan Murray	12/10/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 
sys.path.append(root_folder)
print('agent_email, root_folder = ', root_folder)
import aikif.agents.agent as agt

sys.path.append(root_folder + os.sep + "aikif")  # should not be needed once published
import cls_log as mod_log
import config as mod_cfg

class EmailAgent(agt.Agent):
    """
    agent that logs emails. [using AIKIF logging].
    """
    
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        agt.Agent.__init__(self, name,  fldr, running)
        """
        takes a folder which contains the list of email PST files for logging
        """
        self.LOG_LEVEL = LOG_LEVEL
        self.root_folder = fldr
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
        return res
            
    def do_your_job(self, *arg):
        """
        the goal of the filelist agent is to collect metadata on files
        """ 
        lg = mod_log.Log(self.log_folder)
        lg.record_command('email_collect.txt', 'email agent - checking folder - ' + self.root_folder)

    
def main():
	agt = EmailAgent('email_agent', root_folder, True, 1)
	print(agt)

 		
		
if __name__ == '__main__':
	main()
	
	