# coding: utf-8
# html_tools.py

from bs4 import BeautifulSoup
import aikif.toolbox.network_tools as mod_net


    
def extract_page_links(rawText, searchText):    
    links = []
    soup = BeautifulSoup(rawText)
    for link in soup.findAll('a'):
        #print(link)
        l = str(link.get('href'))
        if searchText in l:
            if l != '/':
                links.append(l)
    return links    

 
def extract_by_div(raw_text, divID):
    html = ''
    soup = BeautifulSoup(raw_text)
    results = soup.find("div", {"id": divID})
    txt = results.getText()  
    print(str(len(txt)) + ' bytes read\n')
    for line in results.contents:
        html = html + str(line) + '\n'
    return html, txt
    
def extract_content(raw_text):
    return BeautifulSoup(raw_text).get_text()
