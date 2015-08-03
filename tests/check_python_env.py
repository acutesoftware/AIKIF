# check_python_env.py   written by Duncan Murray 2/7/2014

import sys
import os

import aikif.lib.cls_filelist as cl

packages = ['os', 'sys', 'requests', 'pypyodbc', 'codecs', 're', 'csv' ,
        'operator' , 'datetime' , 'xml' , 'platform' , 
        'socket' , 'getopt', 'unittest' , 'random', 'binascii' , 'time', 
        'xlrd' , 'glob', 'flask' , 'json', 'sqlite3' , 'string' , 'math' 
        ,'getpass' , 'subprocess', 'fnmatch' , 'ctypes']

def check_environment_for_aikif():
    """
    gives status of python environment including which
    of the commonly used (in AIKIF) libraries are installed
    """
    print ("Python Version = " + sys.version)
    lst_all_imports = get_import_list(os.getcwd() + os.sep + '..')
    lst_imports = test_libraries(lst_all_imports)
    tok, fail = test_libraries(packages)
    generate_report(lst_all_imports, tok, fail )
    

def generate_report(lst_imports, tok, fail ):
    """
    saves results of environment to local file
    """
    op_file = "test_results\\environment.md"
    with open(op_file, "w") as f:
        f.write("#environment.md\n")
        f.write("Details on development environment, imports, code fixes todo.\nCreated by check_python_env.py\n\n")
        f.write("\n###Python version\n")
        f.write(sys.version + "\n")
        f.write("\n##Required packages\n")
        f.write("###Packages needed to be installed\n")
        for imp in fail:
            f.write(imp + "<BR>")
        f.write("\n\n###Packages required and already installed\n")
        for imp in tok:
            f.write(imp + ", ")
        f.write(imp + "<BR><BR>\n\n")
        f.write("##List of all imports in all modules\n")
        for imp in lst_imports:
            f.write(imp + "<BR>\n")        
    print('Done - see ' + op_file + ' for details')

def get_import_list(root_folder):
    """
    scans a root folder for all python files and gets a 
    list of all imports. Wait, stop - this wont work due
    to various local imports of aikif local py files.
    Shelve for now, use hard coded list
    """
    import_statements = []
    print("ROOT FOLDER = " + root_folder)
#    py_files = cl.clsCollectFiles(os.path.join(os.path.dirname(root_folder), os.pardir), '*.py')  # test_cls_collect
    
    py_files = cl.FileList([root_folder], ['*.py'], [], "sample_filelist.csv")
    for fname in py_files.fl_metadata:
        #print(fl.print_file_details_in_line(f, ["fullfilename"]))
        print(fname["fullfilename"])
        with open(fname["fullfilename"], "r") as f:
            for line in f:
                if line.strip()[0:6] == 'import':
                    import_statements.append(line.strip()[7:])
                    #print (line)
     
    return list(set(import_statements))
    
def test_libraries(libs):
    """ 
    takes a list of libraries and checks that they
    can be imported
    """
    tok = []
    fail = []
    for lib in libs:
        try:
            _ = mod = __import__(lib)
            tok.append(lib)
        except:
            fail.append(lib + ' Fail')
            
    return tok, fail
    
    
if __name__ == "__main__":
    check_environment_for_aikif()