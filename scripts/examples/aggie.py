#!/usr/bin/python3
# -*- coding: utf-8 -*-
# aggie.py

#import aikif.config as mod_cfg
#import aikif.cls_log as mod_log

import sys
import os
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." )
code_fldr = os.path.join(root_fldr, 'aikif')
sys.path.append(code_fldr)
log_fldr = os.path.join(root_fldr, 'tests', 'test_results')
import config as mod_cfg
import cls_log as mod_log


def main():
    
    a = Aggie()
    print(a)
    print('done')
    

class Aggie(object):
    """
    main class for agent
    """
    
    def __init__(self, fldr=os.getcwd()):
        self.fldr = fldr
        self.lg = mod_log.Log(fldr)
        self.lg.record_source('aggie.py','Hello, my name is Aggie.')
        self.lg.record_source('aggie.py','base folder is ' + self.fldr)
        
    def __str__(self):
        return 'running aggie in ' + self.fldr
    
main()    
    
