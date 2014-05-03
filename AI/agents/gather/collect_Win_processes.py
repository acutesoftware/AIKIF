# coding: utf-8
# win_processes.py	written by Duncan Murray 3/5/2014




"""
Extracts a list of running processes from Windows PC using 2 possible methods
1 = shell to BAT file to call wmic and parse results (more info but clumsy)
2 = using ctypes to get the description in Python (gets title)


T:\\user\\dev\\src\\python\\lifepim>wmic process os list /?

Property list operations.
USAGE:

LIST [<list format>] [<list switches>]

The following LIST formats are available:

BRIEF                     - ThreadCount, HandleCount, Name, Priority, ProcessId,
 WorkingSetSize
FULL                      - CommandLine, CSName, Description, ExecutablePath, Ex
ecutionState, Handle, HandleCount, InstallDate, KernelModeTime, MaximumWorkingSe
tSize, MinimumWorkingSetSize, Name, OSName, OtherOperationCount, OtherTransferCo
unt, PageFaults, PageFileUsage, ParentProcessId, PeakPageFileUsage, PeakVirtualS
ize, PeakWorkingSetSize, Priority, PrivatePageCount, ProcessId, QuotaNonPagedPoo
lUsage, QuotaPagedPoolUsage, QuotaPeakNonPagedPoolUsage, QuotaPeakPagedPoolUsage
, ReadOperationCount, ReadTransferCount, SessionId, Status, TerminationDate, Thr
eadCount, UserModeTime, VirtualSize, WindowsVersion, WorkingSetSize, WriteOperat
ionCount, WriteTransferCount
INSTANCE                  - __PATH
IO                        - Name, ProcessId, ReadOperationCount, ReadTransferCou
nt, WriteOperationCount, WriteTransferCount
MEMORY                    - Handle, MaximumWorkingSetSize, MinimumWorkingSetSiz
, Name, PageFaults, PageFileUsage, PeakPageFileUsage, PeakVirtualSize, PeakWork
ngSetSize, PrivatePageCount, QuotaNonPagedPoolUsage, QuotaPagedPoolUsage, Quota
eakNonPagedPoolUsage, QuotaPeakPagedPoolUsage, VirtualSize, WorkingSetSize
STATISTICS                - HandleCount, Name, KernelModeTime, MaximumWorkingSe
Size, MinimumWorkingSetSize, OtherOperationCount, OtherTransferCount, PageFault
, PageFileUsage, PeakPageFileUsage, PeakVirtualSize, PeakWorkingSetSize, Privat
PageCount, ProcessId, QuotaNonPagedPoolUsage, QuotaPagedPoolUsage, QuotaPeakNon
agedPoolUsage, QuotaPeakPagedPoolUsage, ReadOperationCount, ReadTransferCount,
hreadCount, UserModeTime, VirtualSize, WorkingSetSize, WriteOperationCount, Wri
eTransferCount
STATUS                    - Status, Name, ProcessId
SYSTEM                    - __CLASS, __DERIVATION, __DYNASTY, __GENUS, __NAMESP
CE, __PATH, __PROPERTY_COUNT, __RELPATH, __SERVER, __SUPERCLASS

The following LIST switches are available:

/TRANSLATE:<table name>      - Translate output via values from <table name>.
/EVERY:<interval> [/REPEAT:<repeat count>] - Returns value every (X interval) s
conds, If /REPEAT specified the command is executed <repeat count> times.
/FORMAT:<format specifier>   - Keyword/XSL filename to process the XML results.

----

catch processes in OS then pipe to text file, this way you can have a function for
linux as well using ps -ef > processes.txt

WINDOWS
wmic  process get description,executablepath,ThreadCount,WriteOperationCount,UserModeTime,Name, OSName,InstallDate

GET_PROCESSES.BAT
==================================
REM GET_WIN_PROCESSES.BAT
wmic  process get description,WorkingSetSize,PrivatePageCount,ReadOperationCount, WriteOperationCount,UserModeTime,executablepath > processes.txt
==================================

Description                   ExecutablePath                                                                                               PrivatePageCount  ReadOperationCount  UserModeTime  WorkingSetSize  WriteOperationCount  
System Idle Process                                                                                                                        0                 0                   0             24576           0                    
System                                                                                                                                     450560            277169              0             16478208        213311               
smss.exe                                                                                                                                   589824            487                 0             1273856         5                    
csrss.exe                     C:\\windows\\system32\\csrss.exe                                                                                3637248           8665                64896416      5787648         0                    
wininit.exe                   C:\\windows\\system32\\wininit.exe                                                                              1720320           621                 0             4857856         0                    
csrss.exe                     C:\\windows\\system32\\csrss.exe                                                                                3715072           4814326             44304284      34344960        0                    



"""

def main():
	lst = GetWindowsProcesses_method2()
	for dicts in lst:
		for d in dicts:
			print (d['Description']   + ' = ' + str(d['UserModeTime'])) #+ d['ExecutablePath'])
	print('Found ' + str(len(lst)) + ' processes')

def GetWindowsProcesses_method2():
	"""  Gets list of windows processes using BAT file
	"""
	import time, os, sys
	batFile = 'GETWINPROCESS.BAT'
	print('creating BAT file - ' + batFile)
	with open(batFile,'w') as f:
		f.write('wmic  process get description,WorkingSetSize,PrivatePageCount,ReadOperationCount, WriteOperationCount,UserModeTime,executablepath > processes.txt\n')
	time.sleep(1)
		
	print('running BAT file to collect processes')
	from subprocess import call
	try:
		retcode = call(batFile, shell=True) 
		time.sleep(1)
	except OSError as e:
		'ERROR - could not get list of processes'
		return []

	print('reading Processes')
	numLines = 0
	processes = []
	with open('processes.txt','r', encoding="utf-16") as f:	  # file appears double spaced if you omit UTF-16
		lines = f.readlines()
		for line in lines:
			processes.append([SplitWinProcessLine(line)])
	return processes
	
def SplitWinProcessLine(txt):
	# Description  ExecutablePath  PrivatePageCount  ReadOperationCount  UserModeTime  WorkingSetSize  WriteOperationCount 
	res = {}
	res['Description'] = txt[0:30].strip()
	res['ExecutablePath'] = txt[30:138].strip()
	try:
		res['PrivatePageCount'] = int(txt[139:157].strip())
		res['ReadOperationCount'] = int(txt[157:177].strip())
		res['UserModeTime'] = int(txt[177:191].strip())
		res['WorkingSetSize'] = int(txt[191:207].strip())
		res['WriteOperationCount'] = int(txt[207:228].strip())
	except:
		res['PrivatePageCount'] = -1
		res['ReadOperationCount'] = -1
		res['UserModeTime'] = -1
		res['WorkingSetSize'] = -1
		res['WriteOperationCount'] = -1
	
	
		print('problem parsing numbers from ' , txt)
	return res
	
def GetWindowsProcesses_method1():
	"""  Gets list of windows processes using Python ctypes (only returns description)
	"""
	import ctypes
	 
	EnumWindows = ctypes.windll.user32.EnumWindows
	EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
	GetWindowText = ctypes.windll.user32.GetWindowTextW
	GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
	IsWindowVisible = ctypes.windll.user32.IsWindowVisible
	 
	titles = []
	def foreach_window(hwnd, lParam):
		if IsWindowVisible(hwnd):
			length = GetWindowTextLength(hwnd)
			buff = ctypes.create_unicode_buffer(length + 1)
			print(buff)
			GetWindowText(hwnd, buff, length + 1)
			titles.append(buff.value)
		return True
	EnumWindows(EnumWindowsProc(foreach_window), 0)
	 
	for t in titles:
		print(t)
		
	return(titles)

#if __name__ == '__main__':
#    main()	
	
