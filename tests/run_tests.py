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

def wipe_file(fname):
    if os.path.exists(fname):
        try:
            os.remove(fname)
            print('deleted ' + fname)
        except:
            pass
        

# cleanup
print ('WIPING ALL TEST RESULTS - PRESS CTRL C TO STOP')

time.sleep(10)
"""
# WARNING - suspect this may wipe from non tests folder in travis-CI 
#   cant find readme.txt after submitting build #100)
# Confirmed - git status shows
# Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    CHANGES.txt
        deleted:    LICENSE.txt
        deleted:    README.txt
        
xtns = ['*.csv', '*.zip',  '*.log', '*.xml']
for xtn in xtns:
    filelist = glob.glob(xtn)
    for f in filelist:
        os.remove(f)
        print('deleting ' + f)
"""
wipe_file('index_odd_chars_results.txt')
wipe_file('index_odd_chars_source.txt')
wipe_file('index_normal_results.txt')
wipe_file('cls_file_test_data.txt')
wipe_file('index_normal_source.txt')
wipe_file('data.txt')
wipe_file('plan_test.txt')
wipe_file('datatable_sample.csv')
wipe_file('datatable_calcs.csv')
wipe_file('csv_sample.csv')
wipe_file('datatable_output.csv')

wipe_file('test_nested.zip')
wipe_file('test2.zip')

wipe_file('sample_small1.xml')
wipe_file('sample_small.xml')