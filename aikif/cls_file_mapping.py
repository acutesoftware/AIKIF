# cls_file_mapping.py   written by Duncan Murray 13/9/2014

import os
import sys
import aikif.lib.cls_filelist as mod_fl

root_folder   = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
dataPath      = root_folder + os.sep + "data"
dataFiles     = []  # complete mapping of file types to physical CSV files
dataFileTypes = [
    'EVENT',    # when
    'LINK',     # how	'relationship', <- relationship is a TYPE of link
    'OBJECT',   # reference file lookup to get heirachy
    'THING',    # what
    'LOCATION', # where
    'PROCESS',  # another what?
    'ACTOR'     # who
    ]
    
dataSubjectAreas = [
    '_TOP', 		# this is the top level ontology for all subject areas
    'INFO-COURSE', 
    'INFO-DATASET', 
    'INFO-PIM', 
    'INFO-PIM-SHOPPING', 
    'INFO-PIM-DIARY',
    'INFO-PIM-PROJECT',
    'INFO-PIM-TASK',
    'INFO-PIM-CONTACT',
    'INFO-PIM-NOTE',
    'INFO-PIM-PCUSAGE',
    'INFO-MESSAGE',
    'INFO-MESSAGE-EMAIL',
    'INFO-MESSAGE-SMS',
    'INFO-MESSAGE-PHONE',
    'INFO-MESSAGE-FORUM',
    'INFO-MESSAGE-LETTER',
    'INFO-SOCIAL-TWITTER',
    'INFO-SOCIAL-FACEBOOK',
    'INFO-SOCIAL-GOOGLE+',
    'INFO-SOCIAL-OTHER',
    'OBJECT-ASSET', 
    'OBJECT-ASSET-COMPUTER', 
    'OBJECT-ASSET-FURNITURE', 
    'OBJECT-ASSET-CAR', 
    'OBJECT-ASSET-RESOURCE', 
    'SYSTEM-PC-LOG', 
    'SYSTEM-PC-FILE', 
    'SYSTEM-PC-FILE-LECTURES', 
    'SYSTEM-PC-FILE-PROGRAM', 
    ]


class FileMap:
    """
    Provides mapping to file names
    
    """
    def __init__(self, localPath):
        self.name = name
        self.fldr = fldr


        
        