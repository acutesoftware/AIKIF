# environment.py     written by Duncan Murray 9/7/2014

import os
import sys
from random import randint
import math
import aikif.cls_log 
import aikif.config

def TEST():  
    e = Environment('test', os.getcwd(), 'blah')
    e.create(40,55, 'some nice text')
    print(e)
    e.destroy()
    
class Environment(object):
    """
    Main base class for all AIKIF environments
    """
    def __init__(self, name, *arg):
        """
        when using elsewhere include the line below
        super().__init__(self, *arg)
        """
        self.name = name
        self.log = aikif.cls_log.Log(aikif.config.fldrs['log_folder'])
        self.log.record_command('enviroment.py', 'Initilising base environment - ' + self.name)
    
    def __str__(self):
        """
        when using elsewhere include the line below
        res += super().__str__(self)
        """
        res = 'Environment: ' + self.name + '\n'
        
        return res
        
    def create(self, *arg):
        """
        in your subclassed create function include the line below
        super().build(self, arg1, arg2, arg2, ...)
        """
        self.log.record_process('enviroment.py', 'Creating environment - ' + self.name)
        
    def destroy(self, *arg):
        """
        Call this when the environment is no longer needed
        in your subclassed create function include the line below
        super().destroy(self, arg1, arg2, arg2, ...)
        """
        self.log.record_process('enviroment.py', 'Destroying environment - ' + self.name)
        
  
if __name__ == '__main__':
    TEST()    
    