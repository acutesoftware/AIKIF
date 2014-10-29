# finance_example.py    written by Duncan Murray 28/10/2014

"""
This is an example showing how to map finance data to aikif


As with any domain you want to log in AIKIF you can choose any level
of detail, e.g.
Simple : annual income tax totals, reminders for bills to be paid
Medium : import log bank statements and aggregate according to rules
Complex: tracking of purchases linked to assets, auto generation of tax returns


Full
=====
objects = items purchased,
events = date purchased
locations = where bought
facts = 
"""

import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder) # TODO - remove this before publish to pypi
import cls_log as mod_log    # TODO - change this before publish (prefix aikif. )


def main():
    """
    This is the main body of the process that does the work.

    Summary:
    - load the raw data
    - read in rules list
    - create log events for AIKIF according to rules [map]
    - create new facts / reports based on rules [report]
    
    OUTPUT = 
                AIKIF mapping  : Date_of_transaction => event
                AIKIF mapping  : Amount => fact
                AIKIF mapping  : Details => location
                New column     : trans_type = DB WHERE amount > 0 ELSE CR
                summing        : details contains "CALTEX" into Travel Expense
                Done    
    
    """
    
    print('AIKIF example: Processing Finance data\n')
    data = read_bank_statements('your_statement.csv')
    maps = load_column_maps()
    rules = load_rules()
    
    for map in maps:
        print('AIKIF mapping  : ' + map[0] + ' => ' + map[1])

    for rule in rules:
        #print(rule)
        if rule[0] == 'agg':
            print('summing        : ' + rule[1] + ' into ' +  rule[2] )
        elif rule[0] == 'derive':
            print('New column     : ' + rule[1] + ' = ' + rule[2] + ' WHERE ' + rule[1] + ' ELSE ' + rule[3] )
    
    print('Done\n')
    

def read_bank_statements(fname):
    """ 
    Step 1 - Load Bank Statement
    this is normally load from CSV but put in list for example
    format is - DATE | AMOUNT  | DETAILS
    """
    return [  
    ['27-06-14',	-53.34,	"BUNNINGS 412000   MARION"],      
    ['27-06-14',	-19,   "BECKS BAKEHOUSE SP  SOMERTON PARK"],   	
    ['27-06-14',	-36.9, "NATIONAL PHARMACIES  GLENELG"],      	
    ['23-06-14',	100,    "PAYMENT RECEIVED"],                
    ['21-06-14',	-56.59, "CALTEX GLENELG NORTH GLENELG SOUTH"],
    ]

def load_column_maps():    
    """
    describe how to map the raw data and any transforms required
    this is added to AIKIF / data / ref / rules_column_maps.csv
    HEADERS (this is normally in the mapping CSV file)
    column_name  |   map_to_aikif_type  |  date_type 
    """
    return [  
    ['Date'   , 'event'   , 'date'  ],
    ['Amount' , 'fact'    , 'number'],
    ['Details', 'location', 'str'   ],
    ]
    
def load_rules():    
    """
    describe how to transform data
    this is added to AIKIF / data / ref / rules_process???.csv
    HEADERS
    type | rule_name | condition | action_if_true | action_if_false
    """
    return [  
    [ 'derive', 'trans_type', 'amount > 0' ,  'DB', 'CR'],
    [ 'agg'   , 'travel'    , 'details contains "CALTEX"', 'Travel Expense', ''],
    [ 'agg'   , 'income'    , 'details contains "RegNow" and CRDB = "DB"', 'Income', ''],
    ]
 

main()
    