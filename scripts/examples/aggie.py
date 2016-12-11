#!/usr/bin/python3
# -*- coding: utf-8 -*-
# aggie.py

import aikif.config as mod_cfg
import aikif.cls_log as mod_log

def main():
    mod_log.record_source('aggie.py','Hello, my name is Aggie.')
    mod_log.record_source('aggie.py','base folder is ', mod_cfg.get_root_folder()[1])
    print('done')
    
main()    
    
