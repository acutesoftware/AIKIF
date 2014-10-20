# cls_log.py    written by Duncan Murray 13/9/2014

import os
import sys
import time
import getpass
import socket
import collections 
#localPath = 'T:\\user\\AIKIF\\' # '..//data//' # os.getcwd()

 
def TEST():
    """ simple test function """
    lg = Log('T:\\user\\AIKIF')
    lg.record_command('test.txt', 'hello')
    print(lg)
    sum = LogSummary(lg, 'T:\\user\\AIKIF\\log')
    sum.summarise_events()
    print(sum)
    

class Log:
    def __init__(self, fldr):
        """ pass the folder on command line """
        self.log_folder = fldr
        #print('class Log__init__(self, fldr)fldr = ' + fldr)
        self.logFileProcess = self.log_folder + os.sep + 'process.log'
        self.logFileSource  = self.log_folder + os.sep + 'source.log'
        self.logFileCommand = self.log_folder + os.sep + 'command.log'
        self.logFileResult  = self.log_folder + os.sep + 'result.log'

    def __str__(self):
        return self.log_folder
    
    def get_folder_process(self):
        return self.logFileProcess
        
    
    def _log(self, fname, txt, prg=''):
        # logs an entry to fname along with standard date and user details
        if os.sep not in fname:
            fname = self.log_folder + os.sep + fname
        delim = ','
        q = '"'
        dte = TodayAsString()
        usr = GetUserName()
        hst = GetHostName()
        #print('_log : os.path.dirname(fname) = ', os.path.dirname(fname))
        ensure_dir(os.path.dirname(fname))

        if prg == '':
            prg = 'cls_log.log' # GetModuleName() 
        logEntry = q + dte + q + delim + q + usr + q + delim + q + hst + q + delim + q + prg + q + delim + q + txt + q + delim + '\n'
        with open(fname, "a") as myfile:
            myfile.write(logEntry)

    def record_source(self, src, prg=''):
        """
        function to collect raw data from the web and hard drive
        Examples - new source file for ontologiesm, email contacts list, folder for xmas photos
        """
        self._log(self.logFileSource , force_to_string(src), prg)

    def record_process(self, process, prg=''):
        """
        log a process or program - log a physical program (.py, .bat, .exe)
        """
        self._log(self.logFileProcess, force_to_string(process), prg)

    def record_command(self, cmd, prg=''):
        """
        record the command passed - this is usually the name of the program
        being run or task being run
        """
        self._log(self.logFileCommand , force_to_string(cmd), prg)

    def record_result(self, res, prg=''):
        """
        record the output of the command. Records the result, can have 
        multiple results, so will need to work out a consistent way to aggregate this
        """
        self._log(self.logFileResult , force_to_string(res), prg)

class LogSummary:
    """
    Aggregating Logs. The goal of this class is to allow for 
    multiple usable aggregates to be automatically obtained 
    from the standard AIKIF log files.
    """
    def __init__(self, log_object, fldr):
        self.process_file = log_object.logFileProcess
        self.command_file = log_object.logFileCommand
        self.result_file = log_object.logFileResult
        self.source_file = log_object.logFileSource
        self.log_folder = fldr
        self.log_sum = fldr + os.sep + 'log_sum.csv'
    
    def __str__(self):
        txt = ''
        with open(self.log_sum, "r") as f:
            txt = f.read()
        return txt
        
        return txt
            
    def summarise_events(self):
        """
        takes the logfiles and produces an event summary matrix
            date	    command	result	process	source
            20140421	9	    40	    178	    9
            20140423	0	    0	    6	    0
            20140424	19	    1	    47	    19
            20140425	24	    0	    117	    24
            20140426	16	    0	    83	    16
            20140427	1	    0	    6	    1
            20140429	0	    0	    0	    4

        """
        print('summarising logfiles')
        all_dates = []
        d_command = self._count_by_date(self.command_file, all_dates)
        d_result  = self._count_by_date(self.result_file,  all_dates)
        d_process = self._count_by_date(self.process_file, all_dates)
        d_source  = self._count_by_date(self.source_file,  all_dates)

        with open(self.log_sum, "w") as sum_file:
            sum_file.write('date,command,result,process,source\n')
            for dte in sorted(set(all_dates)):
                sum_file.write(dte + ',')
                if dte in d_command:
                    sum_file.write(str(d_command[dte]) + ',')
                else:
                    sum_file.write('0,')
                if dte in d_result:
                    sum_file.write(str(d_result[dte]) + ',')
                else:
                    sum_file.write('0,')
                if dte in d_process:
                    sum_file.write(str(d_process[dte]) + ',')
                else:
                    sum_file.write('0,')
                if dte in d_source:
                    sum_file.write(str(d_source[dte]) + '\n')
                else:
                    sum_file.write('0\n')
                
        """
        od = collections.OrderedDict(sorted(d_command.items()))        
        with open(self.log_sum, "w") as sum_file:
            sum_file.write('date,count_command\n')
            for k,v in od.items():
                sum_file.write(k + ',' + str(v) + '\n')
                #print(k,v)
        """        
                
                
                
    def _count_by_date(self, fname, all_dates):
        """
        reads a logfile and returns a dictionary by date
        showing the count of log entries
        """
        if not os.path.isfile(fname):
            return {}
        d_log_sum = {}
        with open(fname, "r") as raw_log:
            for line in raw_log:
                cols = line.split(',')
                dte = cols[0].strip('"')[0:10].replace('-', '')
                all_dates.append(dte)
                if dte in d_log_sum:
                    d_log_sum[dte] += 1
                else:
                    d_log_sum[dte] = 1
        return d_log_sum
    
def ensure_dir(f):
    """ NOTE - not sure if this works exactly - needs a separate test """
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)
        
def List2String(l):
	res = ""
	for v in l:
		res = res + v
	return res
    
def Dict2String(d):
	res = ","
	for k, v in d: 
		res = res + k + str(v) + ','
	return res
    
def TodayAsString():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	
            
def force_to_string(unknown):
    """
    converts and unknown type to string for display purposes
    """
	result = ''
	if type(unknown) is str:
		result = unknown
	if type(unknown) is int:
		result = str(unknown)
	if type(unknown) is dict:
		result = Dict2String(unknown)
	if type(unknown) is list:
		result = List2String(unknown)
	
	return result
	 

def GetUserName():
    """ 
    return username of person logged onto host PC
    """
    
    return getpass.getuser()

def GetHostName():
    """
    returns computer name, based on socket class
    """
	return socket.gethostname()
	        
if __name__ == '__main__':     
    TEST()