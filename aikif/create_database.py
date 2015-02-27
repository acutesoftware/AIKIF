# create_data_base.py
import sys, os

if sys.version[0:1] != '3':
    print ("Python Version = " + sys.version)
    print('==== WARNING - use Python 3 ======')
    exit(1)

import aikif.dataTools.cls_datatable as mod_table
from aikif.dataTools.cls_sql_code_generator import SQLCodeGenerator
import aikif.config as cfg
fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'data') 

def main():
    print('Creating database script in ' + fldr)
    make_table('CORE_EVENTS', ['id', 'name', 'key', 'value'])
    make_table('CORE_OBJECTS', ['id', 'name', 'key', 'value'])
    make_table('CORE_LOCATIONS', ['id', 'name', 'key', 'value'])
    make_table('CORE_PEOPLE', ['id', 'name', 'key', 'value'])
    make_table('CORE_FACTS', ['id', 'name', 'key', 'value'])
    make_table('CORE_PROCESSES', ['id', 'name', 'key', 'value'])
    print('Done..')
    
def make_table(tbl, cols):
    t = mod_table.DataTable(tbl, fldr + tbl + '.csv', cols)
    #t.save_csv(fldr + os.sep + tbl + '.csv')   

    # create the SQL of a file
    t = SQLCodeGenerator(tbl)
    t.set_column_list(cols)
    t.create_script_fact()
    t.create_index(tbl, cols)
    t.save_ddl(fldr + os.sep + tbl + '.sql')


if __name__ == '__main__':
    main()        