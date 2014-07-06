# read_opencyc.py	written by Duncan Murray 	6/7/2014
# sample code to read OpenCyc files

import os
import sys

aikif_dir = os.path.dirname(os.path.abspath(__file__))
fldr = os.path.abspath(aikif_dir + os.sep + "toolbox" )

ipFolder = 'S:\\DATA\\opendata\\ontology\\OpenCyc'
opFolder = '..//..//data//'  # os.getcwd()

files = ['open-cyc.n3', 'open-cyc.rdf', 'open-cyc.trig']
lookup = ['gauge', 'mind', 'post']


print(aikif_dir)
 
def main():
    allWords = []
    num_lines = 0
    num_definitions = 0
    for f in files:
        numLines = 0
        print('Reading OpenCyc file - ', f)
        fullName = ipFolder + '\\' + f
        for line in open(fullName,'r'): 
            num_lines += 1
            if num_lines < 4:
                print(line)
        print('tot_lines = ' , num_lines)
                
if __name__ == "__main__":
	main()
