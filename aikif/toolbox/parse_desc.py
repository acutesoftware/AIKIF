#!/usr/bin/python3
# -*- coding: utf-8 -*-
# parse_desc.py


def TEST():
    backup_rules = 'T:\\user\\dev\\src\\python\\AIKIF\\aikif\\data\\ref\\backup_rules.desc'
    p = Parse(backup_rules)
    print(p)
 

def find_key_concepts(txt):
    """
    parse the string 'txt' and return a list of nouns or strings 
    that are in personal ontology lists with a weighting based on
    likely meaning.
    """
    p = Parse(txt)
 
class Parse(object):
    """
    Handles the parsing of english descriptions to a 
    structured set of objects and parameters
    """
    def __init__(self, fname):
        """
        reads a file containing 'semi-structured' english descriptions
        and attempts to parse into commands for aikif
        """
        self.fname = fname   # english descriptions in text file
        self.raw = []        # list of cleaned descriptions
        self.locations = []  # list of folder locations or websites
        self.users = []      # list of users who will access the files
        self.rules = []      # rules showing which users can access which locations
        self.schedules = []  # final schedules for backups
        self.key_concepts = [] # list of key concepts (projects / strings from pers ontology)
        self._read_file()
        

    def __str__(self):
        res = ''
        for line in self.raw:
            res += line + '\n'
        return res
        
    def _read_file(self):
        """
        reads the file and cleans into standard text ready for parsing
        """
        self.raw = []
        with open(self.fname, 'r') as f:
            for line in f:
                #print(line)
                if line.startswith('#'):    
                    pass # comment
                elif line.strip('\n') == '':
                    pass # space
                else:
                    self.raw.append(line.strip('\n'))
            
TEST()            