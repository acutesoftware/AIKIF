# cls_filelist.py
import os
import shutil
import csv
import glob
import fnmatch
import time
from datetime import datetime

def TEST():
    """ simple test used for development.
    TODO - move to unittest 
    TODO - check that folder is NOT a filename
    TODO - make sure folder passed is a LIST not a string
    TODO - make sure xtn passed is a LIST not a string
    TODO - make sure excluded is passed NOT just the output file
    """
    print("Running self test for cls_filelist")
    fldr = os.path.dirname(os.path.abspath(__file__))
    
    fl_grp = FileListGroup("AIKIF lib files", fldr, "E:\\backup")
    print(fl_grp)
    
    fl = FileList([fldr], ['*.py'], [], "sample_filelist.csv")
    for f in fl.filelist:
        print(f)
    print("Done.")
    
class FileListGroup(object):
    """ 
    not sure about the point of this class - might be simpler 
    to just get cls_filelist to do all the work. Will leave it in
    in case I remember the original idea
    """
    def __init__(self, name, src_folder, dest_folder):
        self.name = name
        self.filelist = []              # contains a list of the filelist class instances
        self.src_folder = src_folder
        self.dest_folder = dest_folder
     
    def __str__(self):
        """ display the filelist group details """
        txt =  'FileListGroup : ' + self.name + '\n'
        txt += 'src_folder    : ' + self.src_folder + '\n'
        txt += 'dest_folder   : ' + self.dest_folder + '\n'
        return txt
        
    def backup(self):
        """
        copies all files from the src folder to the dest folder
        """
        print("TODO backing up " + self.name)
        
    def restore(self):
        """
        restores all files from the dest folder to the src folder
        """
        print("TODO (be careful with this) restoring " + self.name)
        
    def backup_incremental(self):
        """
        copies CHANGED files from the src folder to the dest folder
        This is the primary mode of AutoBackup
        """
        print("TODO backing up changed files only " + self.name)

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
            
    def get_file_list(self):
        """
        uses self parameters if no parameters passed - TODO - add test for this!!!!
        """
        self.get_file_list(self.paths, self.xtn, self.excluded)
        
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
        self.fl_metadata = []
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
                                self.filelist.append(filename)
                                self.add_file_metadata(filename)    # not sure why there is a 2nd list, but there is.
        if VERBOSE:
            print("Found ", numFiles, " files")
        return self.filelist

    def add_file_metadata(self, fname):
        file_dict = {}
        file_dict["fullfilename"] = fname
        
        self.fl_metadata.append(file_dict)
        
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

		
if __name__ == '__main__':
	TEST()
	
            