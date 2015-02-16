# cls_log.py    written by Duncan Murray 13/9/2014

import os
import sys
import time
import getpass
import socket
import collections 
import config as cfg
import random

def TEST():
    """ simple test function """
    lg = Log(cfg.fldrs['localPath'])
    lg.record_command('test.txt', 'hello')
    print(lg)
    sum = LogSummary(lg, cfg.fldrs['log_folder'])
    sum.summarise_events()
    print(sum)
    

class Log:
    def __init__(self, fldr):
        """ pass the folder on command line """
        self.log_folder = fldr
        self.logFileProcess = self.log_folder + os.sep + 'process.log'
        self.logFileSource  = self.log_folder + os.sep + 'source.log'
        self.logFileCommand = self.log_folder + os.sep + 'command.log'
        self.logFileResult  = self.log_folder + os.sep + 'result.log'
        ensure_dir(self.logFileCommand)  # need to pass file not the folder for this to work
        self.session_id = self.get_session_id()
        
    def __str__(self):
        return self.log_folder
    
    def get_folder_process(self):
        return self.logFileProcess
     
    def get_session_id(self):
        """
        get a unique id (shortish string) to allow simple aggregation
        of log records from multiple sources. This id is used for the 
        life of the running program to allow extraction from all logs.
        WARING - this can give duplicate sessions when 2 apps hit it 
        at the same time.
        """
        max_session = '0'
        try:
            with open(self.log_folder + os.sep + '_sessions.txt', 'r') as f:
                for line in f:
                    txt = f.readline()
                    if txt.strip('\n') != '':
                        max_session = txt
        except:
            max_session = '1'
        
        this_session = str(int(max_session) + random.randint(9,100)).zfill(9) # not a great way to ensure uniqueness - TODO FIX  
        with open(self.log_folder + os.sep + '_sessions.txt', 'a') as f2:
            f2.write(this_session + '\n')
        return this_session
        
        
        
    def estimate_complexity(self, x,y,z,n):
        """ calculates a rough guess of runtime based on product of parameters """
        num_calculations = x * y * z * n
        run_time = num_calculations / 100000  # a 2014 PC does about 100k calcs in a second (guess based on prior logs)
        return self.show_time_as_short_string(run_time) 

            
    def show_time_as_short_string(self, seconds):
        """ 
        converts seconds to a string in terms of 
        seconds -> years to show complexity of algorithm
        """
        if seconds < 60:
            return str(seconds) + ' seconds'
        elif seconds < 3600:
            return str(round(seconds/60, 1)) + ' minutes'
        elif seconds < 3600*24:
            return str(round(seconds/(60*24), 1)) + ' hours'
        elif seconds < 3600*24*365:
            return str(round(seconds/(3600*24), 1)) + ' days'
        else:
            print('WARNING - this will take ' + str(seconds/(60*24*365)) + ' YEARS to run' )
            return str(round(seconds/(60*24*365), 1)) + ' years'

    def _log(self, fname, txt, prg=''):
        """
        logs an entry to fname along with standard date and user details
        """
        if os.sep not in fname:
            fname = self.log_folder + os.sep + fname
        delim = ','
        q = '"'
        dte = TodayAsString()
        usr = GetUserName()
        hst = GetHostName()
        id = self.session_id
 
        if prg == '':
            prg = 'cls_log.log' 
        logEntry = q + dte + q + delim + q + id + q + delim + q + usr + q + delim + q + hst + q + delim + q + prg + q + delim + q + txt + q + delim + '\n'
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