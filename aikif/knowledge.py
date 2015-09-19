#!/usr/bin/python3
# coding: utf-8
# knowledge.py


    
class Knowledge(object):
    def __init__(self, name, tpe='', desc=''):
        self.nme = name
        self.type = tpe
        self.desc = desc
        self.core = []
        self.rules = []
        self.bias = []
        

    def __str__(self):
        res = ' /---- Knowledge ------------------------------- \n' 
        res += '|  name = ' + self.nme + '\n'
        res += '|  desc = ' + self.desc + '\n'
        res += '|  type = ' + self.type + '\n'
        res += '\---------------------------------------------\n'
        return res
    
 
    
class Fact(object):
    def verify(self):
        """
        verify raw data and assign bias results
        """
        print('TODO - Fact.verify not yet implemented')
        return True
        
    def process(self, dat):
        """
        take the raw data subset 'dat' and process
        into appropriate information structures
        """
        print('TODO - Fact.process not yet implemented')
        return True
    
class RawData(object):
    def __init__(self, src):
        self.data = []
        self.src = src
        
    def __str__(self):
        res = 'raw_data: ' + self.src + ' (' + str(len(self.data)) + ' entries)\n'
        for num, d in enumerate(self.data):
            res +=  str(num+1).ljust(3) + ' ' + d + '\n'
        return res
    
        
    def add(self, raw):
        """
        Add 'raw' to the raw data section
        """
        self.data.append(raw)
    
    def find(self, txt):
        """
        returns a list of records containing text
        """
        result = []
        for d in self.data:
            if txt in d:
                result.append(d)
        return result
        

