# install_data.py

import os
cur_path = os.getcwd()
config_file = cur_path + os.sep + '..' + os.sep + 'data' + os.sep + 'pers_config.py'
def main():
    """
    script to setup folder structures for AIKIF 
    and prepare data tables.
    """
    print('\n\n /------- AIKIF Installation --------\\')
    print(' |  s. show current setup            |')
    print(' |  f. setup folder structures       |')
    print(' |  c. create sample data            |')
    # not yet - wait for beta release print(' w. wipe data and install everything from scratch')
    print(' |  q. quit                          |')
    print(' \\-----------------------------------/')
    cmd = input('?')
    if cmd == 's':
        show_setup()   
    elif cmd == 'f':
        setup_folders()
    elif cmd == 'c':
        create_sample_data()   
    #elif cmd == 'w':
    #    wipe_and_rebuild_all()
    elif cmd == 'q':
        exit(0)
    main()

def wipe_and_rebuild_all():
    setup_folders()
    create_sample_data()   
    
def setup_folders():
    print('creating folders..')
    create_folder('data')
    os.chdir('data')
    create_folder('core')
    create_folder('log')
    create_folder('raw')
    create_folder('ref')
    create_folder('temp')


def create_folder(fldr):
    try:
        os.mkdir(fldr) 
        print('creating folder ' + fldr)
    except Exception:
        print(os.getcwd() + os.sep + fldr + ' already exists')

def show_setup():
    print(' -= Current Setup =- ')
    try:
        with open(config_file, 'r') as cfg_file:
            print(cfg_file.read())
            #for line in cfg_file:
            #    print(line)
    except Exception:
        print('No config file - press c to create sample data\n')
    
def create_sample_data():
    if os.path.isfile(config_file):
        print('== WARNING - CONFIG DATA ALREADY EXISTS ==\n')
        show_setup()
        print('== ENTER OK to wipe this data and reset ==\n')
        if input() != 'OK':
            print('Aborting create sample data')
            return
    print('creating sample data')
    with open(config_file, 'w') as f:
        f.write('# pers_config.py  - created by aikif.install_data.py\n')
        f.write('# Modify this file after running create sample data\n')
        f.write('LOG_LEVEL = "ERROR"\n')
        f.write('username = "your_name"\n')
        f.write("fldrs['localPath'] = '" + cur_path + "'\n")
        f.write("fldrs['data_folder'] = fldrs['localPath'] + os.sep + 'data'\n")
        f.write('\n')
  
if __name__ == '__main__':  
    main()    