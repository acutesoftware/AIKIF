# coding: utf-8
# project.py	written by Duncan Murray 11/1/2015	(C) Acute Software

import os
import sys

aikif_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(aikif_dir)

def TEST():
    print('starting project')
    proj_diary = Project('Diary')
    proj_diary.add_src('Calendar', aikif_dir)
    proj_diary.add_src('Bookmarks', aikif_dir)
    proj_diary.add_src('File Usage', aikif_dir)
    proj_diary.add_src('PC Usage', aikif_dir)
    proj_diary.add_src('TODO List', aikif_dir)

    print(proj_diary)
    
class Project():
    """
    handles the projects in AIKIF, meaning logs the names
    and parameters used for various algorithms.
    """
    def __init__(self, nme, fldr=None):
        self.nme = nme
        self.data_sources = []
        self.fldr = fldr

    def __str__(self):
        res = 'Project : ' + self.nme + '\n'
        for d in self.data_sources:
            res += d[0] + '\t ' + d[1] + '\n'
        return res
    
    def add_src(self, nme, location):
        """
        handles the data sources used in projects, mainly as an 
        abstract to call the data sources in /lib and /dataTools
        """
        self.data_sources.append([nme, location])
    
    
if __name__ == '__main__':
    TEST()	
    