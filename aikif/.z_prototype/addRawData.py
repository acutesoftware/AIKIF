# addRawData.py   written by Duncan Murray 3/2/2014  (C) Acute Software
# script to append raw data to the standard tables
#
# Currently hard coded, but will be expanded via separate modules to add
# raw information from file system, twitter, wikipedia, datasets

 
import os
import sys
import csv

ref_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..' + os.sep + 'data' + os.sep + 'ref')

import aikif.lib.cls_file as mod_file
import aikif.config as cfg
verbList = mod_file.TextFile(ref_folder + os.sep + 'verbList.txt').load_file_to_list()
nounList = mod_file.TextFile(ref_folder + os.sep + 'nounList.txt').load_file_to_list()
adjectiveList = mod_file.TextFile(ref_folder + os.sep + 'adjList.txt').load_file_to_list()
adverbList = mod_file.TextFile(ref_folder + os.sep + 'advList.txt').load_file_to_list()

#print(nounList)

def TEST():
    addData('duncan', 'sees', 'the lazy dog chases the faster cat')
    addData('duncan', 'sees', 'the huge horse jumps over the gate')
    addData('duncan', 'thinks', 'I have been coding for too long and need a break')
    addData('website', 'claim', 'for the past 16 years we have been helping businesses via high quality software')
    addData('website', 'question', 'How do I make a small label clickable')

    addData('duncan', 'knows', 'the cheetah is faster than man')


def addData(src, method, rawString):
    # adds the raw string to the dataset
    print(('\n' + rawString + ' (src:' + src + ', method: ' + method + ')'  ))
    n, v, a, j = parseRawString(rawString)
    print(('nouns      : ', n))
    print(('verbs      : ', v))
    print(('adverbs    : ', a))
    print(('adjectives : ', j))
    
def parseRawString(rawString):
    nouns = []
    verbs = []
    adverbs = []
    adjectives = []
    words = rawString.split(' ')
    for word in words:
        #print('word='+ word)
        for n in nounList:
            if word + '\n' == n:
                nouns.append(word)
        for v in verbList:
            if word + '\n' == v:
                verbs.append(word)
        for a in adverbList:
            if word + '\n' == a:
                adverbs.append(word)
        for j in adjectiveList:
            if word + '\n' == j:
                adjectives.append(word)
                #print('found adjective - ' + word)
    return nouns, verbs, adverbs, adjectives

# ---- main section for testing ----
print('addRawData.py - appends raw information to AIKIF')
TEST()

