# coding: utf-8
# html_tools.py

import os
import sys
from bs4 import BeautifulSoup

def TEST():
    print('html extraction tools')
    import aikif.toolbox.network_tools as mod_net
    url = 'http://xkcd.com/292'
    raw_text = mod_net.get_web_page(url)
    links = extract_page_links(raw_text, '')
    for l in links:
        print(l)
    
    print(extract_content(mod_net.get_web_page(url), ''))
    
def extract_page_links(rawText, searchText):	
    links = []
    soup = BeautifulSoup(rawText)
    for link in soup.findAll('a'):
        #print(link)
        l = str(link.get('href'))
        if searchText in l:
            a = link.attrs
            content = str(link.string)
            t = str(link.get('title'))
            if l != '/':
                links.append(l)
                #print(l)
    return links	

def extract_page_links_OLD(url, searchText):	
    links = []
    raw_text = mod_net.get_web_page(url)
    soup = BeautifulSoup(raw_text)
    for link in soup.findAll('a'):
        #print(link)
        l = str(link.get('href'))
        if searchText in l:
            a = link.attrs
            content = str(link.string)
            t = str(link.get('title'))
            links.append({'name': content, 'url': l, 'title': t, 'txt': '', 'html': '', 'catList': []})
    return links	

   
def extract_content(raw_text, divID):
	html = ''
	soup = BeautifulSoup(raw_text)
	results = soup.find("div", {"id": divID})
	txt = results.getText()  
	print(str(len(txt)) + ' bytes read\n')
	for line in results.contents:
		html = html + str(line) + '\n'
	return html, txt
    
if __name__ == '__main__':
    TEST()    
    