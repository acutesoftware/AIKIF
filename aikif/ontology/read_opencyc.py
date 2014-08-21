# read_opencyc.py	written by Duncan Murray 	6/7/2014
# sample code to read OpenCyc files

import os
import sys

#ip_folder = os.path.dirname(os.path.abspath(__file__))  # leave src out of git - too big
ip_folder =  'S:\\DATA\\opendata\\ontology\\OpenCyc'
op_folder = os.path.abspath(ip_folder + os.sep + ".." + os.sep + ".." + os.sep + "data" )


print ('ip = ', ip_folder)
print ('op = ', op_folder)


files = ['open-cyc.n3', 'open-cyc.rdf', 'open-cyc.trig']
lookup = ['gauge', 'mind', 'post']


def main():
    create_html_summary()
    
    allWords = []
    num_lines = 0
    num_definitions = 0
    
    
def create_html_summary():
    txt = '<HTML><BODY>'
    for f in files:
        txt += summarise_file_as_html(f)
    txt += '</BODY></HTML>'
    
    with open('open_cyc_summary.html', 'w') as fop:
        fop.write(txt)
    print('Done')

    
def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res
    
def summarise_file_as_html(fname):
    """ 
    takes a large data file and produces a HTML summary as html
    """
    txt = '<H1>' + fname + '</H1>'
    num_lines = 0
    print('Reading OpenCyc file - ', fname)
    with open(ip_folder + os.sep + fname, 'r') as f:
        txt += '<PRE>'
        for line in f: 
            if line.strip() != '':
                num_lines += 1
                if num_lines < 80:
                    txt += str(num_lines) + ': ' + escape_html(line) + ''
        txt += '</PRE>'
        txt += 'Total lines = ' + str(num_lines) + '<BR><BR>'
    
    return txt


    
if __name__ == "__main__":
	main()
