# finance_example.py    written by Duncan Murray 28/10/2014

"""
This is an example showing how to map finance data to aikif


As with any domain you want to log in AIKIF you can choose any level
of detail, e.g.
Simple : annual income tax totals, reminders for bills to be paid
Medium : import log bank statements and aggregate according to rules
Complex: tracking of purchases linked to assets, auto generation of tax returns


date => events
amount => facts
object => accounts
person => account paid to or recieved from


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
    """
    print('AIKIF example: Processing Finance data\n')
    data = read_bank_statements('your_statement.csv')
    maps = load_column_maps()
    rules = load_rules()
    for row in data:
        print(row)  # load this
    
    for map in maps:
        print(map['column_name'] + ' => ' + map['aikif_type'])

    for rule in rules:
        print(rule)
    
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
    """
    return [  
    {'column_id':0, 'column_name':'Date_of_transaction', 'data_type':'date', 'display':'Date','aikif_type':'event'},
    {'column_id':1, 'column_name':'Amount', 'data_type':'number', 'display':'Amount','aikif_type':'fact'},
    {'column_id':2, 'column_name':'Details', 'data_type':'str', 'display':'Details','aikif_type':'location'},
    ]
    
def load_rules():    
    """
    describe how to transform data
    this is added to AIKIF / data / ref / rules_process???.csv
    """
    return [  
    { 'type':'new_col', 'rule_name':'trans_type', 'condition':'amount > 0', 'true': 'DB', 'false':'CR'},
    { 'type':'tax_cat', 'rule_name':'travel', 'condition':'details contains "CALTEX"', 'true': 'Travel Expense', 'false':''},

    ]
 

main()
    