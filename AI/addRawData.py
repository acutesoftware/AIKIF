# addRawData.py   written by Duncan Murray 3/2/2014  (C) Acute Software
# script to append raw data to the standard tables
#
# Currently hard coded, but will be expanded via separate modules to add
# raw information from file system, twitter, wikipedia, datasets

 
import os
import sys
import csv
sys.path.append('..//..//_AS_LIB')
import as_util_data as dat
import AIKIF_utils as aikif


verbList = dat.ReadFileToList('..//data//verbList.txt')
nounList = dat.ReadFileToList('..//data//nounList.txt')
adjectiveList = dat.ReadFileToList('..//data//adjList.txt')
adverbList = dat.ReadFileToList('..//data//advList.txt')

#print(adjectiveList)

def TEST():
    addData('duncan', 'sees', 'the lazy dog chases the faster cat')
    addData('duncan', 'sees', 'the huge horse plants a tiny flower')
    addData('website', 'claim', 'for the past 16 years we have been helping businesses via high quality software')
    addData('website', 'question', 'How do I make a small label clickable')

    addData('duncan', 'knows', 'the cheetah is faster than man')


def addData(src, method, rawString):
    # adds the raw string to the dataset
    print('\n' + rawString + ' (src:' + src + ', method: ' + method + ')'  )
    n, v, a, j = parseRawString(rawString)
    print ('nouns      : ' + dat.listToString(n, ', '))
    print ('verbs      : ' + dat.listToString(v, ', '))
    print ('adverbs    : ' + dat.listToString(a, ', '))
    print ('adjectives : ' + dat.listToString(j, ', '))
    
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

