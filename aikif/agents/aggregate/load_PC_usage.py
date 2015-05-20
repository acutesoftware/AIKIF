# coding: utf-8
# load_PC_usage.py	written by Duncan Murray  19/4/2014
# reads a text file containing PC usage collected from daily agent
# and exports to the AIKIF structures (in personal folder)

import sys
import os

def GetUser():
    try:
        import getpass
        usr = getpass.getuser()
    except Exception:
        usr = 'username'
    return usr

def GetPCName():
    try:
        import socket
        pcname = socket.gethostname()
    except Exception:
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
        print('rawfile = ' + f)
        processRawFile(f, opFolder)
    
def GetRawFiles(ipFolder):
    fl = []
    print(ipFolder)
    for root, dirs, files in os.walk(ipFolder):
        print('root = ', root)
        print('dirs = ', dirs)
        print('files= ', files)
        for basename in files:
            filename = os.path.join(root, basename)
            if basename[0:6] == 'diary_':
                fl.append(filename)
        #print(filename)
        #print(basename[0:9])
    print(fl)
    return fl


def processRawFile(f, opFolder):
    print ('Processing: ', f)
    usage = []
    with open(opFolder + os.sep + 'diary.csv','a') as op:
        with open(f, 'r') as ip:
            for line in ip:
                det = ''
                #print('line=====', line)
                cols = line.split(',')
                dte = cols[0]
                tme = cols[1]
                amt = cols[2]
                for pos in range(3, len(cols)):
                    det += cols[pos]   # cols[2]
                #print('\ndte = ' , dte, '\ntme = ', tme, '\namt = ',amt,'\ndet = ', det)
                usage.append([dte,tme,amt,det])
        for res in usage:
            op.write(chr(31).join(res))
    
if __name__ == '__main__':
    main()	
    
