# cls_datatable.py	written by Duncan Murray 25/6/2014

from cls_dataset import DataSet

class DataTable(object): 
    """
    A data table is a single grid of data, such as a 
    CSV / TXT file or database view or table.
    """

    def __init__(self, name, dataset_type):
        self.name = name
        self.dataset_type = dataset_type
        self.arr = []
        self.header = []
        #self.load_to_array()
        
    def __str__(self):
        res = ''
        for c in self.header:
            res += c.ljust(15) 
        res += '\n'
        for row in self.arr:
            for c in row:
                res += c.ljust(15)
            res += '\n'
        return res
    
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
                f.write(content)
    
        
    def drop(self, fname):
        """ 
        drop the table, view or delete the file
        """
        if self.dataset_type == 'file':
            import os
            try:
                os.remove(fname)
            except:
                pass
        elif self.dataset_type == 'view':
            print ("TODO - drop view")
        elif self.dataset_type == 'table':
            print ("TODO - drop table")
            
    def get_arr(self):
        return self.arr
    
    def get_header(self):
        """ returns a list of the first rows data """
        
        return self.header
        
    def add_cols(self, col_list):
        #print("BEFORE = " , self.arr)
        self.arr.extend(col_list)
        print("AFTER = " , self.arr)
        
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
        for num, c in enumerate(self.header):
            #print (num, c)
            if c == col_name:
                return num
        return 0
          
            