# coding: utf-8
# knowledge.py      written by Duncan Murray 11/3/2015

def TEST():
    """
    goal is to have a set of classes to manage the transition
    of raw data to knowledge, tapered by the bias network
    """
    print('stub for knowledge module')
    k = Knowledge('test')
    print(k)
    
    
class Knowledge():
    def __init__(self, name, type='', desc=''):
        self.nme = name
        self.type = type
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
    
 
    
class Fact():
    pass
    
class RawData():
    def __init__(self, src):
        self.data = []
        self.src = src
        
    def __str__(self):
        res = ' /---- Raw Data ------------------------------- \n' 
        res += '|  source = ' + self.src + '\n'
        for d in self.data:
            res += '|           ' + d + '\n'
        res += '\---------------------------------------------\n'
        return res
    
        
    def add(self, raw):
        """
        Add 'raw' to the raw data section
        """
        self.data.append(raw)
        
    def verify(self):
        """
        verify raw data and assign bias results
        """
        pass
        
    def process(self, dat):
        """
        take the raw data subset 'dat' and process
        into appropriate information structures
        """
        pass

        
if __name__ == '__main__':
    TEST()	