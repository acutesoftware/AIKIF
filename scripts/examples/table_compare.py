#!/usr/bin/python3
# -*- coding: utf-8 -*-
# table_compare.py

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder + os.sep + 'dataTools')

import cls_datatable as cl

with open('dummy_table1.csv', "w") as f:
    f.writelines(
"""TERM,GENDER,ID,tot1,tot2
5300,F,00078,18,66
7310,M,00078,18,465
7310,M,00078,10,12
7310,F,00078,30,2
7310,F,00016,25,12
5300,M,00016,31,0 
7310,F,00016,67,873""")

with open('dummy_table2.csv', "w") as f:
    f.writelines(
"""TERM,GENDER,ID,tot1,tot2,tot3
5300,F,00078,18,66,45
7310,M,00078,16,465,64
7310,F,00078,30,2,3
7310,F ,00016,25,12,2
5320,M,00016,31,0,66
7310,F,00016,67,873,2""")


old_table = 'dummy_table1.csv'
new_table = 'dummy_table2.csv'


def main():
    analysis = cl.DataTable('Results' , ',', col_names = ['results'])
    if len(sys.argv) != 3:
        print('usage:')
        print('table_compare.py "TABLE1.CSV" "TABLE2.CSV":')
        old_table = 'dummy_table1.csv'
        new_table = 'dummy_table2.csv'
    else:
        old_table = sys.argv[1]
        new_table = sys.argv[2]
    

    t_old = cl.DataTable(old_table, ',')
    t_old.load_to_array()
    t_old.describe_contents()
    
    t_new = cl.DataTable(new_table, ',')
    t_new.load_to_array()
    t_new.describe_contents()

    res, pass_fail = check_col_names(t_old, t_new)
    #print(res)
    analysis.add([res])
    if pass_fail != 'OK':
        print('Bypassing exact row test, as columns are different')
    else:
        print(check_rows(t_old, t_new))

    res, pass_fail = compare_values(t_old, t_new)
    analysis.add([res])
    res = distinct_values(t_old, t_new)
    for r in res:
        analysis.add(r)
        
    analysis.save_csv('results.csv', write_header_separately=True)
    
    import pprint
    pprint.pprint(analysis)
    
def check_col_names(t_old, t_new):
    res = '\n -- Column Name check -- \n'
    pass_fail = 'OK'
    for col_num, c in enumerate(t_old.header):
        if len(t_new.header) >= col_num + 1:
            if c == t_new.header[col_num]:
                res += c + ' ok\n'
            else:
                res += c + ' different name (now ' + t_new.header[col_num] + ')\n'
                pass_fail = 'Different Name'
        else:
            res += c + ' is missing in new table\n'
            pass_fail = 'Missing Column'
    return res, pass_fail
    
    
def check_rows(t_old, t_new):
    res = '\n -- Row Name check#1 -- \n'

    for row_num, r in enumerate(t_old.arr):
        if len(t_new.arr) >= row_num + 1:
            if r == t_new.arr[row_num]:
                res += str(row_num) + ' ok\n'
            else:
                res += str(r) + ' different values (now ' + str(t_new.arr[row_num]) + ')\n'
        else:
            res += str(r) + ' is missing in new table\n'
    return res
    
def compare_values(t_old, t_new):
    res = '\n -- compare_values -- \n'
    pass_fail = 'OK'

    for row_num, r in enumerate(t_old.arr):
        if len(t_new.arr) >= row_num + 1:
            for col_num, c in enumerate(r):
                if c == t_new.arr[row_num][col_num]:
                    #res += c + ' ok\n'
                    pass
                else:
                    res += ' different value in r[' + str(row_num) + ']c[' + str(col_num) + '] ' + t_new.header[col_num] + ' was ' + c +  ' => ' + t_new.arr[row_num][col_num] + '\n'
                    pass_fail = 'Different value'

    return res, pass_fail
    
def distinct_values(t_old, t_new):   
    """
    for all columns, check which values are not in 
    the other table
    """
    res = []
    for new_col in t_new.header:
        dist_new = t_new.get_distinct_values_from_cols([new_col])
        #print('NEW Distinct values for ' + new_col + ' = ' + str(dist_new))
        for old_col in t_old.header:
            if old_col == new_col:
                dist_old = t_old.get_distinct_values_from_cols([old_col])
                #print('OLD Distinct values for ' + old_col + ' = ' + str(dist_old))
                
                # Now compare the old and new values to see what is different
                not_in_new = [x for x in dist_old[0] if x not in dist_new[0]]
                if not_in_new != []:
                    #print(old_col + ' not_in_new = ' , not_in_new)
                    res.append(['Not in New', old_col, not_in_new])
                    
                not_in_old = [x for x in dist_new[0] if x not in dist_old[0]]
                if not_in_old != []:
                    #print(new_col + ' not_in_old = ' , not_in_old)
                    res.append(['Not in Old', new_col, not_in_old])
                    
                    
    
    return sorted(res)

if __name__ == '__main__':
    main()    

