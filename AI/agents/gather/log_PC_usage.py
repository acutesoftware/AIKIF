# log_usage.py  written by Duncan Murray 13/1/2014

from win32gui import GetWindowText, GetForegroundWindow
import sys
import os
import time


def GetUser():
	try:
		import getpass
		usr = getpass.getuser()
	except:
		usr = 'username'
	return usr

def GetPCName():
	try:
		import socket
		pcname = socket.gethostname()
	except:
		pcname = 'computer'
	return pcname

try:
	fname = sys.argv[1] + '\\pc_usage_' + GetPCName() + '_' + GetUser() + '.txt'
except:
	fname = os.getcwd() + GetUser() + '\\pc_usage_' + GetPCName() + '_' + GetUser() + '.txt'



def main():
	lstRaw = []
	prevText = ''
	startTime = TodayAsString()
	tot_seconds = 1
	try:
		while True:
			txt = GetWindowText(GetForegroundWindow())
			#print(txt)
			#AppendToFile(fname, TodayAsString() + ' ' + txt + '\n')
			if txt == prevText:
				tot_seconds = tot_seconds + 1
			else:
				lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
				prevText = txt
				tot_seconds = 1
				startTime = TodayAsString()
			time.sleep(1)
			if TodayAsString()[-3:] == ':00':
				lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)
				#print('Recording data')
				tot_seconds = 1
				startTime = TodayAsString()
				record(lstRaw)
				lstRaw = []

	except KeyboardInterrupt:	
		print("logging halted")
		lstRaw.append(startTime + ',' + format(tot_seconds, "03d") + ',' + txt)   # save the latest record
		record(lstRaw)

	
def TodayAsString():
	return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def record(lst):
	with open(fname, "a") as f:
		for txt in lst:
			f.write(txt + '\n')
	tot_seconds = 1
		
if __name__ == '__main__':
	main()
	
	
