# coding: utf-8
# html_tools.py

from bs4 import BeautifulSoup
import aikif.toolbox.network_tools as mod_net

def TEST():
    print('html extraction tools')
    
    url = 'http://xkcd.com/292'
    raw_text = mod_net.get_web_page(url)
    links = extract_page_links(raw_text, '')
    for l in links:
        print(l)
    
    print(extract_content(mod_net.get_web_page(url)))
    
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
     
if __name__ == '__main__':
    TEST()    
    