# install_data.py

import os
import aikif.config as cfg
import aikif.cls_log as mod_log
cur_path = os.getcwd()

def main():
    """
    script to setup folder structures for AIKIF 
    and prepare data tables.
    """
    print('\n\n --------- AIKIF Installation --------')
    print(' s. show current setup')
    print(' f. setup folder structures')
    print(' c. create sample data')
    print(' w. wipe data and install everything from scratch')
    print(' q. quit')
    cmd = input('?')
    if cmd == 's':
        show_setup()   
    elif cmd == 'f':
        setup_folders(cur_path)
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
    
def setup_folders(cur_path):
    print('creating folders..')
    create_folder(cur_path + os.sep + 'data')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'core')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'index')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'log')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'raw')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'ref')
    create_folder(cur_path + os.sep + 'data' + os.sep + 'temp')
    

def create_sample_data():
    print('creating sample data')

def create_folder(fldr):
    print('creating folder ' + fldr)
    ensure_dir(fldr)

def ensure_dir(f):
    d = os.path.dirname(f)
    #print('ensure_dir=' + d)
    if not os.path.exists(d):
        os.makedirs(d) 
main()    