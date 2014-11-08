# maths_fermat_brute_force.py   written by Duncan Murray 8/11/2014

import os
import sys
from random import randint 
sys.path.append('..')
import config as mod_cfg
import cls_log as mod_log

def main():
    """
    Example of logging the success of a Brute force using AIKIF.
    This uses http://en.wikipedia.org/wiki/Fermat's_Last_Theorem
    which was proven in 1994-1995 so you will not get a success
    result with this program unless you set the power to 2
    (the point of the program is not to solve it, but to show how
    to log a complex running algorithm)
 
    Steps are:
    1. Define a name for the project (MATHS_FERMAT) which then 
       becomes the log folder as subfolder of your private logs.
    2. do the imports and instantiate the Log class
    3. call record_command to show how often you run this example
    4. call record_source to show the parameters chosen for each run
    5. call record_result when you solve it (ha!), or it fails
    
    TODO
    - polish the log details to make easier aggregation
    - call the LogSummary class to do the aggregation
    - Add logSummary method to show percent success based on param ranges
    
    """
    proj = 'MATHS_FERMAT'
    log_folder = mod_cfg.fldrs['log_folder'] + os.sep + proj
    mod_log.ensure_dir(log_folder)
    mylog = mod_log.Log(log_folder)
    #mode = 'QUICK'
    mode = 'AVERAGE'
    #mode = 'HARD'  # assumes you have infinite time and CPU resources
    #mode = 'TEST_FAILURE_NOT_FERMAT'
    start_x = randint(1,9999999999999999999999999999999999)
    start_y = randint(1,9999999999999999999999999999999999)
    start_z = randint(1,9999999999999999999999999999999999)
    start_n = 3
    end_n = 3
    if mode == 'QUICK':
        steps_x = 50
        steps_y = 30
        steps_z = 10
        start_n = 3
        end_n = 15
    elif mode == 'AVERAGE':
        steps_x = 100
        steps_y = 100
        steps_z = 20
        start_n = 3
        end_n = 15
    elif mode == 'HARD':
        steps_x = 99999999
        steps_y = 99999999
        steps_z = 3000
        start_n = 3
        end_n = 99999
    elif mode == 'TEST_FAILURE_NOT_FERMAT':   # test mode power 2 (to test 'True' case though not Fermat test)
        start_x = 2
        start_y = 2
        start_z = 2
        start_n = 2
        end_n = 3
        steps_x = 10
        steps_y = 10
        steps_z = 10
        
    mylog.record_command(proj, ' starting brute force program in mode ' + mode)      
    mylog.record_source(proj, mode + ' Start Params. steps: x=' + str(steps_x) + 'y=' + str(steps_y) + ',z=' + str(steps_z) + '. Start vals ='+ format_vars_as_string(start_x, start_y, start_z, start_n) )      

    fame_and_fortune = False
    tot_calcs = 0
    for n in range(start_n, end_n):
        print('n = ', n)
        for i in range(start_z, (start_z + steps_z)):
            print('testing n=', n, ' z=', i, ' (total calcs = ', tot_calcs , ')')
            for j in range(start_y, (start_y + steps_y)):
                for k in range(start_x, (start_x + steps_x)):
                    tot_calcs += 1
                    if not fermat_test(k,j,i,n):
                        fame_and_fortune = True
                        mylog.record_result(proj, 'FOUND MATCH = ' + format_vars_detailed(k,j,i,n))      
    if fame_and_fortune:
        print('Found match!')
    else:
        print('No matches found - total calculations = ' + str(tot_calcs))
        mylog.record_result(proj, 'FAILED with params: ' + format_vars_as_string(k,j,i,n) + ' after ' + str(tot_calcs) + ' calculations')    
    
def format_vars_as_string(x,y,z,n):
    """   return as a string for logging or printing """
    return 'x=' + str(x) + ', y=' + str(y) + ', z=' + str(z) + ', n=' + str(n)
    
    
def format_vars_detailed(x,y,z,n):
    """  return vars and proof as a string for logging or printing """
    res = str(x) + '**n=' + str(x**n) + ' + ' + str(y) + '**n=' + str(y**n) + ' = ' + str(z) + '**n=' + str(z**n)
    return res
    
def fermat_test(x, y, z, n):
    """ check to see if the parameters pass the test """
    if x**n + y**n == z**n:
        print('Match found !', x,y,z,n)
        print('PROOF: ' + format_vars_detailed(x,y,z,n)) 
        return False
    return True
    
  
if __name__ == '__main__': 
    main()    