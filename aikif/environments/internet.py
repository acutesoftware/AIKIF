# internet.py     written by Duncan Murray 14//5/2014

import random
import aikif.environments.environment as mod_env

def TEST():  
    e = Internet('Virtual Internet',  'Simulation of several websites')
    e.create(5)
    print(e)
    e.destroy()
    
class Internet(mod_env.Environment):
    """
    Main base class for all AIKIF environments. Example output
            1  127.0.222.159:3674  (6 pages)
            2  127.0.38.18:3218  (8 pages)
            3  127.0.164.219:3963  (6 pages)
            4  127.0.105.73:3106  (5 pages)
            5  127.0.193.200:3862  (6 pages)
    """
    def __init__(self, name, desc):
        """
        Note that the base class handles the following
        self.name = name
        self.log = aikif.cls_log.Log(aikif.config.fldrs['log_folder'])
        self.log.record_command('enviroment.py', 'Initilising base environment - ' + self.name)
        """
        super(Internet, self).__init__(name)
        self.websites = []
        self.desc = desc
    
    def __str__(self):
        res = super(Internet, self).__str__()
        res += ' Internet class \n'
        for num, w in enumerate(self.websites):
            res += str(num+1).ljust(3) + str(w) + '  (' + str(len(w.pages)) + ' pages)\n'
        return res
        
    def create(self, num_sites):
        """
        Creates the environment
        Code in Base class = self.log.record_process('enviroment.py', 'Creating environment - ' + self.name)
        """
        #super(Internet, self).create()
        print('building websites')
        for _ in range(0,num_sites):
            self.websites.append(Website())
        
    def destroy(self):
        """
        Call this when the environment is no longer needed
        Code in Base class = self.log.record_process('enviroment.py', 'Destroying environment - ' + self.name)
        """
        super(Internet, self).destroy()

class Website(object):
    """
    manage the creation of a simulated website
    """
    def __init__(self):
        self.url = '127.0.' + str(random.randint(1,255)) + '.' + str(random.randint(1,255)) + ':' + str(random.randint(3000,4000))
        self.pages = []
        
        for _ in range(0,random.randint(3,8)):
            self.pages.append(WebPage)
            
    def __str__(self):
        return self.url
    

class WebPage(object):
    """
    this is a random page in a site
    """
    def __init__(self):
        self.text = '<H1>Test</H1>this is a test'
        self.title = 'Test page'
    
    def __str__(self):
        return self.title
    
    
if __name__ == '__main__':
    TEST()    
    