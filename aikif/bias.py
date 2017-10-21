# bias.py   written by Duncan Murray 10/10/2014
# part of AIKIF 

import os
#import logging
#logging.basicConfig(filename='test_bias.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
import cls_log
from decorators import debug

root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  )

bias_files = [  'bias-website.csv', 
                'bias-source-type.csv', 
                'bias-person-reputation.csv', 
                'bias-person-relationship.csv', 
                'bias-collection-method.csv',
]

sample_metadata = [
    {'label':'collection-method', 'value': 'website'},
    {'label':'website', 'value': 'reddit.com'},
    {'label':'person', 'value': 'acutesoftware'},
    {'label':'reputation', 'value': 'logged in user'},
    {'label':'time', 'value': 'recent'},
    {'label':'relationship', 'value': 'self'},
    {'label':'source-type', 'value': 'comment'},
    
]

sample_rawdata = {  'metadata': sample_metadata, 
                    'data':'You should develop in Python 3 instead of 2 for new projects unless you have a dependant package that only works on version 2'}

lg = cls_log.Log(os.getcwd())
lg.record_process('bias.py', 'starting bias.py')


bias_schema = open(os.path.join(root_fldr, 'aikif', 'bias.schema'), 'r').readlines()
print(bias_schema)

                
class Bias(object):
    """
    class to give a rough weighting to a piece of information
    based on source, time, context, etc.
    This is used when automatically parsing data to ensure that
    a random comment on a forum does not get equal weighting to 
    a peer reviewed academic paper.
    There can be multiple biases, and each user can modify the 
    weights to what they deem accurate for their situation.
    
    Parameters:
        sources [] = list of sources, all optional. This comes 
                     from the 'data' metadata and can contain 
                     website, type, person-reputation, person-relationship,
                     collection_method
    Public functions:
        get_bias_rating() = returns the bias rating 0=bullshit -> 1=fact
        
    """
    @debug
    def __init__(self, metadata):
        """ 
        passes all data on command line leave as empty string for blank
        """
        self.metadata = metadata        
        self.bias_rating = 1  # everything starts unbiased
        lg.record_process('bias.py', 'init bias class')

        self.bias_details = []
        for f in bias_files:
            self._read_bias_rating(f)
        self._calculate_bias()
        lg.record_process('bias.py', 'bias rating = ' + str(self.bias_rating) + ' for ' + str(self.metadata))

    def __str__(self):
        """ 
        returns a string of basic inputs and outputs 
        """
        res = 'Bias\n'
        for m in self.metadata:
            res += m['label'] + ' = ' + m['value'] + '\n'
        res += 'BIAS Rating    = ' + str(self.bias_rating) + '\n'
        return res
    
    def get_bias_details(self):
        """
        returns a string representation of the bias details
        """
        res = 'Bias File Details\n'
        for b in self.bias_details:
            if len(b) > 2:
                res += b[0].ljust(35)
                res += b[1].ljust(35)
                res += b[2].ljust(9)
            res += '\n'
        return res
        
    def _calculate_bias(self):
        """
        returns a weighting from 0 to 1 based on the sources.
        Due to fractions multiplying resulting in very small 
        numbers, adding 0.5 to bias calculations which means
        actual range is 0.5 -> 1.5 (still testing)
        
        Note - range should be from 0 - > 1
        
        """
        for m in self.metadata:
            for b in self.bias_details:
                if  b[0] == 'bias-' + m['label'] + '.csv':
                    l_bias = 1.000
                    try:
                        l_bias = float(b[2]) + 0.5
                    except:
                        lg.record_process('bias.py','ERROR converting bias value to float: ' + str(b))
                    self.bias_rating *= l_bias
    
    #@debug
    def _read_bias_rating(self, short_filename):
        """
        read the bias file based on the short_filename
        and return as a dictionary
        """
        res = {}
        full_name = os.path.join(root_fldr, 'aikif', 'data', 'ref', short_filename)
        lg.record_process('bias.py','reading ' + full_name)
         
        with open(full_name, 'r') as f:
            for line in f:
                if line.strip('') == '':
                    break
                bias_line = []
                cols = line.split(',')
                bias_line.extend([short_filename])
                for col in cols:
                    bias_line.extend([col.strip('"').strip('\n')])
                self.bias_details.append(bias_line)
    
    def get_bias_rating(self):
        return self.bias_rating

        
class Controversy(object):
    """
    class to handle and report on controversial topics so 
    that it can be added as a value to bias calculations.
    
    The outcome is a value from:
        0 (universally agreed) to
        1 (everyone argues about it)
    There is also a 'noise' rating for a topic, also a value
        0 = no one is talking about it
        1 = everyone talks about it
        
    Controversies should be time stamped so that the values
    can be factored accordingly.
    
    """
    
    def __init__(self, topic):
        """
        testing reading noise by topic from external file
        {
        'topic'      : ['maths', 'physics', 'economics', 'politics', 'religion'], 
        'controversy': ['0.01',  '0.012',   '0.4',       '0.85',     '0.95'], 
        'noise'      : ['0.1',   '0.2',     '0.3',       '0.9',      '0.9']
         }        
        
        Once all topics are loaded, the key 'topic' passed as on initialisation
        is used to find the controversy and noise
        
        """
        self.topic = topic
        self.topics = []
        
        import csv
        full_name = os.path.join(root_fldr, 'aikif', 'data', 'ref', 'bias_by_topic.csv')
        with open(full_name, 'r') as fin:
            reader = csv.reader(fin)
            for num, r in enumerate(reader):
                self.topics.append({'name':r[0], 'controversy':float(r[1]), 'noise':float(r[2])})
        
        self.controversy = self.get_controversy('controversy')
        self.noise = self.get_controversy('noise')
        
    def __str__(self):
        res = 'Controversy: '
        res += self.topic 
        res += ' controversy=' + str(self.controversy) + ' noise=' + str(self.noise) + '\n'
        return res
    
    def get_controversy(self, item='controversy'):
        for t in self.topics:
            if t['name'] == self.topic:
                return t[item]
        return 0    
    

            
