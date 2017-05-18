# agg_context.py		written by Duncan Murray	21/4/2014
# program to create a list and weightings of contexts
# from usage data to determine what is happening
# other programs in the learn folder will decide what the list
# of contexts mean (so this only aggregates the data)

# USAGE - e.g. test_agent.py
# from agent import Agent
# class TestAgent(Agent):
# 	def __init__(self, *arg):
# 		Agent.__init__(self, *arg)
#
# def main():
# 	test = TestAgent('hello',  os.getcwd())
# 	test.start()
# 	print(test.check_status())
# 	print(test.report())
        
import os, sys
from aikif.agents.agent import Agent
aikif_dir = os.path.dirname(os.path.abspath(__file__))


if len(sys.argv) == 3:   # folder and filename passed on command line
    localFolder = sys.argv[1] 
    fileListSrc = sys.argv[2]
else:
    localFolder = aikif_dir + os.sep
    fileListSrc = 'file_sample.csv' 
#print('localFolder = ', localFolder)
#print('fileListSrc = ', fileListSrc)

    
def main():
    agentFileList = AggContext()
    agentFileList.start()
    print((agentFileList.report()))
    
    
class AggContext(Agent):
    def __init__(self, *arg):
        Agent.__init__(self, *arg)
         
    def do_your_job(self):
        """
        This is the function that actually does the work of the agent subclass 
        """
        fullfilenames, files, folders = summarise_filelist(localFolder + fileListSrc)
        print(('AggContext found ' + str(len(files)) + ' files'))
        self.results.append(['Found ' + str(len(fullfilenames)) + ' files in ' + str(len(folders)) + ' folders'] )
    
def summarise_filelist(fname):
    """ 
    takes a filelister.py generated filelist and returns a summary 
    """
    from collections import Counter
    import operator
            
    def saveListWithCounts(fname, lst):
        """ 
        takes a list of strings, counts unique values and saves to a file 
        """
        with open(fname, 'w', encoding="utf8") as f:
            counts = Counter( sorted(lst) )
            sorted_x = sorted(list(counts.items()), key=operator.itemgetter(0))
            for l in sorted_x:
                f.write('"' + l[0] + '","' +  str(l[1]) + '",\n')
    
    
    def multi_split(line, split_chars):
        res = [line]
        for sep in split_chars:
            line, res = res, []
            for seq in line:
                res += seq.split(sep)
        return res

    fullfilenames = []
    files = []
    folders = []
    print(('Summarizing FileList = ', fname))
    with open(fname, 'r', encoding="utf8") as f:
        for line in f:
            if len(line) > 0:
                try:
                    cols = line.split('","')
                    fullfilenames.append(cols[0].strip('"'))
                    files.append(cols[1].strip('"').strip(' '))
                    folders.append(cols[2].strip('"').strip(' '))
                except Exception:
                    pass
                    
    # make an index of ALL words
    print('generating index')
    ndx = []
    for line in fullfilenames:
        words = multi_split(line, ['\\', ' ', '_', '-', '.', ','])
        for word in words:
            ndx.append(word.strip(' ').strip('').strip('"').strip('"'))
    
    saveListWithCounts(localFolder + 'lf_files.csv', sorted(files))
    saveListWithCounts(localFolder + 'lf_folders.csv', sorted(folders))
    saveListWithCounts(localFolder + 'lf_words.csv', sorted(ndx))
    
    return fullfilenames, (files), (folders)
    
            
if __name__ == '__main__':
    main()
    
    