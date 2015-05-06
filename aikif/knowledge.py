# coding: utf-8
# knowledge.py      written by Duncan Murray 11/3/2015

def TEST():
    """
    goal is to have a set of classes to manage the transition
    of raw data to knowledge, tapered by the bias network
    """
    print('stub for knowledge module')
    r = RawData('test')
    r.add('the dog chases the cat')
    r.add('the cat eats the fish')
    r.add('the fish is out of luck')
    print(r)
    k = Knowledge('test')
    print(k)
    
class BaseData():
    """
    TODO - base class for each of the classes to handle
    standard add/find in lists. Though may be using data
    class in dataTools
    """
    pass

    
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