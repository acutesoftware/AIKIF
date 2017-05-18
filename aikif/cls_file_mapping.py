#!/usr/bin/python3
# coding: utf-8
# cls_file_mapping.py

import os
from . import config as mod_cfg
import yaml

root_folder   = mod_cfg.fldrs['root_path']
dataPath      = root_folder + os.sep + 'aikif' + os.sep + "data"
dataFiles     = [] 


"""
Load the ontology lookup files externally
See issue #22 for details on moving to local ontology
https://github.com/acutesoftware/AIKIF/issues/22
"""

subject_file = root_folder + os.sep + "data" + os.sep + "ref" + os.sep + "ONTOLOGY_SUBJECT_AREA.txt"
file_type_file = root_folder + os.sep + "data" + os.sep + "ref" + os.sep + "ONTOLOGY_FILE_TYPE.txt"


dataFileTypes = []
dataSubjectAreas = []

def load_data_subject_areas(subject_file):
    """
    reads the subject file to a list, to confirm config is setup
    """
    lst = []
    if os.path.exists(subject_file):
        with open(subject_file, 'r') as f:
            for line in f:
                lst.append(line.strip())
    else:
        print(('MISSING DATA FILE (subject_file) ' , subject_file))
        print('update your config.py or config.txt')
    return lst

        
        
def load_data_file_types(file_type_file):
    lst = []
    if os.path.exists(file_type_file):
        with open(file_type_file, 'r') as f:
            for line in f:
                lst.append(line.strip())
    else:
        print(('MISSING DATA FILE (file_type_file) ' , file_type_file))
        print('update your config.py or config.txt')
    return lst


class FileMap(object):
    """
    Provides mapping to file names
    """
    def __init__(self, lst_type, lst_subj):
        self.root_folder = root_folder
        self.dataPath    = root_folder + os.sep + "aikif" + os.sep + "data"
        self.dataFiles   = []
        
        if lst_type == []:
            self.lst_type = load_data_file_types(file_type_file)
        else:
            self.lst_type = lst_type
        
        if lst_subj == []:
            self.lst_subj = load_data_subject_areas(file_type_file)
        else:
            self.lst_subj = lst_subj
        
 
    def get_root_folder(self):
        """ 
        returns root path for data folder - used by other modules in aikif 
        """
        return self.root_folder 
     
    def get_datapath(self):
        """ 
        returns root path for data folder - used by other modules in aikif 
        """
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
            for i in self.lst_subj:
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
        for i in self.lst_type:
            if searchString in i:
                match = i
        return match
        
    def get_full_filename(self, dataType, subjectArea):
        """ 
        returns the file based on dataType and subjectArea 
        """
        return dataPath + os.sep + 'core' + os.sep + dataType + '_' + subjectArea + '.CSV'
        
    def get_filename(self, dataType, subjectArea):
        """ 
        get relative filename of core file 
        """
        return dataType + '_' + subjectArea + '.CSV'
        
    def add_file_to_mapping_list(self, fname, lst):
        """ 
        adds the name of the file to the list 
        """
        lst.append(fname)
        
def check_ontology(fname):    
    """
    reads the ontology yaml file and does basic verifcation
    """
    with open(fname, 'r') as stream:
        y = yaml.safe_load(stream)
    import pprint
    pprint.pprint(y) 


    