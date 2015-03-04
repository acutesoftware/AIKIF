# cls_file_mapping.py   written by Duncan Murray 13/9/2014

import os
import sys
import aikif.lib.cls_filelist as mod_fl
import aikif.config as mod_cfg

root_folder   = mod_cfg.fldrs['root_path']
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
        self.root_folder = root_folder
        self.dataPath    = root_folder + os.sep + "data"
        self.localPath   = localPath
        self.dataFiles   = []
 
    def get_root_folder(self):
        """ returns root path for data folder - used by other modules in aikif """
        return self.root_folder 
      
    def get_localPath(self):
        """ returns root path for data folder - used by other modules in aikif """
        return self.localPath 
      
    def get_datapath(self):
        """ returns root path for data folder - used by other modules in aikif """
        return self.dataPath 
      
    def find_ontology(self, txt):
        """
        top level function used for new data processing which attempts
        to find a level in a heirarchy and return the key and filename
        usage res = FindOntology('file')  # returns 'SYSTEM-PC-FILE'
        """
        totFound = 0
        searchString = txt.upper()
        match = []
        if searchString != '':
            for i in dataSubjectAreas:
                if searchString in i:
                    totFound = totFound + 1
                    match.append(i)
        if len(match) == 0:
            match.append('_TOP')
        return match

    def find_type(self, txt):
        """
        top level function used to simply return the 
        ONE ACTUAL string used for data types
        """
        searchString = txt.upper()
        match = 'Unknown'
        for i in dataFileTypes:
            if searchString in i:
                match = i
        return match
        
    def get_full_filename(self, dataType, subjectArea):
        """ returns the file based on dataType and subjectArea """
        return dataPath + os.sep + 'core' + os.sep + dataType + '_' + subjectArea + '.CSV'
        
    def get_filename(self, dataType, subjectArea):
        """ get relative filename of core file """
        return dataType + '_' + subjectArea + '.CSV'
        
    def add_file_to_mapping_list(self, fname, lst):
        """ adds the name of the file to the list """
        lst.append(fname)
        
        