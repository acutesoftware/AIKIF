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
        
            
    def data_to_links(self, id_col_num, link_col_num):
        """
        This takes a table of data conaining a person identifier (Name or ID)
        and returns a table showing all links based on a common column 
        Ip table                  Links by Location  Links by Job 
        NAME  Location  Job
        John  Perth     Plumber   Location,Perth,John,Fred   Job,Farmer,Mary,Jane 
        Mary  Burra     Farmer    Location,Perth,John,Cindy  
        Jane  Darwin    Farmer    Location,Perth,Fred,Cindy  
        Fred  Perth     Cleaner
        Cindy Perth     Manager  
        
        So, for any link - link ALL joins. Meaning 3 people in one location
        will create 3 links of 2. This is to allow finding any one person, and
        listing all their links.
        """
        res = []
        
        # construct the header - can be done in 1 line, but clarified
        hdr_col_name = 'Cat_name'
        hdr_col_val = self.ip_data[0][link_col_num]  # gets the header 'Location'
        hdr_col_base_id = self.ip_data[0][id_col_num]  # gets the header 'NAME'
        op_hdr = [hdr_col_name,hdr_col_val,hdr_col_base_id + '_a', hdr_col_base_id + '_b']
        
        res.append(op_hdr)
        
        for row in self.ip_data[1:]:
            id_col_a = row[id_col_num]
            link_col = row[link_col_num]
            row_cat_name = hdr_col_val   # this is replicated for this links list
            
            for link_row in self.ip_data[1:]:    # find all links to this
                if link_row[link_col_num] == link_col:
                    id_col_b = link_row[id_col_num] # get the name of the other link
                    if id_col_a != id_col_b:
                        res.append([row_cat_name, link_col, id_col_a, id_col_b])
            
            # do we add the self link?
            res.append([row_cat_name, link_col, id_col_a, ''])
        return res
        
        
    def links_to_data(self, id_col_num, link_a_col_num, link_b_col_num):
        """
        This is the reverse of data_to_links and takes a links table and 
        generates a data table as follows
        Input Table                         Output Table
        Cat_Name,CAT_val,Person_a,person_b  NAME,Location  
        Location,Perth,John,Fred            John,Perth
        Location,Perth,John,Cindy           Cindy,Perth
        Location,Perth,Fred,Cindy           Fred,Perth
        """
        pass
        