#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_datatable.py

#from cls_dataset import DataSet
import math
import collections

class DataTable(object): 
    """
    A data table is a single grid of data, such as a 
    CSV / TXT file or database view or table.
    
    Sample input ( test.csv)
        TERM,GENDER,ID,tot1,tot2
        5320,M,78,18,66
        1310,M,78,10,12
        1310,F,78,1,45
        1310,F,16,0,2
        1310,F,16,5,12
        5320,F,16,31,40
        1310,F,16,67,83
    >> describe_contents()
        ======================================================================
        TERM      GENDER    ID        tot1      tot2
        5320      M         78        18        66
        1310      M         78        10        12
        1310      F         78        1         45
        1310      F         16        0         2
        1310      F         16        5         12
        5320      F         16        31        40
        1310      F         16        67        83

        Table  =  5 cols x 7 rows
        HEADER =  ['TERM', 'GENDER', 'ID', 'tot1', 'tot2']
        arr    =  [['5320', 'M', '78', '18', '66'], ['1310', 'M', '78', '10', '12']]    
    """

    def __init__(self, name, dataset_type, col_names = None, delim = ','):
        self.name = name
        self.delim = delim
        self.dataset_type = dataset_type
        self.arr = []
        self.header = []
        if col_names:
            self.col_names = col_names
        else:
            self.col_names = []
            
        self.header = col_names  # possible dupe but work in progress
        #self.load_to_array()
        
    def __str__(self):
        res = ''
        for c in self.header:
            res += c.ljust(8) 
        res += '\n'
        for row in self.arr:
            for c in row:
                res += self.force_to_string(c).ljust(8) + self.delim
            res += '\n' 
        return res

    def add(self, row):
        """ add a row to data table array """
        self.arr.append(row)
        
    def describe_contents(self):
        """ describes various contents of data table """
        print('======================================================================')
        print(self)
        print('Table  = ',  str(len(self.header)) + ' cols x ' + str(len(self.arr)) + ' rows')
        print('HEADER = ', self.get_header())
        print('arr    = ', self.arr[0:2])
        #for num, itm in enumerate(self.get_header()):
        #    print('HEADER ', num, itm)
        

    def get_distinct_values_from_cols(self, l_col_list):
        """
        returns the list of distinct combinations in a dataset
        based on the columns in the list. Note that this is 
        currently implemented as MAX permutations of the combo
        so it is not guarenteed to have values in each case.
        """
        uniq_vals = []
        for l_col_name in l_col_list:
            #print('col_name: ' + l_col_name)   
            uniq_vals.append(set(self.get_col_data_by_name(l_col_name)))
            #print(' unique values = ', uniq_vals)    
        
        #print(' unique values[0] = ', uniq_vals[0])
        #print(' unique values[1] = ', uniq_vals[1])
        if len(l_col_list) == 0:
            return []
        elif len(l_col_list) == 1:
            return sorted([v for v in uniq_vals])
        elif len(l_col_list) == 2:
            res = []
            res = [(a, b) for a in uniq_vals[0] for b in uniq_vals[1]]
            return res
        else:
            print ("TODO ")
            return -44  # yes this will crash - fix this

    def count_unique_values(self, colNum, colText, topN_values=10):
        res = []
        cols = collections.Counter()
        for row in self.arr:
            cols[row[colNum]] += 1
        print (colText)
        for k,v in cols.most_common()[0:topN_values]:
            res.append( self.force_to_string(k) + ' (' +  self.force_to_string(v) + ')')

        return res
            
    def select_where(self, where_col_list, where_value_list, col_name=''):
        """ 
        selects rows from the array where col_list == val_list
        """
        res = []        # list of rows to be returned
        col_ids = []    # ids of the columns to check
        #print('select_where  : arr = ',  len(self.arr), 'where_value_list = ',  where_value_list)
        for col_id, col in enumerate(self.header):
            if col in where_col_list:
                col_ids.append([col_id, col])
        #print('select_where    : col_ids = ',  col_ids)   # correctly prints [[0, 'TERM'], [2, 'ID']]
        
        for row_num, row in enumerate(self.arr):
            keep_this_row = True
            #print('col_ids=', col_ids, ' row = ', row_num, row)
            for ndx, where_col in enumerate(col_ids):
                #print('type where_value_list[ndx] = ', type(where_value_list[ndx]))
                #print('type row[where_col[0]] = ', type(row[where_col[0]]))
                
                if row[where_col[0]] != where_value_list[ndx]:
                    keep_this_row = False
            if keep_this_row is True:
                if col_name == '':
                    res.append([row_num, row])
                else:   # extracting a single column only
                    l_dat = self.get_col_by_name(col_name)
                    if l_dat is not None:
                        res.append(row[l_dat])
        return res

    def force_to_string(self,unknown):
        result = ''
        if type(unknown) is str:
            result = unknown
        if type(unknown) is int:
            result = str(unknown)
        if type(unknown) is float:
            result = str(unknown)
        if type(unknown) is dict:
            result = '{' + self.Dict2String(unknown) + '}'
        if type(unknown) is list:
            result = '[' + ','.join([self.force_to_string(i) for i in unknown]) + ']'
        
        return result
        
    def Dict2String(self, d):
        res = ""
        for k, v in d.items(): # .iteritems():
            res = res + k + '=' + str(v) + ','
        return res

    #def dict2list(self, dct, keylist): 
    #    return [dct[i] for i in keylist]
        
    def update_where(self, col, value, where_col_list, where_value_list):
        """ 
        updates the array to set cell = value where col_list == val_list
        """
        if type(col) is str:
            col_ndx = self.get_col_by_name(col)
        else:
            col_ndx = col
        #print('col_ndx = ', col_ndx    )
        #print("updating " + col + " to " , value, " where " , where_col_list , " = " , where_value_list)
        new_arr = self.select_where(where_col_list, where_value_list)
        #print('new_arr', new_arr)
        for r in new_arr:
            self.arr[r[0]][col_ndx] = value
        
        #print(self.arr)
        
    def calc_percentiles(self, col_name, where_col_list, where_value_list):
        """ 
        calculates the percentiles of col_name 
        WHERE [where_col_list] = [where_value_list]
        """
        #col_data = self.get_col_data_by_name(col_name)
        col_data = self.select_where(where_col_list, where_value_list, col_name)
        #print('calc_percentiles: col_data = ', col_data, ' where_col_list = ', where_col_list, ', where_value_list = ', where_value_list)
        if len(col_data) == 0:
            #print("Nothing to calculate")
            return 0,0,0
        else:
            first  = self.percentile(col_data, .25)
            third  = self.percentile(col_data, .75)
            median = self.percentile(col_data, .50)
            #print('CALC_PERCENTILES =  first, third, median ',  first, third, median )
            return  first, third, median 
        
    def percentile(self, lst_data, percent , key=lambda x:x):
        """ calculates the 'num' percentile of the items in the list """
        new_list = sorted(lst_data)
        #print('new list = ' , new_list)
        #n = float(len(lst_data))
        k = (len(new_list)-1) * percent
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            #print(key(new_list[int(k)]))
            return key(new_list[int(k)])
        d0 = float(key(new_list[int(f)])) * (c-k)
        d1 = float(key(new_list[int(c)])) * (k-f)
        return d0+d1

        
    def load(self, filename):
        """
        loads a dataset to memory - usually overriden but 
        default is to load a file as a list of lines
        """
        with open(filename, "r") as f:
            return f.read()
    
    def save(self, filename, content):
        """
        default is to save a file from list of lines
        """
        with open(filename, "w") as f:
            if hasattr(content, '__iter__'):
                f.write('\n'.join([row for row in content]))
            else:
                print('WRINGI CONTWETESWREWR')
                f.write(str(content))

    def save_csv(self, filename, write_header_separately=True):
        """
        save the default array as a CSV file
        """
        txt = ''
        #print("SAVING arr = ", self.arr)
        
        with open(filename, "w") as f:
            if write_header_separately:
                f.write(','.join([c for c in self.header]) + '\n')
            for row in self.arr:
                #print('save_csv: saving row = ', row)
                txt = ','.join([self.force_to_string(col) for col in row])
                #print(txt)
                f.write(txt + '\n')
            f.write('\n')
        
    def drop(self, fname):
        """ 
        drop the table, view or delete the file
        """
        if self.dataset_type == 'file':
            import os
            try:
                os.remove(fname)
            except Exception as ex:
                print('cant drop file "' + fname + '" : ' + str(ex))
        #elif self.dataset_type == 'view':
        #    print ("TODO - drop view")
        #elif self.dataset_type == 'table':
        #    print ("TODO - drop table")
            
    def get_arr(self):
        return self.arr
    
    def get_header(self):
        """ returns a list of the first rows data """
        
        return self.header
        
    def add_cols(self, col_list):
        #print("col_list = " , len(col_list))
        #print("BEFORE = " , len(self.arr[0]))
        self.header.extend(col_list)
        for r in self.arr:
            r.extend(['0' for _ in col_list])
        #print("AFTER = " , len(self.arr[0]))
        
    def load_to_array(self):
        self.arr = []
        with open (self.name, 'r') as f:
            row = f.readline()
            self.header = [r.strip('\n').strip('"') for r in row.split(self.dataset_type)]
            #print (self.header)
            for row in f:
                if row:
                    self.arr.append([r.strip('\n').strip('"') for r in row.split(self.dataset_type)])
                #print('loading row : ', row)
        #return self.arr
        
    def get_col_by_name(self, col_name): 
        #print('get_col_by_name: col_name = ', col_name, ' self.header = ', len(self.header))
        for num, c in enumerate(self.header):
            #print (num, c)
            if c == col_name:
                #print('found = c =', c, ' num=', num)
                return num
        print(col_name, 'NOT found = returning None')
        return None
        
    def get_col_data_by_name(self, col_name, WHERE_Clause=''):
        """ returns the values of col_name according to where """
        #print('get_col_data_by_name: col_name = ', col_name, ' WHERE = ', WHERE_Clause)
        col_key = self.get_col_by_name(col_name)
        if col_key is None:
            print('get_col_data_by_name: col_name = ', col_name, ' NOT FOUND')
            return []
        #print('get_col_data_by_name: col_key =', col_key)
        res = []
        for row in self.arr:
            #print('col_key=',col_key, ' len(row)=', len(row), ' row=', row)
            res.append(row[col_key])  # need to convert to int for calcs but leave as string for lookups
        return res
 
    def format_rst(self):
        """
        return table in RST format
        """
        res = ''
        num_cols = len(self.header)
        col_width = 25
        for _ in range(num_cols):
            res += ''.join(['=' for _ in range(col_width - 1)]) + ' ' 
        res += '\n'
        for c in self.header:
            res += c.ljust(col_width) 
        res += '\n'
        for _ in range(num_cols):
            res += ''.join(['=' for _ in range(col_width - 1)]) + ' ' 
        res += '\n'
        for row in self.arr:
            for c in row:
                res += self.force_to_string(c).ljust(col_width)
            res += '\n' 
        for _ in range(num_cols):
            res += ''.join(['=' for _ in range(col_width - 1)]) + ' ' 
        res += '\n'
        return res
 
    def get_col_width(self, col_name):
        vals = self.get_col_data_by_name(col_name)
        return max([len(l) for l in vals])
        
        
class DataStats(object):
    """ class to do statistics on an array """
    def __init__(self, arr):
        self.arr = arr
                   
                   
# Utility

def TodayAsString():    
    """
    returns current date and time like oracle
    """
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
