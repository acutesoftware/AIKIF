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
        
    def __str__(self):
        return self.name
    
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
            
        
            