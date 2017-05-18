# read_wordnet.py	written by Duncan Murray 	12/4/2014
# sample code to read a WordNet file

ipFolder = 'S:\\DATA\\opendata\\ontology\\WordNet\\dict'
opFolder = '..//..//data//'  # os.getcwd()

files = ['data.noun', 'data.verb']
lookup = ['gauge', 'mind', 'post']
 
def main():
    allWords = []
    for f in files:
        numLines = 0
        print(('Reading WordNet file - ', f))
        fullName = ipFolder + '\\' + f
        for line in open(fullName,'r'): 
            if line[0:2] != '  ':
                ndx, words = ParseLine(line)
                # works sort of rec = [f, ndx, [w for w in words]]
                for w in words:
                    rec = [f, ndx, w, line]
                    allWords.append(rec)
                    numLines = numLines + 1
                    if numLines < 40:
                        #print(line[0:75] + '...')
                        #print('ndx=', ndx, '  words = ', words)
                        #print(rec)
                        pass
            
        print(('Finished reading ' + str(numLines) + ' lines\n'))
    print(('allWords = ', str(len(allWords))))
    # Do a lookup
    for i in lookup:
        results = Lookup(i, allWords)
        for r in results:
            print(r)
            print(('Result for ' + i + ' - ' + r[0] + ' ' + r[1] + '\n ' , r[2], '\n'))

    # TESTING - show lines for index
    PrintLineForIndex('00469029', allWords)
    PrintLineForIndex('05619057', allWords)
    PrintLineForIndex('01033142', allWords)
    
def Lookup(txt, wrdList):
    res = []
    for i in wrdList:
        src = i[0]
        ndx = i[1]
        for wrd in i[2]:
            if txt == wrd:
                res.append([src, ndx, wrd])
                res.append([src, ndx, GetWordForIndex(ndx, wrdList)])
    return res

    
def GetWordForIndex(ndxToFind, lst):
    wrdResult = []
    for i in lst:
        src = i[0]
        ndx = i[1]
        if ndxToFind == ndx:
            for wrd in i[2]:
                wrdResult.append([src, ndx, wrd])
    
    
    return wrdResult

def PrintLineForIndex(i, wrdList):
    print(('looking for index - ', i))
    for line in wrdList:  # bug here - TODO
        if i in line:
            print(line)
            print(('found index ' , i[0:40], '\n'))
    
def ParseLine(line):
    wrds = []
    cols = line.split(' ')
    ndx = cols[0]
    #print(line)
    numWords = int(cols[3], 16)
    for i in range(numWords):
        wrds.append(cols[5+i-1])
        
    #if numWords > 10:
        #print (line)
    return ndx, wrds

        
if __name__ == '__main__':
    main()	
