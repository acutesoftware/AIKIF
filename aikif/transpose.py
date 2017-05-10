#!/usr/bin/python3
# -*- coding: utf-8 -*-
# transpose.py

import sys
import os


class Transpose(object):
    """
    main transpose object
    """
    def __init__(self, data):
        self.ip_data = data
        self.op_data = []
    
    def __str__(self):
        return str(self.op_data)
        
    def pivot(self):
        """
        transposes rows and columns
        """
        self.op_data = [list(i) for i in zip(*self.ip_data)]
        
    def key_value_pairs(self):
        """
        convert list to key value pairs
        
        This should also create unique id's to allow for any
        dataset to be transposed, and then later manipulated
        r1c1,r1c2,r1c3
        r2c1,r2c2,r2c3
        
        should be converted to 
        ID  COLNUM  VAL
        r1c1, 
        """
        self.op_data = []
        hdrs = self.ip_data[0]
        for row in self.ip_data[1:]:
            id_col = row[0]
            for col_num, col in enumerate(row):
                self.op_data.append([id_col, hdrs[col_num], col])
        
            
        
        