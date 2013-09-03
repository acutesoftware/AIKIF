# AI.py   written by Duncan Murray 28/7/2013  (C) Acute Software
# This is the main script that uses the framework of tables to capture the flow 
# of information ready for an AI to utilise it.
# AIKIF = Artificial Intelligence Knowledge Information Framework

import os
import sys
import csv
sys.path.append('C://user//dev//src//python//_AS_LIB')
import as_util_data as dat
import AIKIF_utils as aikif
localPath = "C://user//dev//src//python//AI//"

def GetCommand():
    allCommands = dat.ReadFileToList("commands.csv", 2)
    
    #for com in allCommands:
    #    if com.split(",")
    #   currentCommand = allCommands[0].rsplit())
    currentCommand = "READ"
    currentCommand = "PROCESS"
    currentCommand = "PLAY"
    
    print("   Current Operator Commands = ", currentCommand)
    return currentCommand
    
def CollectData():
    # function to collect raw data from the web and hard drive[ currently using documents on disk instead of web ]
    print("   Collecting Data")

def ProcessData():
    # function to process raw data using Bias tables to get a comprehension of the information
    print("   Processing Data")

def Play():
    # function to process raw data using Bias tables to get a comprehension of the information
    print("   Free form play - learn what you want")

      
#------------------------------
#  Main Program 
#------------------------------
print("Hello - Welcome to AI.py")
try:
    AIKIF_FileList = aikif.build_AIKIF_structure()
except:    
    sys.exit("Error - cant load data structures")

numIterations = 0
while(numIterations < 1):
    currentCommand = GetCommand()
    if currentCommand == "READ":
        CollectData()
    elif currentCommand == "PROCESS":    
        ProcessData()
    elif currentCommand == "PLAY":    
        Play()
        
    numIterations = numIterations + 1

print("Goodbye") 