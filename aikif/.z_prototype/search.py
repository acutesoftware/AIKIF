# -*- coding: utf-8 -*-
import argparse
import aikif.config as cfg

def search(search_string):
    """ 
    main function to search using indexes 
    """
    print(('Searching for ' + search_string))
    ndxFiles = cfg.params['index_files']
    numResults = 0
    totLines = 0
    for fname in ndxFiles:
        print(("Searching " + fname))
        with open(fname, 'r') as f:
            line_num = 0
            for line_num, line in enumerate(f):
                totLines = totLines + 1
                if search_string in line:
                    try:
                        print(line)   # gives error with some encoding
                    except Exception:
                        print("Cant print search result")
                    numResults = numResults + 1
            print((str(line_num) + " lines searched"))
    print(('Found ', str(numResults), 'results in', str(totLines), 'lines over', str(len(ndxFiles)), 'index files'))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search.py looks in AIKIF index files for strings')
    parser.add_argument('-s', '--search', help='enter a search string, enclosed with quotes if multiple words needed')
    parser.add_argument('-i', '--index', help='choose an index file to search')
    args = parser.parse_args()
    search(args.search.strip(''))	
    print("REMEMBER - call this with python otherwise it doesnt run\n python search.py -s database\n")
        

    