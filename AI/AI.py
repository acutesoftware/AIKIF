# AI.py   written by Duncan Murray 28/7/2013  (C) Acute Software
# This is the main script that uses the framework of tables to capture the flow 
# of information ready for an AI to utilise it.
# AIKIF = Artificial Intelligence Knowledge Information Framework

import os
import sys
import csv
sys.path.append('..//..//_AS_LIB')
import as_util_data as dat
import AIKIF_utils as aikif
localPath = os.getcwd()


def BlackBoxAI(command, sourceInfo):
    # call to your application
    result = []
    print('running AI task ...')
    x = 0
    #for c in command:
    for i in sourceInfo:
        x = x + int(i)
    # -----------------------------
    # insert link to real code here
    # -----------------------------
    result.append('answer=' + str(x))
    result.append('status=Success')
    return result
    
#------------------------------
#  Main Program 
#------------------------------
print("Sample code to run an AI task using the AIKIF framework")
#try:
AIKIF_FileList = aikif.build_AIKIF_structure()
#aikif.printFileList(AIKIF_FileList)
aikif.showColumnStructures(AIKIF_FileList)
#aikif.debugPrintFileStructures(AIKIF_FileList)

aikif.LogProcess('sample task - BlackBoxAI')

# define source data and commands
source = []
command = []
command.append( 'Sum all variables')
source.append('2')
source.append('5')
aikif.LogCommand(command)
aikif.LogDataSource(source)

# call your AI task 
result = BlackBoxAI(command, source)        

# record the result
aikif.LogResult(result)
    
#except:    
#    sys.exit("Error - cant load data structures")

print("Done") 