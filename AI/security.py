# coding: utf-8
# security.py	written by Duncan Murray 23/3/2014	(C) Acute Software
# security and privacy settings for AIKIF

import os
import sys
import AIKIF_utils as aikif
import fileMapping as filemap

if len(sys.argv) == 2:
    viewStructure = sys.argv[1]

securityLevels = [
    'NONE', 	# anyone
    'NETWORK',  # all users on any device in the network
    'WORK',		# your work group (customise this - have as many as desired)
    'FAMILY',	# your family
    'PARTNER',	# your partner
    'SELF'		# yourself
    ]
    

privateFiles = []
privateFiles.append(filemap.GetFullFilename(filemap.FindType('thing'), filemap.FindOntology('shopping')[0]))
privateFiles.append(filemap.GetFullFilename(filemap.FindType('event'), filemap.FindOntology('shopping')[0]))

workFiles = []
workFiles.append(filemap.GetFullFilename(filemap.FindType('location'), filemap.FindOntology('file')[0]))


securityMappings = []
    
def MapSecurityLevel(files, security):   
    # call this function when adding sensitive data
    for file in files:
        securityMappings.append([file, security])

    
def show_security():
    res = ''
    num = 0
    res += 'num\tmap\tfile\n'
    res += '---\t------\t-------------------------------------\n'
    for map in securityMappings:
        num = num+ 1
        res += str(num) + '\t' + map[1] + '\t' + os.path.basename(map[0]) + '\n'
    return res
        
def main():
    # main function 
    MapSecurityLevel(workFiles, 'WORK')
    MapSecurityLevel(privateFiles, 'FAMILY')

    aikif.LogProcess('Starting Security',  'view.py') 
    print('AIKIF Security Settings')
    
    
    print(show_security())
    
    
if __name__ == '__main__':
    main()	
    
        
        