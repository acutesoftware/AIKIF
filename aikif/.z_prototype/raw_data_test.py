# raw_data_test.py

import os
import sys

# AIKIF latest files
aikif_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  )
sys.path.append(aikif_fldr)
sys.path.append(os.path.join(aikif_fldr, 'dataTools'))
print(' aikif_fldr = ', aikif_fldr)
import project as mod_prj
import cls_datatable as mod_dt

# rawdata latest files (from this prototype folder in AIKIF)
rawdata_fldr = os.path.join(os.path.abspath(os.path.dirname(os.path.abspath(__file__))), "..", "..", "..", 'rawdata', 'rawdata'  )
sys.path.append(rawdata_fldr)
print(' rawdata_fldr = ', rawdata_fldr)
import generate
import content

def main():
    """
    test for rawdata module to create test files
    """
    
    
    print('Initialising rawdata for AIKIF...')
    
    # setup project for logging
    name = 'rawdata_gen'
    type = 'Data'
    desc = 'Creates raw data tables for aikif'
    desc += '\n     Last updated ' + mod_dt.TodayAsString()	
    fldr = os.getcwd()
    p = mod_prj.Project(name, type, desc, fldr)
    p.add_detail('source', 'pip install rawdata')

    
    # create the rawdata
    col_names = ['Year', 'name',   'Purchase', 'Location']
    col_types = ['DATE', 'PEOPLE', 'CURRENCY', 'PLACE']
    t = generate.TableGenerator(10, col_types, col_names)
    
    
    # save the table (you can save it via rawdata class, but demonstrates other use
    test_data = mod_dt.DataTable('random.csv', ',', col_names=col_names)
    p.log_table(test_data)
    for row in t.tbl:
        #print(row)
        p.record(test_data, '', row)
    p.build_report('test_raw_data.html', 'html')
    p.build_report('test_raw_data.rst', 'rst')
    p.build_report('test_raw_data.md', 'md')
    
    print(test_data)
    
    


main()