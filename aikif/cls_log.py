# cls_log.py    written by Duncan Murray 13/9/2014

import os
import sys
import time
import getpass
import socket
 
#localPath = 'T:\\user\\AIKIF\\' # '..//data//' # os.getcwd()

 
def TEST():
    """ simple test function """
    lg = Log('T:\\user\\AIKIF')
    lg.record_command('test.txt', 'hello')
    print(lg)
    sum = LogSummary(lg, 'T:\\user\\AIKIF')
    print(sum)
    

class Log:
    def __init__(self, fldr):
        """ pass the folder on command line """
        self.log_folder = fldr
        self.logFileProcess = self.log_folder + os.sep + 'log' + os.sep + 'process.log'
        self.logFileSource = self.log_folder + os.sep + 'log' + os.sep + 'source.log'
        self.logFileCommand = self.log_folder + os.sep + 'log' + os.sep + 'command.log'
        self.logFileResult = self.log_folder + os.sep + 'log' + os.sep + 'result.log'

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
        ensure_dir(os.path.dirname(fname))

        if prg == '':
            prg = 'cls_log.log' # GetModuleName() 
        logEntry = q + dte + q + delim + q + usr + q + delim + q + hst + q + delim + q + prg + q + delim + q + txt + q + delim + '\n'
        with open(fname, "a") as myfile:
            myfile.write(logEntry)

    # -----------------------------------------
    # --   Logging Functions 
    # -----------------------------------------
    def record_data_source(self, src, prg=''):
        # function to collect raw data from the web and hard drive[ currently using documents on disk instead of web ]
        #print(' source  =', src)
        self._log(self.logFileSource , force_to_string(src), prg)

    def record_process(self, process, prg=''):
        # log a process or program
        #print(' process = ', process)
        self._log(self.logFileProcess, force_to_string(process), prg)

    def record_command(self, cmd, prg=''):
        # record the command passed
        #print(' command = ', cmd)
        self._log(self.logFileCommand , force_to_string(cmd), prg)

    def record_result(self, res, prg=''):
        # record the output of the command
        #print('   result    = ', res)
        self._log(self.logFileResult , force_to_string(res), prg)

class LogSummary:
    """
    Aggregating Logs 
    """
    def __init__(self, log_object, fldr):
        self.process_file = log_object.logFileProcess
        self.command_file = log_object.logFileCommand
        self.result_file = log_object.logFileResult
        self.source_file = log_object.logFileSource
        print('process_file:' + self.process_file)
    
    def __str__(self):
        txt = '---- LogSummary ---\n'
        txt += 'self.process_file = ' + self.process_file + '\n'
        txt += 'self.command_file = ' + self.command_file + '\n'
        txt += 'self.result_file  = ' + self.result_file + '\n'
        txt += 'self.source_file  = ' + self.source_file + '\n'
        return txt
            
    def summarise_events(self, opFile):
        """
        takes the logfiles and produces an event summary matrix
        """
        print('summarising logFileCommand - ' + self.logFileCommand)
        
def ensure_dir(f):
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
    return getpass.getuser()

def GetHostName():
	return socket.gethostname()
	        
    
TEST()