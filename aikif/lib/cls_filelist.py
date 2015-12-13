#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_filelist.py
import os
#import shutil
#import csv
#import glob
import fnmatch
import time
from datetime import datetime
import aikif.cls_log as mod_log

class FileListGroup(object):
    """ 
    not sure about the point of this class - might be simpler 
    to just get cls_filelist to do all the work. Will leave it in
    in case I remember the original idea
    """
    def __init__(self, name, src_folder, dest_folder):
        self.name = name
        self.filelist = []              # contains a list of the filelist class instances
        self.dest_folder = dest_folder

    def __str__(self):
        """ display the filelist group details """
        txt =  'FileListGroup : ' + self.name + '\n'
        txt += 'dest_folder   : ' + self.dest_folder + '\n'
        return txt

    def backup(self):
        """
        copies all files from the src folder to the dest folder
        """
        for fl in self.filelist:
            print("TODO backing up filelist " + str(fl))


    def backup_incremental(self):
        """
        copies CHANGED files from the src folder to the dest folder
        This is the primary mode of AutoBackup
        """
        print("TODO backing up changed files only " + self.name)

class FileList(object):
    def __init__(self, paths, xtn, excluded, output_file_name = 'my_files.csv'):
        self.output_file_name = output_file_name
        self.filelist = []       # list of full filenames
        self.fl_metadata = []    # dictionary of all file metadata
        self.fl_dirty_files = [] # list of fullfilenames needing to be backed up
        self.failed_backups = [] # list of files that failed to backup
        self.paths = paths
        self.xtn = xtn
        self.excluded = excluded
        self.get_file_list(self.paths, self.xtn, self.excluded)
    
    def get_list(self):
        return self.filelist

    def get_dirty_filelist(self):
        return self.fl_dirty_files

    def get_metadata(self):
        return self.fl_metadata
    
    def backup(self, dest_root_folder):
        """
        backup all files for the filelist into a destination
        root folder
        """
        for fldr in self.filelist:
            print('TODO - backing up ' + fldr)
        

    
    def get_failed_backups(self):
        return self.failed_backups

    def add_failed_file(self, fname):
        """ 
        this file failed to backup, so log it for future retry 
        """
        self.failed_backups.append(fname)
    
    
    def check_files_needing_synch(self, dest_root_folder, base_path_ignore, date_accuracy = 'hour'):
        """ 
        checks the metadata in the list of source files
        against the dest_folder (building path) and flags a
        data_dirty column in the metadata if the file needs
        backing up.
        """
        for f in self.fl_metadata:
            if base_path_ignore == '':
                dest_folder =  os.path.join(dest_root_folder, os.path.dirname(f["fullfilename"]))
                #print('dest_root_folder = ', dest_root_folder,  ', dest_folder = ', dest_folder )
            else:
                dest_folder =  os.path.join(dest_root_folder, os.path.dirname(f["fullfilename"])[len(base_path_ignore):])
            dest_file = dest_folder + os.sep + f["name"]
            # works - find correct source file and dest file
            #print("Checking file - " + f["fullfilename"])
            #print("against dest_file = " + dest_file)
            if self.is_file_dirty(f, dest_file, date_accuracy):
                self.fl_dirty_files.append(f["fullfilename"])
                
    
    def is_file_dirty(self, src_file_dict, dest_file, date_accuracy):
        """ 
        does various tests based on config options (eg simple
        date modified, all files, check CRC hash
        """
        try:
            if os.path.isfile(dest_file) == False:
                return True  # no backup exists, so needs backing up
        except IOError:
            pass

        try:
            if src_file_dict["size"] != os.path.getsize(dest_file):
                return True  # file size has changed, so backup
        except IOError:
            pass
        
        try:
            if self.compare_file_date(src_file_dict["date"], dest_file, date_accuracy) == False:
                return True  # file date is different so MAYBE backup
        except IOError:
            pass
         
        try:
            if self.get_file_hash(src_file_dict["fullfilename"]) != self.get_file_hash(dest_file):
                return True   # file contents changed so backup (e.g. fixed file sizes)
        except IOError:
            pass
        
        # all tests pass, so assume file is ok and doesn't need syncing    
        
        return False
    
    def get_file_hash(self, fname):
        """ returns a file hash of the file """
        #print('WARNING - get_file_hash not implemented - no hash for ' + fname)
        return True  # not implemented obviously - should used saved results anyway
    
    def compare_file_date(self, dte, dest_file, date_accuracy):
        """Checks to see if date of file is the same   """
        if os.path.exists(dest_file):
            dest_date = self.GetDateAsString(os.path.getmtime(dest_file))
        else:
            return False
        
        date_size = 17
        if date_accuracy == 'day':
            date_size = 11
        if date_accuracy == 'hour':
            date_size = 13
        if date_accuracy == 'min':
            date_size = 15
            
        # now trunc both date strings by same amount
        #print("dte before = " + dte)
        dest_date = dest_date[:date_size]
        dte  = dte[:date_size]
        #print("dte after  = " + dte)
        # TODO = take into account time differences on other servers
        # do this once at calling function by creating a file and 
        # checking timestamp against sysdate and then getting an offset
        # (usually .5 to 1 hour difference max)
        
        if dte != dest_date:
            return False
        return True
        
    def get_file_list(self, lstPaths, lstXtn, lstExcluded, VERBOSE = False):
        """
        builds a list of files and returns as a list 
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
                if VERBOSE:
                    print(dirs)
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
                                numFiles = numFiles + 1
                                self.filelist.append(filename)
                                self.add_file_metadata(filename)    # not sure why there is a 2nd list, but there is.

        if VERBOSE:
            print("Found ", numFiles, " files")
        return self.filelist

    def add_file_metadata(self, fname):
        """
        collects the files metadata - note that this will fail
        with strange errors if network connection drops out to
        shared folder, but it is better to stop the program 
        rather than do a try except otherwise you will get an 
        incomplete set of files.
        """
        
        file_dict = {}
        try:
            file_dict["fullfilename"] = fname
        except IOError:
            file_dict["fullfilename"] = 'Unknown filename'  # should never get here
        
        try:        
            file_dict["name"] = os.path.basename(fname)
        except IOError:
            file_dict["name"] = 'Unknown basename'
            
        try:        
            file_dict["date"] = self.GetDateAsString(fname)
        except IOError:
            file_dict["date"] = 'Unknown date'
            
        try:        
            file_dict["size"] = os.path.getsize(fname)
        except IOError:
            file_dict["size"] = 'Unknown size'
            
        try:        
            file_dict["path"] = os.path.dirname(fname)
        except IOError:
            file_dict["path"] = 'Unknown path'
            
        self.fl_metadata.append(file_dict)

    def print_file_details_in_line(self, fname, col_headers):
        """ makes a nice display of filename for printing based on columns passed 
               print('{:<30}'.format(f["name"]), '{:,}'.format(f["size"]))
        """
        line = ''
        for fld in col_headers:
            if fld == "fullfilename":
                line = line + fname
            if fld == "name":
                line = line + '{:<30}'.format(os.path.basename(fname)) + ' '
            if fld == "date":
                line = line + self.GetDateAsString(fname) + ' '
            if fld == "size":
                line = line + '{:,}'.format(os.path.getsize(fname)) + ' ' 
            if fld == "path":
                line = line + os.path.dirname(fname) + ' '
        #line += '\n'
        return line
        
    def print_file_details_as_csv(self, fname, col_headers):
        """ saves as csv format """
        line = ''
        qu = '"'
        d = ','
        for fld in col_headers:
            if fld == "fullfilename":
                line = line + qu + fname + qu + d
            if fld == "name":
                line = line + qu + os.path.basename(fname) + qu + d
            if fld == "date":
                line = line + qu + self.GetDateAsString(fname) + qu + d
            if fld == "size":
                line = line + qu + self.get_size_as_string(fname) + qu + d
            if fld == "path":
                try:
                    line = line + qu + os.path.dirname(fname) + qu + d 
                except IOError:
                    line = line + qu + 'ERROR_PATH' + qu + d

        return line
    
    def get_size_as_string(self, fname):
        res = ''
        try:
            res = str(os.path.getsize(fname))
        except Exception:
            res = 'Unknown size'
        return res

    def GetDateAsString(self, fname):
        res = ''  
        try:
            t = os.path.getmtime(fname)
            res = str(datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S"))
        except Exception:
            res = 'Unknown Date'
        return res     
        
    def TodayAsString(self):	
        """
        returns current date and time like oracle
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
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
                try:
                    for fld in opFormat:
                        if fld == "name":
                            line = line + qu + os.path.basename(f) + qu + delim
                        if fld == "date":
                            line = line + qu + self.GetDateAsString(f) + qu + delim 
                        if fld == "size":
                            line = line + qu + str(os.path.getsize(f)) + qu + delim
                        if fld == "path":
                            line = line + qu + os.path.dirname(f) + qu + delim
                except IOError:
                    line += '\n'   # no metadata
                try:
                    fout.write (str(line.encode('ascii', 'ignore').decode('utf-8')))
                    fout.write ('\n')
                except IOError:
                    #print("Cant print line - cls_filelist line 304")
                    pass
    
    def save_file_usage(self, fldr, nme):
        """ 
        saves a record of used files for infolink applications
        
        print("Saving File Usage to " + fldr)
        file_copied = fldr + 'copied_' + nme + '.txt'
        file_failed = fldr + 'failed_' + nme + '.txt'
        file_data = fldr + 'filelist_' + nme + '.csv'
        file_usage = fldr + 'file_usage.csv'
        
        if os.path.isfile(file_copied):
            os.remove(file_copied)
        with open(file_copied, 'w', encoding='utf-8') as f:
            f.write("# Backed up on " + self.TodayAsString() + '\n')
            for fname in self.get_dirty_filelist():
                try:
                    f.write(fname + '\n')
                except IOError:
                    print("FAILED LOGGING FILENAME to file_copied")
                
        if os.path.isfile(file_failed):
            os.remove(file_failed)
        with open(file_failed, 'w', encoding='utf-8') as f:
            f.write("# Files Failed to backup on " + self.TodayAsString() + '\n')
            for fname in self.get_failed_backups():
                try:
                    f.write(fname + '\n')
                except IOError:
                    print("FAILED LOGGING FILENAME to file_failed")
                
        if os.path.isfile(file_data):
            os.remove(file_data)
        with open(file_data, 'w', encoding='utf-8') as f:
            f.write("# FileList refreshed on " + self.TodayAsString() + '\n')
            for fname in self.get_list():
                try:
                    f.write(self.print_file_details_as_csv(fname, ["name", "size", "date", "path"] ) + '\n')
                except IOError:
                    print("FAILED LOGGING FILENAME to file_data")
            
        with open(file_usage, 'a', encoding='utf-8') as f:
            for fname in self.get_dirty_filelist():
                try:
                    f.write(self.TodayAsString() + ', ' + fname + ' (' + str(os.path.getsize(fname)) + ' bytes)\n')
                except IOError:
                    print("FAILED LOGGING FILENAME to file_usage")
        """
        pass 
 
    def update_indexes(self, fname):
        """ 
        updates the indexes in AIKIF with any changed files.
        This uses the same process as main metdatalist - check to see if date of index
        is old, THEN update index for that file and call consolidate index
        """
        print("Updating index " + fname)
        
        
    
if __name__ == '__main__':
    TEST()
    
            