#!/usr/bin/python3
# aikif_test_utils.py
"""
module to import for all test modules in /tests
NOTE - use this for constants such as folder paths
but do not rely on it for the sys.path in case there
are side effects with CI tools - keep it simple and 
do a sys.path.insert in each of the test modules
from https://docs.python.org/3/library/sys.html
sys.path
A list of strings that specifies the search path for modules. Initialized from
 the environment variable PYTHONPATH, plus an installation-dependent default.

As initialized upon program startup, the first item of this list, path[0], is 
the directory containing the script that was used to invoke the Python 
interpreter. If the script directory is not available (e.g. if the interpreter
 is invoked interactively or if the script is read from standard input), 
 path[0] is the empty string, which directs Python to search modules in the 
 current directory first. Notice that the script directory is inserted before
 the entries inserted as a result of PYTHONPATH.

A program is free to modify this list for its own purposes. Only strings and
bytes should be added to sys.path; all other data types are ignored during 
import.
"""
import os
import sys
root_fldr = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_fldr)

test_fldr = os.path.dirname(__file__) + os.sep + 'test_results'

print('root_fldr : ' + root_fldr)
print('test_fldr : ' + test_fldr)
