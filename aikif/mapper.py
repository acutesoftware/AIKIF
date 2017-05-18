#!/usr/bin/python3
# -*- coding: utf-8 -*-
# mapper.py

import os
import csv
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 

import aikif.dataTools.cls_datatable as mod_datatable
from . import config as mod_cfg

data_folder = mod_cfg.core_folder + os.sep + 'aikif' + os.sep + 'data' + os.sep +  'ref'

column_map_file = data_folder + os.sep + 'rules_column_maps.csv'
map_file = data_folder + os.sep + 'mapping_rules.csv'
sample_datafile = mod_cfg.fldrs['log_folder'] + os.sep + 'sample-filelist-for-AIKIF.csv'
sample_datafile = data_folder + os.sep + 'sample-filelist-for-AIKIF.csv'
  
class Mapper(object):    
    """
    Main class to map input information to aikif data structures
    based on a mapping table
    """
    
    def __init__(self, map_file=None):
        """
        setup that reads the table
        """
        self.map_type = 'file'
        self.map_file = map_file
        self.maps = []          # list of MapRule objects
        self.load_rules()

    def __str__(self):
        res = ' -- List of Mapping Business Rules -- \n'
        for m in self.maps:
            res += str(m)
        return res

    def get_maps_stats(self):
        """
        calculates basic stats on the MapRule elements of the maps
        to give a quick overview.
        """
        tpes = {}
        for m in self.maps:
            if m.tpe in tpes:
                tpes[m.tpe] += 1
            else:
                tpes[m.tpe] = 1
        return tpes
        
    def load_rules(self):
        """ 
        load the rules from file
        """
        self.maps = []
        with open(self.map_file, 'r') as f:
            for line in f:
                if line.strip(' ')[0:1] != '#':
                    rule = MapRule(line)
                    #print('rule = ', rule)
                    self.maps.append(rule)
     
    def save_rules(self, op_file):
        """ 
        save the rules to file after web updates or program changes 
        """
        with open(op_file, 'w') as f:
            for m in self.maps:
                f.write(m.format_for_file_output())
    
    def process_raw_file(self, raw_file_name, field_names):
        """
        takes the filename to be read and uses the maps setup 
        on class instantiation to process the file.
        This is a top level function and uses self.maps which 
        should be the column descriptions (in order).
        """
        #num_outouts = 0
        dist_vals = []
        group_dat = []
        events = []
        #facts = []
        
        with open(raw_file_name) as csvfile:
            reader = csv.DictReader(csvfile, fieldnames = field_names)
            for num_lines, row in enumerate(reader):
                #print('row = =',row)
                for col_num, fld in enumerate(field_names):
                    try:
                        #print('self.maps[', col_num, '] = ', self.maps[col_num])
                        if self.maps[col_num].val == 'group_distinct':
                            group_dat.append(str(row[fld]))
                        elif self.maps[col_num].val == 'event_date':
                            events.append(str(row[fld]))

                    except Exception as ex:
                        print(('parsing error - shouldnt really be splitting using a comma anyway!', str(ex)))
        
        dist_vals = sorted(list(set(group_dat)))
        
        return num_lines, dist_vals, group_dat, sorted(list(set(events)))

    def aggregate_data(self):
        pass
    
    def identify_data(self, tpe, raw_data):
        """
        function to decide how to process 
        the raw data (which can be any format).
        Note - not 100% sure how this will be implemented
        should we pass the filename (currently takes a line)
        """
        num_applicable_rules = 0
        formatted_data = self.format_raw_data(tpe, raw_data)
        for m in self.maps:
            if m.tpe == tpe:
                num_applicable_rules += 1
                self.process_rule(m, formatted_data, tpe)
        return num_applicable_rules
        
    def process_rule(self, m, dct, tpe):
        """ 
        uses the MapRule 'm' to run through the 'dict'
        and extract data based on the rule
        """
        print(('TODO - ' + tpe + ' + applying rule ' + str(m).replace('\n', '') ))
        #print(dct)
    
    def format_raw_data(self, tpe, raw_data):
        """
        uses type to format the raw information to a dictionary
        usable by the mapper
        """
        
        if tpe == 'text':
            formatted_raw_data = self.parse_text_to_dict(raw_data)
        elif tpe == 'file':
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
        print(('TODO - parse_file_to_dict' + fname))
        for m in self.maps:
            if m.tpe == 'file':
                if m.key[0:3] == 'col':
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
        function '' to generate a  .rule file based on the data in the map
        
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
                #print('ROW = ' , row)
                if type(row) is str:
                    f.write(row + '\n')
                else:
                    for v in row:
                        f.write(v)
                
            
        
#def List2String(l):
#    res = ""
#    for v in l:
#        res = res + v
#    return res
        
                    
class MapRule(object):
    """
    manages the parsing of rules in the mapping table.
    A rule can be a classification such as
    1. File types: rule is file, [xtn], [doc_type]
    eg 
            
        file           .php           program
        file           .docx          document
        file           .htm           document
        file           .html          document
        file           .xls           data_file
        file           .xlsx          data_file    
        
    or it can be a text relationship 
        text           object         all
        text           event          all
        text           action         all
        text           relationship   all


    Column rules are currently mapped as separately (??) 
    
    """
    def __init__(self, raw_line):
        """
        takes a raw row in the map file and extracts info
        """
        
        cols = raw_line.split(',')
        self.tpe = cols[0].strip()
        self.key = cols[1].strip()
        self.val = cols[2].strip()
    
    def __str__(self):
        """
        display a map rule to string
        """
        return self.tpe.ljust(15) + self.key.ljust(15) + self.val.ljust(15) + '\n'
        
    def format_for_file_output(self):
        return self.tpe + ',' + self.key + ',' + self.val + '\n'
 
class MapColumns(object):
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
        print(('self.col_file = ' + self.col_file))
        for m in self.col_maps:
            res += str(m)
            #print(m)
        return res

    def load_rules(self):
        """ 
        load the rules from file
        """
        self.col_maps = []
        #print("reading mapping table")
        with open(self.col_file, 'r') as f:
            for line in f:
                rule = MapColumn(line)
                #rule = line
                self.col_maps.append(rule)

class MapColumn(object):
    """
    Class to manage the content of a single column map rule.
    It is designed to be re-usable for all rows in a map file,
    so instantiate it once, then call the create_from_csv_line
    to load a rule, and then use it (parse, or process).
    
    Properties of the class are:
    table
    column
    data_type
    aikif_map
    aikif_map_name
    extract
    format
    where
    index
    
    table,column,data_type,aikif_map,aikif_map_name,extract,format,where,index
    emails_sent.csv,subject,str,fact,email subject,,,,full

    """
    def __init__(self, csv_line):
        self.csv_line = csv_line
        self.cols = []
        self.table = ''
        self.column = ''
        self.data_type = ''
        self.aikif_map = ''
        self.aikif_map_name = ''
        self.extract = ''
        self.format = ''
        self.where = ''
        self.index = ''
        
        self._parse_csv_col_rules()
        
        
    def __str__(self):
        res = ' Map Column\n'
        
        res += 'table : ' + self.table + '\n'
        res += 'column : ' + self.column + '\n'
        res += 'data_type : ' + self.data_type + '\n'
        res += 'aikif_map : ' + self.aikif_map + '\n'
        res += 'aikif_map_name : ' + self.aikif_map_name + '\n'
        res += 'extract : ' + self.extract + '\n'
        res += 'format : ' + self.format + '\n'
        res += 'where : ' + self.where + '\n'
        res += 'index : ' + self.index + '\n'
        return res
        
    def extract_col(self, num):
        txt = ''
        try:
            txt = self.cols[num].strip(' ').strip('\n')
            return txt
        except Exception as ex:
            #print('cant put text into col ' , num, ' txt = ', txt, ' ', str(ex))
            # TODO - only log issues AFTER sorting out mapping validation on load
            return ''
            
    def _parse_csv_col_rules(self):
        """
        splits the CSV line of the current format and puts into 
        local class variables - mainly for testing, though this is
        not the best method long term. (TODO - fix this)
        """
        self.cols = self.csv_line.split(',')
        self.table = self.extract_col(0)
        self.column = self.extract_col(1)
        self.data_type = self.extract_col(2)
        self.aikif_map = self.extract_col(3)
        self.aikif_map_name = self.extract_col(4)
        self.extract = self.extract_col(5)
        self.format = self.extract_col(6)
        self.where = self.extract_col(7)
        self.index = self.extract_col(8)
        
        
        
    
