# bias.py   written by Duncan Murray 10/10/2014
# part of AIKIF 

import os
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

sample_rawdata = {'metadata': sample_metadata, 'data':'You should develop in Python 3 instead of 2 for new projects unless you have a dependant package that only works on version 2'}
                
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
    def __init__(self, metadata):
        """ 
        passes all data on command line leave as empty string for blank
        """
        self.metadata = metadata        
        self.bias_rating = 1  # everything starts unbiased
        self.bias_details = []
        for f in bias_files:
            self._read_bias_rating(f)
        self._calculate_bias()
        
        for b in self.bias_details:
            #print(b)
            pass
            
        
    def __str__(self):
        """ returns a string of basic inputs and outputs """
        res = 'Bias\n'
        for m in self.metadata:
            res += m['label'] + ' = ' + m['value'] + '\n'
        res += 'BIAS Rating    = ' + str(self.bias_rating) + '\n'
        return res
    

    
    def _calculate_bias(self):
        """
        returns a weighting from 0 to 1 based on the sources.
        Due to fractions multiplying resulting in very small 
        numbers, adding 0.5 to bias calculations which means
        actual range is 0.5 -> 1.5 (still testing)
        """
        for m in self.metadata:
            print('METADATA : ', m)
            for b in self.bias_details:
                if  b[0] == 'bias-' + m['label'] + '.csv':
                    #print('b = ', b, 'm = ', m)
                    l_bias = 1.000
                    try:
                        l_bias = float(b[2]) + 0.5
                    except:
                        print("ERROR converting bias value to float: ", b)
                        print('bias found ', m, b)
                    self.bias_rating *= l_bias
    
        print('FINISHED - bias_rating = ', self.bias_rating)
        #self.bias_rating = 0.863
    
    def _read_bias_rating(self, short_filename):
        """
        read the bias file based on the short_filename
        and return as a dictionary
        """
        res = {}
        full_name = os.path.join(root_fldr, 'aikif', 'data', 'ref', short_filename)
        #print('reading bias file : ', short_filename, ' from ' , full_name)
        with open(full_name, 'r') as f:
            for line in f:
                bias_line = []
                cols = line.split(',')
                bias_line.extend([short_filename])
                for col in cols:
                    bias_line.extend([col.strip('"').strip('\n')])
                self.bias_details.append(bias_line)
    
    def get_bias_rating(self):
        return self.bias_rating
    
class Contraversy(object):
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
        self.topic = topic
        self.noise = 0
        self.controversy = 0
        
    def __str__(self):
        res = 'Contraversy: '
        res += self.topic 
        res += ' controversy=' + str(self.controversy) + ' noise=' + str(self.noise) + '\n'
        return res
    
    def get_contraversy(self):
        print('TODO')
        if self.topic == 'maths':
            return 0.1
        else:
            return 0.85