# create_word_lists.py   written by Duncan Murray 3/2/2014
# creates a simple list of verbs, nouns and adjectives for 
# simple 'bag of words' parsing.
# First implementation uses the following dataset:
#     WordNet 3.1 Copyright 2011 by Princeton University.

import os
import sys
sys.path.append('S://duncan//C//user//dev//src//python//_AS_LIB')
import as_util_data as dat

ipFolder = 'S://DATA//opendata//datasets//dict//'
opFolder = 'T://user//dev//src//python//AI//'

def SaveListFirstWordOnly(msg, ipfile, opFile):
    numRecs = 0
    opList = []
    rawList = dat.ReadFileToList(ipfile)
    for line in rawList:
        if line[0:1] != ' ':
            numRecs = numRecs  + 1
            noun = line[0:line.find(' ')]
            opList.append(noun)
    dat.SaveListToFile(opList, opFile)
    print ('Saved ' + str(numRecs) + ' ' + msg)
    return numRecs
    
# ----  get the list of nouns, adverbs and adjectives ---- 
numRecs = SaveListFirstWordOnly('nouns', ipFolder + 'index.noun', opFolder + 'nounList.txt')
numRecs = SaveListFirstWordOnly('adverbs', ipFolder + 'index.adv', opFolder + 'advList.txt')
numRecs = SaveListFirstWordOnly('adjectives', ipFolder + 'index.adj', opFolder + 'adjList.txt')

# ---- get the list of verbs ---- (need some stemming here)
numRecs = 0
verbList = []
rawList = dat.ReadFileToList(ipFolder + 'index.verb')
for line in rawList:
    if line[0:1] != ' ':
        numRecs = numRecs  + 1
        verb = line[0:line.find(' ')]
        verbList.append(verb)
        verbList.append(verb + 's')  # turns play to plays  - TODO, use stemming algorithm
        verbList.append(verb + 'ed')
dat.SaveListToFile(verbList, opFolder + 'verbList.txt')    
print ('Saved ' + str(numRecs) + ' verbs')



###############################################################
##                 Build a Master Word List                  ##
###############################################################
#
# Idea is to concatenate unique words from all lists and also 
# names from contacts or baby names list (+country names, etc)
# to create one huge list of ALL words used in english sentences.
# Then, in a table each word has flags like isVerb, isNoun, isAdv,
# isAdjective, isName, isPerson, isPlace
# Once this is built then ANY sentence can be parsed into a list
# of ids instead of storing strings you store a series of numbers.





