# maths_fermat_brute_force.py   written by Duncan Murray 8/11/2014

import os
import sys
from random import randint 
sys.path.append('..')
import config as mod_cfg
import cls_log as mod_log

def main():
    """
    Brute force 
    
    
    self.mylog.record_process('test', 'hello - recording process')
      
    self.mylog.record_result('test', 'hello - recording result')        
    self.mylog.record_source('test', 'hello - recording source')        

    """
    proj = 'MATHS_FERMAT'
    log_folder = mod_cfg.fldrs['log_folder'] + os.sep + proj
    mod_log.ensure_dir(log_folder)
    mylog = mod_log.Log(log_folder)
    mylog.record_command(proj, 'starting brute force program')      
    mode = 'QUICK'
    mode = 'AVERAGE'
    mode = 'HARD'  # assumes you have infinite time and CPU resources
    mode = 'TEST_FAILURE_NOT_FERMAT'
    start_x = randint(1,9999999999999999999999999999999999)
    start_y = randint(1,9999999999999999999999999999999999)
    start_z = randint(1,9999999999999999999999999999999999)
    start_n = 3
    end_n = 3
    if mode == 'QUICK':
        steps_x = 5000
        steps_y = 30
        steps_z = 300
        start_n = 3
        end_n = 15
    elif mode == 'AVERAGE':
        steps_x = 998
        steps_y = 98
        steps_z = 18
        start_n = 3
        end_n = 15
    elif mode == 'HARD':
        steps_x = 99999999
        steps_y = 99999999
        steps_z = 3000
        start_n = 3
        end_n = 9999
    elif mode == 'TEST_FAILURE_NOT_FERMAT':   # test mode power 2 (to test 'True' case though not Fermat test)
        start_x = 2
        start_y = 2
        start_z = 2
        start_n = 2
        end_n = 3
        steps_x = 10
        steps_y = 10
        steps_z = 10
        
    # as starting point, iterate z**n to ensure whole numbers will work 
    mylog.record_source(proj, 'Start Params = ' + format_vars_as_string(start_x, start_y, start_z, start_n) )      

    print('Brute Force example - mode = ' + mode)
    fame_and_fortune = False
    tot_calcs = 0
    for n in range(start_n, end_n):
        print('n = ', n)
        for i in range(start_z, (start_z + steps_z)):
            print('testing n=', n, ' z=', i, ' (total calcs = ', tot_calcs , ')')
            for j in range(start_y, (start_y + steps_y)):
                #print('testing  y=', j, ', z=', i)

                for k in range(start_x, (start_x + steps_x)):
                    tot_calcs += 1
                    if not fermat_test(k,j,i,n):
                        fame_and_fortune = True
                        mylog.record_result(proj, 'FOUND MATCH = ' + format_vars_as_string(k,j,i,n))      

                        break
    if fame_and_fortune:
        print('Found match!')
    else:
        print('No matches found - total calculations = ' + str(tot_calcs))
    
def format_vars_as_string(x,y,z,n):
    """   return as a string for logging or printing """
    return 'x=' + str(x) + ', y=' + str(y) + ', z=' + str(z) + ', n=' + str(n)
    
    
def format_vars_detailed(x,y,z,n):
    """  return vars and proof as a string for logging or printing """
    res = str(x) + '**n=' + str(x**n) + ' + ' + str(y) + '**n=' + str(y**n) + ' = ' + str(z) + '**n=' + str(z**n)
    return res
    
def fermat_test(x, y, z, n):
    if x**n + y**n == z**n:
        print('Match found !', x,y,z,n)
        print('PROOF: ' + format_vars_detailed(x,y,z,n)) 
        return False
    else:
        pass
        #print('testing x=', x, ' , y=', y, ', z=', z)
    #print('no luck')    
    return True
    
    
    
 
if __name__ == '__main__': 
    main()    