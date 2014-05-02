# load_PC_usage.py	written by Duncan Murray  19/4/2014
# reads a text file containing PC usage collected from daily agent
# and exports to the AIKIF structures (in personal folder)

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
	ipFolder = sys.argv[1] 
	opFolder = sys.argv[2] 
except:
	print ('load_PC_usage.py - processes logged PC usage data to diary files')
	print('Usage:')
	print('  load_PC_usage.py [input_folder] [output_folder]')
	exit(1)
	
	
def main():	
	#ipFile = ipFolder + '\\pc_usage_' + GetPCName() + '_' + GetUser() + '.txt'
	#opFile = opFolder + '\\diary.csv'
	print('aggregating ', ipFolder, ' to ' , opFolder)
	rawFiles = GetRawFiles(ipFolder)
	for f in rawFiles:
		processRawFile(f, opFolder)
	
def GetRawFiles(ipFolder):
	fl = []
	#print(ipFolder)
	for root, dirs, files in os.walk(ipFolder):
		#print('root = ', root)
		#print('dirs = ', dirs)
		#print('files= ', files)
		for basename in files:
			filename = os.path.join(root, basename)
			if basename[0:9] == 'pc_usage_':
				fl.append(filename)
		#print(filename)
		#print(basename[0:9])
	
	return fl


def processRawFile(f, opFolder):
	print ('Processing: ', f)
	opFile = opFolder + '\\diary.csv'
	curText = ''
	oldText = ''
	usage = []
	with open(opFile,'a') as op:
		with open(f, 'r') as ip:
			for line in ip:
				print('line=====', line)
				cols = line.split(',')
				dte = cols[0].split(' ')[0]
				tme = cols[0].split(' ')[1]
				amt = cols[1]
				det = cols[2]
				print('\ndte = ' , dte, '\ntme = ', tme, '\namt = ',amt,'\ndet = ', det)
				if oldText == curText:
					print('same')
				usage.append(det)

		uniqueUsage = set(usage)
		
		for res in uniqueUsage:
			# sum amt for usage
			# TODO
		
		
			op.write(res)
	
if __name__ == '__main__':
    main()	
	
