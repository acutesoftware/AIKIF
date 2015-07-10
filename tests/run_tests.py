# run_tests.py

import os
import glob
import time
import unittest as unittest

#root_folder =  os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + "..") 
#sys.path.append(root_folder + os.sep + 'lib')

import aikif.lib.cls_filelist as fl 

# run all tests in tests folder
all_tests = unittest.TestLoader().discover('.', pattern='test*.py')
unittest.TextTestRunner().run(all_tests)    

# cleanup
print ('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(10)

xtns = ['*.csv', '*.zip', '*.txt', '*.log', '*.xml']
for xtn in xtns:
    filelist = glob.glob(xtn)
    for f in filelist:
        os.remove(f)
        print('deleting ' + f)

        