# check_python_env.py   written by Duncan Murray 2/7/2014

import sys
import os
sys.path.append('..\\AI')
import cls_collect_files as cl

packages = ['os', 'sys', 'numpy', 'requests', 'pypyodbc', 'codecs', 're', 'csv' ,
        'operator' , 'datetime' , 'xml' , 'platform' , 'cx_Oracle',
        'socket' , 'getopt', 'unittest' , 'random', 'binascii' , 'time', 
        'xlrd' , 'glob', 'flask' , 'json', 'sqlite3' , 'string' , 'math' 
        ,'getpass' , 'subprocess', 'fnmatch' , 'ctypes']

def check_environment_for_aikif():
    """
    gives status of python environment including which
    of the commonly used (in AIKIF) libraries are installed
    """
    print ("Python Version = " + sys.version)
    lst_all_imports = get_import_list(os.getcwd())
    lst_imports = test_libraries(lst_all_imports)  # no point testing this 
    #print ('\n'.join(lst))
    tok, fail = test_libraries(packages)
    generate_report(lst_all_imports, tok, fail )
    

def generate_report(lst_imports, tok, fail ):
    """
    saves results of environment to local file
    """
    with open("test_results\\environment.md", "w") as f:
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
    py_files = cl.clsCollectFiles(os.path.join(root_folder, os.pardir), '*.py')  # test_cls_collect
    py_files.collect_filelist()
    for fname in py_files.get_filelist():
        print(fname)
        with open(fname, "r") as f:
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