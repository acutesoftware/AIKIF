#!/usr/bin/python3
# coding: utf-8
# data_content.py

import os

class DataContent(object):
    """
    Class to identify a column or table based on its content.
    
    It will use a reference table to specify known content types
    such as 
        transactions CONTAINS [ date col, amount col, desc, customer]
        web logs CONTAINS [ date, ip, file , type (OPT)]
        
    TODO
    - use the sample files on rawdata.data.samples as a starting point
    
    """
    pass