# agent_filelist.py		written by Duncan Murray	24/7/2014


import os
import sys
import random
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + "..") 
sys.path.append(root_folder)
print(root_folder)
import AI.agents.agent as agt
import AI.lib.cls_filelist as fl
		

class FileListAgent(agt.Agent):
    """
    agent that gathers file metadata. The purpose of this class 
    is to manage when the filelist runs (calls cls_filelist.py)
    and how the results are saved [using AIKIF logging]
    """
    def __init__(self, name,  fldr, running, LOG_LEVEL):
        agt.Agent.__init__(self, name,  fldr, running)
        self.LOG_LEVEL = LOG_LEVEL
        if running == True:
            self.do_your_job()

    def do_your_job(self, *arg):
        """
        the goal of the filelist agent is to collect metdata on files
        """
        print("Collecting file metadata")
        lst = fl.FileList([root_folder + '\\tests'], ['*.*'], [], True)
        lst.save_filelist(lst.filelist, lst.output_file_name, ["name", "path", "size", "date"])
        print("saved filelist to ", lst.output_file_name)
    
    def check_last_updated(self):
        """
        checks the date of the output file list and returns 
        when the list was last modified
        """
        pass
        
    
def main():
	agt = FileListAgent('filelist_agent',  'T:\\user\\AIKIF', True, 3)
	print(agt.report())

 		
		
if __name__ == '__main__':
	main()
	
	