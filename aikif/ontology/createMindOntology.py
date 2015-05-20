# coding: utf-8
# createMindOntology.py		written by Duncan Murray 27/3/2014
# Script to generate a single ontology file from the OpenCog wiki



baseURL = 'http://wiki.opencog.org'
srcURL = 'http://wiki.opencog.org/w/MindOntology'
AllPagesURL = 'http://wiki.opencog.org/wikihome/index.php?title=Special:AllPages&namespace=104'

searchStringOntology = '/w/Category:MindOntology'
searchStringPages = '/w/MindOntology:'
searchStringWebText = 'mw-content-text'
searchStringCategoryLink = 'mw-normal-catlinks'

csvOutput = 'mindOntology.csv'
owlOutput = 'mindOntology.owl'  # NOT implemented properly
txtOutput = 'mindOntology.txt'
xmlOutput = 'mindOntology.xml'
subOutput = 'mindOntology_subCategory.csv'

subOntology = []
allPages = []

import urllib.request 

try:
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
 
def main():
    print('Converts OpenCog wiki pages "MindOntology" to single file')
    subOntology = ExtractPageLinks(srcURL, searchStringOntology)
    allPages = ExtractPageLinks(AllPagesURL, searchStringPages)	
    currentWebText = ''
    for p in allPages:
        fixedURL = p['url'].replace('%26', ' ')  # not needed - the actual page returned 404 anyway
        print('Reading ... ' + fixedURL)
        currentWebText = GetWebPage(fixedURL)
        if currentWebText != '404':
            p['html'], p['txt'] = ExtractContent(currentWebText, searchStringWebText)
            p['catList'] = ExtractCategoryLinks(currentWebText, searchStringCategoryLink)
    SaveAsTXT(allPages, txtOutput)
    SaveAsXML(allPages, xmlOutput)
    SaveAsOWL(allPages, owlOutput)  # not implemented
    SaveAsCSV(allPages, csvOutput)
    SaveAsCSV(subOntology, subOutput)
    print('Done')

    

def ExtractPageLinks(url, searchText):	
    links = []
    rawText = GetWebPage(url)
    soup = BeautifulSoup(rawText)
    for link in soup.findAll('a'):
        l = str(link.get('href'))
        if searchText in l:
            #a = link.attrs
            content = str(link.string)
            t = str(link.get('title'))
            links.append({'name': content, 'url': baseURL + l, 'title': t, 'txt': '', 'html': '', 'catList': []})
    return links	
    
def ExtractCategoryLinks(txt, divID):
    lCatList = []
    soup = BeautifulSoup(txt)
    textBlob = soup.find("div", {"id": divID})
    if textBlob is not None:
        for link in textBlob.findAll('a'):
            l = str(link.get('title'))
            content = str(link.string)
            #t = str(link.get('title'))       # link not needed here, as many pages dont exist (??)
            if l != 'Special:Categories':    #this is the category heading so ignore
                curCat = content.replace('(page does not exist)', '')
                #links.append({'name': content, 'url': baseURL + l, 'title': t, 'txt': '', 'html': ''})
                lCatList.append({'catList': curCat})
    return lCatList	
    
def GetWebPage(url):
    txtString = '404'
    try:
        rawText = urllib.request.urlopen(url).read()
        txtString =  str( rawText, encoding='utf8' )
    except Exception:
        pass
    return txtString

def ExtractContent(rawText, divID):
    html = ''
    soup = BeautifulSoup(rawText)
    results = soup.find("div", {"id": divID})
    txt = results.getText()   # gives results without List items
    print(str(len(txt)) + ' bytes read\n')
    for line in results.contents:
        html = html + str(line) + '\n'
    return html, txt


    
def SaveAsTXT(lst, fname):
    def formatListItemText(itm): 
        txt = '[BEGIN_ROW]\n'
        txt = txt + 'NAME: ' + itm['name'] + '\n'
        txt = txt + 'URL: ' + itm['url'] + '\n'
        txt = txt + 'TEXT: ' + itm['txt'] + '\n'
        txt = txt + 'HTML: ' + itm['html'] + '\n'
        for i in itm['catList']:
            txt = txt + 'CATEGORY: ' + str(i['catList']) + '\n'
        txt = txt + '[END_ROW]\n\n'
        #print(txt)
        return txt
    with open(fname, "w") as myfile:
        for dct in lst:
            myfile.write(formatListItemText(dct))	
            
def SaveAsCSV(lst, fname):  
    def formatListItemCSV(itm):  
        def StripLineBreaks(txt):
            # also double quotes "
            result = ''
            try:
                result = txt.replace('\n', ' ').replace('\r', ' ').replace('"', '""')
            except Exception:
                pass
            return result
        txt = '"'
        txt = txt + itm['name'] + '","'
        txt = txt + itm['url'] + '","'
        txt = txt + itm['title'] + '","'
        txt = txt + StripLineBreaks(itm['txt']) + '","'
        txt = txt + StripLineBreaks(itm['html']) + '","'
        for i in itm['catList']:
            txt = txt + str(i['catList']) + ' ; '
        txt = txt +  '"\n'
        return txt

    op = open(fname, 'w')
    op.write('"name","url","title","txt","html","catList"\n')
    for dct in lst:
        op.write(formatListItemCSV(dct))

def SaveAsXML(lst, fname):
    def formatListItemXML(itm):
        """
        def FixTextForXML(txt):
            res = txt.replace('&', '&amp;')  # must be done first
            return res.replace('"', '&quot;').replace('\'', '&apos;').replace('<', '&lt;').replace('>', '&gt;')
        """
        def StripHexChars(txt):  
            txt2 = txt.replace('\0x93', '"') 
            return txt2.replace('\0x94', '"')
        txt = '<MindOntology_Definition>\n' 
        txt = txt + '  <COL_NAME><![CDATA[' + itm['name'] + ']]></COL_NAME>\n'
        txt = txt + '  <COL_URL><![CDATA[' + itm['url'] + ']]></COL_URL>\n'
        txt = txt + '  <COL_TXT>\n<![CDATA[\n' + StripHexChars(itm['txt']) + '\n]]>\n</COL_TXT>\n'
        txt = txt + '  <COL_HTML>\n<![CDATA[\n' + StripHexChars(itm['html']) + '\n]]>\n</COL_HTML>\r\n'
        for i in itm['catList']:
            txt = txt + '  <COL_CATEGORY><![CDATA[' + str(i['catList']) + ']]></COL_CATEGORY>\n'
        txt = txt + '</MindOntology_Definition>\r\n'
        #print(FixTextForXML(txt))
        return txt

    with open(fname, "w") as op:
        op.write('<?xml version="1.0"?>' + "\n")
        op.write('<mindOntology>' + "\n")
        for l in lst:
            op.write(formatListItemXML(l))
        op.write('</mindOntology>')
                
def SaveAsOWL(lst, fname):
    def formatListItemOWL(itm):
        txt = '<RDF_ROW>\n'
        txt = txt + '  <COL_NAME>' + itm['name'] + '</COL_NAME>\n'
        txt = txt + '  <COL_URL>' + itm['url'] + '</COL_URL>\n'
        txt = txt + '  <COL_TXT>' + itm['txt'] + '</COL_TXT>\n'
        txt = txt + '  <COL_HTML>' + itm['html'] + '</COL_HTML></RDF_ROW>\r\n'
        for i in itm['catList']:
            txt = txt + '  <COL_CATEGORY>' + str(i['catList']) + '</COL_CATEGORY>\n'
        #print(txt)
        return txt
    with open(fname, "w") as op:
        op.write('<RDF>')
        for l in lst:
            op.write(formatListItemOWL(l))
        op.write('</RDF>')
    

if __name__ == '__main__':
    main()	
    
