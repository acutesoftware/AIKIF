# raw_data_test.py

import os
import aikif.project as mod_prj
import aikif.dataTools.cls_datatable as mod_dt
import rawdata.generate
import rawdata.content

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
    t = rawdata.generate.TableGenerator(50, col_types, col_names)
    
    
    # save the table (you can save it via rawdata class, but demonstrates other use
    test_data = mod_dt.DataTable('random.csv', ',', col_names=col_names)
    p.log_table(test_data)
    for row in t.tbl:
        #print(row)
        p.record(test_data, '', row)
    p.build_report('test_raw_data.rst', 'rst')
    
    print(test_data)
    
    


main()