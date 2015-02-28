# -*- coding: utf-8 -*-
# mapper.py     written by Duncan Murray 21/10/2014


import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
#sys.path.append(root_folder)
print('mapper, root_folder = ', root_folder)
import aikif.agents.agent as agt

import aikif.cls_log as mod_log
import aikif.config as mod_cfg
import aikif.dataTools.cls_datatable as mod_datatable

column_map_file = root_folder + os.sep + 'data' + os.sep +  'ref' + os.sep + 'rules_column_maps.csv'
map_file = root_folder + os.sep + 'data' + os.sep +  'ref' + os.sep + 'mapping_rules.csv'
sample_datafile = root_folder + os.sep + 'data' + os.sep +  'raw' + os.sep + 'sample-filelist-for-AIKIF.csv'
  
class Mapper:    
    """
    Main class to map input information to aikif data structures
    based on a mapping table
    """
    
    def __init__(self):
        """
        setup that reads the table
        """
        self.load_rules()

    def __str__(self):
        res = ' -- List of Mapping Business Rules -- \n'
        for map in self.maps:
            res += str(map)
        return res

    def load_rules(self):
        """ 
        load the rules from file
        """
        self.maps = []
        #print("reading mapping table")
        with open(map_file, 'r') as f:
            for line in f:
                rule = MapRule(line)
                self.maps.append(rule)
    
    def save_rules(self):
        """ 
        load the rules to file after web updates or program changes 
        """
        with open(map_file, 'w') as f:
            for map in self.maps:
                f.write(map.format_for_file_output())
                
    def process_data(self, type, raw_data):
        """
        top level function to decide how to process 
        the raw data (which can be any format)
        """
        num_applicable_rules = 0
        formatted_data = self.format_raw_data(type, raw_data)
        for m in self.maps:
            if m.type == type:
                num_applicable_rules += 1
                self.process_rule(m, formatted_data, type)
        return num_applicable_rules
        
    def process_rule(self, m, dict, type):
        """ 
        uses the MapRule 'm' to run through the 'dict'
        and extract data based on the rule
        """
        print('TODO - ' + type + ' + applying rule ' + str(m).replace('\n', '') )
    
    def format_raw_data(self, type, raw_data):
        """
        uses type to format the raw information to a dictionary
        usable by the mapper
        """
        
        if type == 'text':
            formatted_raw_data = self.parse_text_to_dict(raw_data)
        elif type == 'file':
            formatted_raw_data = self.parse_file_to_dict(raw_data)
        else:
            formatted_raw_data = {'ERROR':'unknown data type', 'data':[raw_data]}
        return formatted_raw_data
    
    def parse_text_to_dict(self, txt):
        """ 
        takes a string and parses via NLP, ready for mapping
        """
        op = {}
        print('TODO - import NLP, split into verbs / nouns')
        op['nouns'] = txt
        op['verbs'] = txt
        
        return op
    
    def parse_file_to_dict(self, fname):
        """
        process the file according to the mapping rules.
        The cols list must match the columns in the filename
        """
        for map in self.maps:
            if map.type == 'file':
                if map.key[0:3] == 'col':
                    print('reading column..')


    def generate_map_from_dataset(self, l_dataset):
        """
        creates a map file (in the standard CSV format) based on 
        columns of a dataset. 
        1. read column names, lookup names in list
        2. read column content, get highest match of distinct values 
            from ontology lists (eg, Years, countries, cities, ages)
        """
        l_map = []
        headers = l_dataset.get_header()
        print(headers)
        for row_num, col in enumerate(headers):
            if col != '':
                l_map.append('column:name:' + str(row_num) + '=' + l_dataset.force_to_string(col))
        
        for row_num, col in enumerate(headers):
            if col != '':
                vals = l_dataset.get_distinct_values_from_cols([col])
                l_map.append('column:count:distinct:' + col + '=' + str(len(vals[0])) )
                
        for row_num, col in enumerate(headers):
            if col != '':
                col_vals = l_dataset.count_unique_values(row_num, col, 10)
                for val_num, v in enumerate(col_vals):
                    l_map.append('column:topvalues:' + col + ':' + str(val_num) + '='  + v )
                #l_map.append('column:values:top5:' + str(row_num) + '=' + col_vals)
                
                
        return l_map
        
    def create_map_from_file(self, data_filename):
        """
        reads the data_filename into a matrix and calls the main
        function '' to generate a map file
        
        For all datafiles mapped, there exists a .rule file to define it
        
        """
        
        op_filename = data_filename + '.rule'
        
        dataset = mod_datatable.DataTable(data_filename, ',')
        dataset.load_to_array()
        l_map = self.generate_map_from_dataset(dataset)
        with open(op_filename, 'w') as f:
            f.write('# rules file autogenerated by mapper.py v0.1\n')
            f.write('filename:source=' + data_filename + '\n')
            f.write('filename:rule=' + op_filename + '\n\n')
            for row in l_map:
                print('ROW = ' , row)
                if type(row) is str:
                    f.write(row + '\n')
                else:
                    for num, v in enumerate(row):
                        f.write(v)
                
            
        
def List2String(l):
	res = ""
	for v in l:
		res = res + v
	return res
        
                    
class MapRule:
    """
    manages the parsing of rules in the mapping table
    """
    def __init__(self, raw_line):
        """
        takes a raw row in the map file and extracts info
        """
        cols = raw_line.split(',')
        self.type = cols[0].strip()
        self.key = cols[1].strip()
        self.val = cols[2].strip()
    
    def __str__(self):
        """
        display a map rule to string
        """
        return self.type.ljust(15) + self.key.ljust(15) + self.val.ljust(15) + '\n'
        
    def format_for_file_output(self):
        return self.type + ',' + self.key + ',' + self.val + '\n'
 
class MapColumns:
    """
    directly maps columns in tables to aikif structures
    """
    def __init__(self, col_file):
        """
        takes a raw row in the map file and extracts info
        """
        self.col_file = col_file
        self.load_rules()
    
    def __str__(self):
        res = ' -- List of Column Mappings -- \n'
        print('self.col_file = ' + self.col_file)
        for map in self.col_maps:
            res += map
            print(map)
        return res

    def load_rules(self):
        """ 
        load the rules from file
        """
        self.col_maps = []
        #print("reading mapping table")
        with open(self.col_file, 'r') as f:
            for line in f:
                rule = line  # class to parse here?
                self.col_maps.append(rule)


        
def TEST():
    """ 
    local test function for mapper
    """
    map = Mapper()
    print(map)
    map.process_data('text', 'the cat sat on the mat')
    # use this to clean up file or AFTER web updates map.save_rules()
    map.create_map_from_file(sample_datafile)
 
    col_map = MapColumns(column_map_file)
    print(col_map)

if __name__ == '__main__':
    TEST()        