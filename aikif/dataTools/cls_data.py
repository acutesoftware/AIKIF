#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_data.py

import os

import aikif.cls_log as mod_log
import aikif.config as mod_cfg

#lg = mod_log.Log(mod_cfg.fldrs['log_folder'])
lg = mod_log.Log(os.getcwd())

class Data(object):
    """
    This is an experiment to provide a high level interface the 
    various data conversion functions in AIKIF and the toolbox
    methods.
    For non critical (low bias rating) information, you use this
    to scan scan large numbers of unknown data sources (e.g. twitter
    feeds, web sites) and shouldn't have to worry too much about 
    file formats / data types.
    """
    def __init__(self, input_data, name='unamed data', data_type='', src='', bias=[]):
        self.input_data = input_data
        self.content = {}
        self.name = name
        self.data_type = data_type
        self.src = src
        self.bias = bias
        self.data_records = 0
        self.data_length = 0
        self.data_length = 0
        

        if self.data_type == '':
            self._identify_datatype(self.input_data)
        
        self.read_data()
        
        
        lg.record_source(self.src, self._calc_size_stats())
        
        
    def __str__(self):
        """
        txt = self.name + ' (type=' + self.data_type + ')\n'
        txt += str(self.content)
        return txt
        """
        return str(self.content['data'])
    
    def _identify_datatype(self, input_data):
        """
        uses the input data, which may be a string, list, number
        or file to work out how to load the data (this can be 
        overridden by passing the data_type on the command line
        """
        if isinstance(input_data, (int, float)) :
            self.data_type = 'number'
        if isinstance(input_data, (list, dict)):
            self.data_type = 'list'
        elif type(input_data) is str:
            if self.input_data[0:4] == 'http':
                self.data_type = 'url'
            elif os.path.exists(input_data):
                self.data_type = 'file'
            else:
                self.data_type = 'str'
                
        lg.record_result('_identify_datatype', self.name + ' is ' + self.data_type)
    
    def read_data(self):
        if self.data_type in ['str', 'list', 'number']:
            self.content['data'] = self.input_data
        elif self.data_type == 'file':
            if self.input_data[-3:].upper() == 'CSV':
                self._create_from_csv()
            elif self.input_data[-3:].upper() == 'OWL':
                self._create_from_owl()
        elif self.data_type == 'url':
            self._create_from_url()
            
    
    def _create_from_csv(self):
        """
        create a standard data object based on CSV file
        """
       
        import aikif.dataTools.cls_datatable as cl
        fle = cl.DataTable(self.input_data, ',')
        fle.load_to_array()
        self.content['data'] = fle.arr
        
        
        lg.record_process('_create_from_csv', 'read ' + self._calc_size_stats() + ' from ' + self.input_data)
        
    def _create_from_owl(self):
        """
        create a standard data object based on CSV file
        """
        self.content['data'] = 'TODO - read OWL from ' + self.input_data
        
        lg.record_process('_create_from_owl', 'read ' + self._calc_size_stats() + ' from ' + self.input_data)
        
        
    def _create_from_url(self):
        """
        create a standard data object based on CSV file
        """
        import aikif.toolbox.network_tools as mod_net
        mod_net.download_file_no_logon(self.input_data, 'temp_file.htm')
        with open('temp_file.htm', 'r') as f:
            self.content['data'] = f.read()
        lg.record_process('_create_from_url', 'read ' + self._calc_size_stats() + ' from ' + self.input_data)
        
        
    def _calc_size_stats(self):
        """
        get the size in bytes and num records of the content
        """
        self.total_records = 0
        self.total_length = 0
        self.total_nodes = 0
        if hasattr(self.content['data'], '__iter__') and type(self.content['data']) is not str:
            self._get_size_recursive(self.content['data'])
        else:
                self.total_records += 1
                self.total_length += len(str(self.content['data']))
            
        return str(self.total_records) + ' records [or ' +  str(self.total_nodes) + ' nodes], taking ' + str(self.total_length) + ' bytes'
        
    def _get_size_recursive(self, dat):
        """
        recursively walk through a data set or json file 
        to get the total number of nodes
        """
        self.total_records += 1
        for rec in dat:
            if hasattr(rec, '__iter__') and type(rec) is not str:
                self._get_size_recursive(rec)
            else:
                self.total_nodes += 1
                self.total_length += len(str(rec))
