# -*- coding: utf-8 -*-
# read_opencyc.py	written by Duncan Murray 	6/7/2014
# sample code to read OpenCyc files

import os
import sys
import redis

#ip_folder = os.path.dirname(os.path.abspath(__file__))  # leave src out of git - too big
ip_folder =  'S:\\DATA\\opendata\\ontology\\OpenCyc'
op_folder = os.path.abspath(ip_folder + os.sep + ".." + os.sep + ".." + os.sep + "data" )


print ('ip = ', ip_folder)
print ('op = ', op_folder)


#files = ['open-cyc.n3', 'open-cyc.rdf', 'open-cyc.trig']
files = ['open-cyc.n3.csv']
#files = ['open-cyc_sample.n3.csv']
lookup = ['gauge', 'mind', 'post']


def main():
    #create_html_summary()
    load_data(ip_folder + os.sep + files[0])
    allWords = []
    num_lines = 0
    num_definitions = 0
    

def load_data(fname):
    """ loads previously exported CSV file to redis database """
    print('Loading ' + fname + ' to redis')
    r = redis.StrictRedis(host = '127.0.0.1', port = 6379, db = 0);
    with open(fname, 'r') as f:
        for line_num, row in enumerate(f): 
            if row.strip('') != '':
                if line_num < 100000000:
                    l_key, l_val = parse_n3(row, 'csv')
                    if line_num % 1000 == 0: 
                        print('loading line #', line_num, 'key=', l_key, ' = ', l_val)
                    if l_key != '':
                        r.set(l_key, l_val)

def parse_n3(row, src='csv'):
    """ 
    takes a row from an n3 file and returns the triple
    NOTE - currently parses a CSV line already split via
    cyc_extract.py
    """
    if row.strip() == '':
        return '',''
    l_root = 'opencyc'
    key = ''
    val = ''
    if src == 'csv': 
        cols = row.split(',')
        if len(cols) < 3:
            #print('PARSE ISSUE : ', row)
            return '',''
        key = ''
        val = ''
        key = l_root + ':' + cols[1].strip('"').strip() + ':' + cols[2].strip('"').strip()
        try:
            val = cols[3].strip('"').strip()
        except:
            val = "Error parsing " + row
    elif src == 'n3':
        pass
    return key, val
    
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
