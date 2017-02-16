# coding: utf-8
# load_PC_usage.py	written by Duncan Murray  19/4/2014
# reads a text file containing PC usage collected from daily agent
# and exports to the AIKIF structures (in personal folder)

import sys
import os

 
def process_all(ipFolder, op_file):	
    
    print('aggregating ', ipFolder, ' to ' , op_file)
    rawFiles = get_raw_files(ipFolder)
    for f in rawFiles:
        print('rawfile = ' + f)
        process_raw_file(f, op_file)
    
def get_raw_files(ipFolder):
    fl = []
    print(ipFolder)
    for root, _, files in os.walk(ipFolder):
        for basename in files:
            filename = os.path.join(root, basename)
            if basename[0:6] == 'diary_':
                fl.append(filename)
    return fl


def process_raw_file(f, op_file):
    print ('Processing: ', f)
    usage = []
    with open(op_file,'a') as op:
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
    
