# coding: utf-8
# project.py	written by Duncan Murray 11/1/2015	(C) Acute Software

import os
import sys

aikif_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(aikif_dir)

def TEST():
    print('starting project')
    myproj = Project()
    
    
class Project():
    """
    handles the projects in AIKIF, meaning logs the names
    and parameters used for various algorithms.
    """
    pass


    
if __name__ == '__main__':
    TEST()	
    