#!/usr/bin/python3
# -*- coding: utf-8 -*-
# cls_data.py

import os

import aikif.cls_log as mod_log
import aikif.config as mod_cfg

lg = mod_log.Log(mod_cfg.fldrs['log_folder'])

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
        

        if self.data_type == '':
            self._identify_datatype(self.input_data)
        
        self.read_data()
        
        
        lg.record_source(self.src, 'length=' + str(self.data_length) + ', records=' + str(self.data_records))
        
        
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
        self.content['data'] = 'TODO - read CSV from ' + self.input_data
        
        lg.record_process('_create_from_csv', 'read ' + str(self.data_records) + ' from ' + self.input_data)
        
    def _create_from_owl(self):
        """
        create a standard data object based on CSV file
        """
        self.content['data'] = 'TODO - read OWL from ' + self.input_data
        
        lg.record_process('_create_from_owl', 'read ' + str(self.data_records) + ' from ' + self.input_data)
        
        
    def _create_from_url(self):
        """
        create a standard data object based on CSV file
        """
        self.content['data'] = 'TODO - read website ' + self.input_data
        lg.record_process('_create_from_url', 'read ' + str(self.data_records) + ' from ' + self.input_data)
        
        
