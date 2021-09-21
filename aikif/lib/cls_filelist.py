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
#import aikif.cls_log as mod_log

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

class FileList(object):
    def __init__(self, paths, xtn, excluded, output_file_name = 'my_files.csv'):
        self.output_file_name = output_file_name
        self.filelist = []       # list of full filenames
        self.fl_metadata = []    # dictionary of all file metadata
        self.paths = paths
        self.xtn = xtn
        self.excluded = excluded
        self.get_file_list(self.paths, self.xtn, self.excluded)

    def get_list(self):
        return self.filelist

    def get_metadata(self):
        return self.fl_metadata


    def get_list_of_paths(self):
        """
        return a list of unique paths in the file list
        """
        all_paths = []
        for p in self.fl_metadata:
            try:
                all_paths.append(p['path'])
            except:
                try:
                    print('cls_filelist - no key path, ignoring folder ' + str(p))
                except:
                    print('cls_filelist - no key path, ignoring odd character folder')

        return list(set(all_paths))


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
        file_dict["fullfilename"] = fname
        try:
            file_dict["name"] = os.path.basename(fname)
            file_dict["date"] = self.GetDateAsString(fname)
            file_dict["size"] = os.path.getsize(fname)
            file_dict["path"] = os.path.dirname(fname)
        except IOError:
            print('Error getting metadata for file')

        self.fl_metadata.append(file_dict)

    def print_file_details_in_line(self, fname, col_headers):
        """
        makes a nice display of filename for printing based on columns passed
        print('{:<30}'.format(f["name"]), '{:,}'.format(f["size"]))
        """
        line = ''
        try:
            sze = os.path.getsize(fname)
        except Exception as ex:
            return 'no file'
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

        op_folder = os.path.dirname(opFile)
        if op_folder is not None:   # short filename passed
            if not os.path.exists(op_folder):
                os.makedirs(op_folder)


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
