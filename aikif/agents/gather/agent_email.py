# agent_email.py		written by Duncan Murray	12/10/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 
sys.path.append(root_folder)
print('agent_email, root_folder = ', root_folder)
import aikif.agents.agent as agt

class EmailAgent(agt.Agent):
    """
    agent that logs emails. [using AIKIF logging].
    """
    
    def __init__(self, name,  fldr, running, LOG_LEVEL, log_folder):
        agt.Agent.__init__(self, name,  fldr, running)
        """
        takes a folder which contains the list of email PST files for logging
        """
        self.LOG_LEVEL = LOG_LEVEL
        self.root_folder = fldr
        self.log_folder = log_folder
        self.fl_opname = log_folder + os.sep + name + '.csv'
        if running == True:
            self.do_your_job()

    def do_your_job(self, *arg):
        """
        the goal of the filelist agent is to collect metadata on files
        """ 
        print('email agent - checking folder - ' + self.root_folder + '\n')
    

    
def main():
	agt = EmailAgent('email_agent', root_folder, True, 1, 'T:\\user\\AIKIF')
	print(agt.report())

 		
		
if __name__ == '__main__':
	main()
	
	