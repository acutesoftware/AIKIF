#!/usr/bin/python3
# coding: utf-8
# html_tools.py

from bs4 import BeautifulSoup


def extract_page_links(rawText, searchText):
    links = []
    soup = BeautifulSoup(rawText, "html.parser")
    for link in soup.findAll('a'):
        #print(link)
        l = str(link.get('href'))
        if searchText in l:
            if l != '/':
                links.append(l)
    return links


def extract_by_div(raw_text, divID):
    html = ''
    soup = BeautifulSoup(raw_text, "html.parser")
    results = soup.find("div", {"id": divID})
    txt = results.getText()
    #print(str(len(txt)) + ' bytes read\n')
    for line in results.contents:
        html = html + str(line) + '\n'
    return html, txt

def extract_content(raw_text):
    return BeautifulSoup(raw_text, "html.parser").get_text()

#html, txt = extract_by_div('<DIV id=aa>div aa</DIV>blah blah', 'aa')
#print(html, txt)
