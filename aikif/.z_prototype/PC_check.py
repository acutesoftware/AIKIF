# PC_check.py

# called by AIKIF to log PC status
# - hard disk space
# apps installed
# files used (called filelister via cls_collect_file)

#

import fnmatch
import os
import sys 

def main():
    pattern = '*.*'
    #pattern = '*.py'
    try:
        fldr =  sys.argv[1]
        listFiles = 'N'
    except:
        fldr = os.getcwd()
        listFiles = 'N' #'Y'
    print(("listFiles=" + listFiles))
    fldrs, files, bytes = GetFolderSize(fldr, pattern, listFiles)
    print(("Found " + str(files) + " in " + str(fldrs) + " Total size = " + str(bytes) + " (" + str(bytes/1000000) + "MBytes)"))

def GetFileSize(fname):
    #print(fname)
    sze = os.path.getsize(fname)
    
#	except:
#		file_size = 0
#    	print ("Cant get file size for " + filename)
    
    return sze
    
def GetFolderSize(rootPath, pattern, showFiles): 
    tot_bytes = 0
    tot_files = 0
    tot_fldrs = 0
    cur_bytes = 0
    cur_files = 0
    for root, dirs, files in os.walk(rootPath):
        tot_fldrs += 1
        print(( root + ", " + str(cur_files) + " files ( "  + str(cur_bytes/1000) + "kBytes)" ))
        cur_bytes = 0
        cur_files = 0
        for filename in fnmatch.filter(files, pattern):
            file_size = GetFileSize(os.path.join(root, filename)) 
            tot_files += 1
            cur_files += 1
            tot_bytes += file_size
            cur_bytes += file_size
            #print( os.path.join(root, filename))
            if showFiles == 'Y':
                print(( os.path.join(root, filename), str(file_size)))
            #print( filename, file_size)
            
    return tot_fldrs, tot_files, tot_bytes		
    
main()