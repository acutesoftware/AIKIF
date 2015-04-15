# coding: utf-8
# index.py	written by Duncan Murray 19/3/2014	(C) Acute Software
# Indexes all the data in AIKIF for fast searching

import os
import sys
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(root_folder)


import aikif.cls_log as mod_log
import aikif.config as mod_cfg
import aikif.lib.cls_filelist as mod_fl

silent = 'N'
if len(sys.argv) == 2:
    if sys.argv[1] == 'Q':
        silent = 'Y'

ndxPath = mod_cfg.fldrs['public_data_path'] + os.sep +  'index'
ndxFile = ndxPath + os.sep + 'ndxFull.txt'
opIndex = ndxPath + os.sep + 'ndxWordsToFiles.txt'
ignore_files = ["__pycache__", ".git"]   
     
def index():
    """
    main function - outputs in following format BEFORE consolidation (which is TODO)
    # filename,         word,           linenumbers
    # refAction.csv,    ActionTypeName, 1
    # refAction.csv,    PhysicalType,   1
    # goals.csv,        Cleanliness,    11
    """
    lg = mod_log.Log(mod_cfg.fldrs['localPath'])
    lg.record_command('Starting indexing',  'index.py') # sys.modules[self.__module__].__file__)
    if silent == 'N':
        print('------------------')
        print('Rebuilding Indexes')
        print('------------------')	

    with open(ndxFile, "w") as ndx:
        ndx.write('filename, word, linenumbers\n')

    files_to_index = mod_fl.FileList([mod_cfg.fldrs['public_data_path'] + os.sep + 'core'], ['*.csv'], ignore_files, "files_to_index_filelist.csv")
    
    for f in files_to_index.get_list():
        buildIndex(f, ndxFile, silent)
    
    # now build the one big index file
    consolidate(ndxFile, opIndex )

    lg.record_command('Finished indexing',  'index.py')   #, fle.GetModuleName())
    if silent == 'N':
        print('Done')


def buildIndex(ipFile, ndxFile, append='Y', silent='N', useShortFileName='Y'):
    """
    this creates an index of a text file specifically for use in AIKIF
    separates the ontology descriptions highest followed by values and lastly
    a final pass to get all delimited word parts.
    """
    numWords = 0
    numWordParts = 0
    totWordCount = 0
    if silent == 'N':
        pass
    if append == 'N':
        try:
            os.remove(ndxFile)
        except:
            pass
    delims = [',', '$', '&', '"', '%', '/', '.', ';', ':', '!', '?', '-', '_', ' ', '\n', '*', '\'', '(', ')', '[', ']', '{', '}']
    # 1st pass - index the ontologies, including 2 depths up (later - TODO)
    #buildIndex(ipFile, ndxFile, ' ', 1, 'Y')

    # 2nd pass - use ALL delims to catch each word as part of hyphenated - eg AI Build py
    totWords, totLines, uniqueWords = getWordList(ipFile, delims)
    
    AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile, useShortFileName)
    if silent == 'N':
        pass
        print(os.path.basename(ipFile).ljust(30) + ' ' + str(totLines).rjust(6) + ' lines ' + str(totWords).rjust(6) + ' words ' + str(len(uniqueWords)).rjust(6) + ' unique words')
    
        #show('uniqueWords', uniqueWords, 5)
    #print(uniqueWords)  # this is now a DICTIONARY with no key names - TODO - how to save properly
    #DisplayIndexAsDictionary(uniqueWords)

def AppendIndexDictionaryToFile(uniqueWords, ndxFile, ipFile, useShortFileName='Y'):
    """ Save the list of unique words to the master list """
    if useShortFileName == 'Y':
        f = os.path.basename(ipFile)
    else:
        f = ipFile
    with open(ndxFile, "a") as ndx:
        word_keys = uniqueWords.keys()
        #uniqueWords.sort()
        for word in sorted(word_keys):
            if word != '':
                line_nums = uniqueWords[word]
                ndx.write(f + ', ' + word + ', ')
                for line_num in line_nums:
                    ndx.write(str(line_num))
                ndx.write('\n')
                
def DisplayIndexAsDictionary(word_occurrences):
    """ print the index as a dict """
    word_keys = word_occurrences.keys()
    for word in word_keys:
        line_nums = word_occurrences[word]
        print(word + " ")
        for line_num in line_nums:
            print(str(line_num) + " ")
        print("\n")

            
def show(title, lst, full=-1):
    """
    for testing, simply shows a list details
    """
    txt = title + ' (' + str(len(lst)) + ') items :\n '
    num = 0
    for i in lst:
        if full == -1 or num < full:
            if type(i) is str:
                txt = txt + i + ',\n '
            else:
                txt = txt + i + ', ['
                for j in i:
                    txt = txt + i + ', '
                txt = txt + ']\n'
        num = num + 1
    print(txt)
    
def getWordList(ipFile, delim, headersOnly='N'):
    """
    extract a unique list of words and have line numbers that word appears
    """
    indexedWords = {}
    totWords = 0
    totLines = 0
    f = open(ipFile, 'r')
    #f = open(ipFile, 'r', encoding='utf8')  # doesnt work in Python 3.4
    for line in f:
        totLines = totLines + 1
        words = multi_split(line, delim)
        totWords = totWords + len(words)
        #show('orig words', words)
        for word in words:
            cleanedWord = word.lower().strip()
            if cleanedWord not in indexedWords:
                indexedWords[cleanedWord] =  str(totLines)
            else:
                indexedWords[cleanedWord] = indexedWords[cleanedWord] + ' ' + str(totLines)
    f.close()
    #print ('total words = ' + str(len(indexedWords)))
    #show('indexedWords', indexedWords, 50)
    return totWords, totLines, indexedWords

def multi_split(txt, delims):
    """ split by multiple delimiters """
    res = [txt]
    for delimChar in delims:
        txt, res = res, []
        for word in txt:
            if len(word) > 1:
                res += word.split(delimChar)
    return res

    
def consolidate(ipFile, opFile):
    """
    make a single index file with 1 record per word which shows the word, file and linenums
        # storms, knowledge.csv - 3
        # string, rawData.csv - 1
        # structure, EVENT_SYSTEM-PC-FILE.CSV - 18, OBJECT_SYSTEM-PC-FILE.CSV - 4, sample-filelist-for-AIKIF.csv - 18 18
        # subgoal, goals.csv - 3 4 12 13 14, goal_types.csv - 8
        # subgoals, goal_types.csv - 9
        # subgoals;, goals.csv - 2
    """
    curFile = ''
    curWord = ''
    curLineNums = ''
    indexedWords = {}
    with open(ipFile, "r") as ip:
        for line in ip:
            cols = line.split(',')
            curFile = cols[0]
            curWord = cols[1]
            curLineNums = cols[2].strip()
            #DebugIndexing(curFile, curWord, curLineNums, line)
            if curWord in indexedWords:
                indexedWords[curWord] =  indexedWords[curWord] + ', ' + curFile + ' - ' + curLineNums
            else:
                indexedWords[curWord] = curFile + ' - ' + curLineNums
    with open(opFile, "w") as op:
        op.write('word, filenames\n')  # this shows which words appear in which files
        word_keys = indexedWords.keys()
        for word in sorted(word_keys):
            if word != '':
                line_nums = indexedWords[word]
                op.write(word + ', ')
                for line_num in line_nums:
                    op.write(str(line_num))
            op.write('\n')
    
 

def DebugIndexing(curFile, curWord, curLineNums, line):
    print('line = ' + line)
    print('curFile = ' + curFile)
    print('curWord = ' + curWord)
    print('curLineNums = ' + curLineNums)
    
        
if __name__ == '__main__':
    index()	
    

