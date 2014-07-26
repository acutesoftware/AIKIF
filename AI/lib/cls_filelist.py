# cls_filelist.py
import os
import shutil
import csv
import glob
import fnmatch
import time
from datetime import datetime

class FileList(object):
    def __init__(self, paths, xtn, excluded, output_file_name = 'my_files.csv'):
        self.output_file_name = output_file_name
        self.filelist = []
        self.paths = paths
        self.xtn = xtn
        self.excluded = excluded
        
        self.get_file_list(self.paths, self.xtn, self.excluded)
    
    def get_list(self):
        return self.filelist
            
    def get_file_list(self, lstPaths, lstXtn, lstExcluded, VERBOSE = False):
        """
        builds a list of files and returns as a list 
        originally from lib_file.py in aspytk
        """
        if VERBOSE:
            print("Generating list of Files...")
            print("Paths = ", lstPaths)
            print("Xtns  = ", lstXtn)
            print("exclude = ", lstExcluded)
        numFiles = 0    
        self.filelist = []
        for rootPath in lstPaths:
            if VERBOSE:
                print(rootPath)
            for root, dirs, files in os.walk(rootPath):
                for basename in files:
                    for xtn in lstXtn:
                        if fnmatch.fnmatch(basename, xtn):
                            filename = os.path.join(root, basename)
                            includeThisFile = "Y"
                            if len(lstExcluded) > 0:
                                for exclude in lstExcluded:
                                    if filename.find(exclude) != -1:
                                        includeThisFile = "N"
                            if includeThisFile == "Y":
                                if VERBOSE:
                                    print(os.path.basename(filename), '\t', os.path.getsize(filename))
                                numFiles = numFiles + 1
                                self.filelist.append( filename)
        if VERBOSE:
            print("Found ", numFiles, " files")
        return self.filelist

        
    def GetDateAsString(self, t):
        res = ''
        try:
            res = str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
        except:
            pass
        return res     
        
    def TodayAsString(self):	
        """
        returns current date and time like oracle
    #	return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        
        
    def save_filelist(self, opFile, opFormat, delim=',', qu='"'):
        """
        uses a List of files and collects meta data on them and saves 
        to an text file as a list or with metadata depending on opFormat.
        """
        with open(opFile,'w') as fout:
            fout.write("fullFilename" + delim)
            for colHeading in opFormat:
                fout.write(colHeading + delim)
            fout.write('\n')    
            for f in self.filelist:
                line = qu + f + qu + delim
                for fld in opFormat:
                    if fld == "name":
                        line = line + qu + os.path.basename(f) + qu + delim
                    if fld == "date":
                        line = line + qu + self.GetDateAsString(os.path.getmtime(f)) + qu + delim 
                    if fld == "size":
                        line = line + qu + str(os.path.getsize(f)) + qu + delim
                    if fld == "path":
                        line = line + qu + os.path.dirname(f) + qu + delim
                        
                fout.write (line + '\n')
            #print ("Finished saving " , opFile)
