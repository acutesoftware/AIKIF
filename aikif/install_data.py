# install_data.py

import os
import aikif.config as cfg
import aikif.cls_log as mod_log

def main():
    """
    script to setup folder structures for AIKIF 
    and prepare data tables.
    """
    print(' --------- AIKIF Installation --------')
    print(' s. show current setup')
    print(' f. setup folder structures')
    print(' c. create sample data')
    print(' w. wipe data and install everything from scratch')
    print(' q. quit')
    cmd = input('?')
    if cmd == 's':
        show_setup()   
    elif cmd == 'f':
        setup_folders()
    elif cmd == 'c':
        create_sample_data()   
    elif cmd == 'w':
        setup_folders()
        create_sample_data()   
    elif cmd == 'q':
        exit(0)
    main()
 
def show_setup():
    print(' -= Current Setup =- ')
    
def setup_folders():
    print('creating folders..')
    create_folder('data')
    create_folder('data\\core')
    create_folder('data\\index')
    create_folder('data\\log')
    create_folder('data\\raw')
    create_folder('data\\ref')
    create_folder('data\\temp')
    

def create_sample_data():
    print('creating sample data')

def create_folder(fldr):
    print('create folder : ', fldr)

 
main()    