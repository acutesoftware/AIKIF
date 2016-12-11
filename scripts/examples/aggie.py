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
    lg = mod_log.Log(log_fldr)
    lg.record_source('aggie.py','Hello, my name is Aggie.')
    lg.record_source('aggie.py','base folder is ' + mod_cfg.get_root_folder()[1])
    print('done')
    
main()    
    
