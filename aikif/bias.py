# bias.py   written by Duncan Murray 10/10/2014
# part of AIKIF 

import os
import sys
root_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".."  )
sys.path.append(root_fldr)
import cls_log
import config as mod_cfg


def TEST():
    """
    Local self test routine - see test_bias.pt in /tests for full tests
    """
    my_bias = Bias('gov.au', 'published_data', 'abs.gov.au', '')
    print(my_bias)
    
    
class Bias:
    """
    class to give a rough weighting to a piece of information
    based on source, time, context, etc.
    This is used when automatically parsing data to ensure that
    a random comment on a forum does not get equal weighting to 
    a peer reviewed academic paper.
    There can be multiple biases, and each user can modify the 
    weights to what they deem accurate for their situation
    """
    def __init__(self, source_area, source_type, source_website, source_person):
        """ 
        passes all data on command line leave as empty string for blank
        """
        self.source_area = source_area        
        self.source_type = source_type       
        self.source_website =  source_website       
        self.source_person = source_person
        self.bias_rating = 0  # default to zero for safety - dont trust anything
        self.calculate_bias()
        
    def __str__(self):
        """ returns a string of basic inputs and outputs """
        res = 'Bias\n'
        res += 'source_area    = ' + self.source_area + '\n'
        res += 'source_type    = ' + self.source_type + '\n'
        res += 'source_website = ' + self.source_website + '\n'
        res += 'source_person  = ' + self.source_person + '\n'
        res += 'BIAS Rating    = ' + str(self.bias_rating) + '\n'
        return res
    
    def calculate_bias(self):
        """
        returns a weighting from 0 to 1 based on the sources
        Read the bias files in:
        AIKIF / data / temp / bias.csv
        AIKIF / data / temp / people.csv
        AIKIF / data / temp / websites.csv
        
        and then lookup the names and find the weightings
        
        """
        print('TODO calculating bias...')
        self.bias_rating = 0.863
        
    def get_bias_rating(self):
        return self.bias_rating
    
if __name__ == '__main__':
    TEST()
           