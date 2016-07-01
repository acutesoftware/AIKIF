#!/usr/bin/python3
import sys
import os

print ("sys.version = ", sys.version)
print ("os.getcwd() = ", os.getcwd())

#AIKIF_WEB_VERSION = "PROD"
AIKIF_WEB_VERSION = "DEV"
AIKIF_VERSION_NUM = "Version 0.1.9 (pre-alpha) - updated 22-Apr-2016"

import web_utils as web
from flask import Flask
from flask import request
    
app = Flask(__name__)
menu = [
    ['/',        'Home',     'This is the admin web interface for AIKIF (Artificial Intelligence Knowledge Information Framework)'],
    ['/todo',    'Todo',     'Project overview showing current list of tasks being worked on'],
    ['/data',    'Data',     'Shows the available data sets for AIKIF'],
    ['/projects',    'Projects',     'Manage projects'],
    ['/agents',  'Agents',   'Describes the agents capabilities, and last run status'],
    ['/programs','Programs', 'Details of the modules in AIKIF'],
    ['/about',   'About',    'About AIKIF and author contact']
    ]


###################### HELPER FUNCTIONS#################
def start_server():
    if AIKIF_WEB_VERSION == "DEV":
        print("WARNING - DEBUG MODE ACTIVE")
        app.debug = True	# TURN THIS OFF IN PRODUCTION
    app.run()

###################### ROUTING #########################

@app.route("/")
def page_home():
    txt = aikif_web_menu()
    txt += web.build_search_form()
    
    txt += "<H3>Pages on this site</h3><TABLE width=80% border=0 align=centre>\n"
    for m in menu:
        txt += '<TR><TD><a href="' + m[0] + '">' + m[1] + '</a></td><td>' + m[2] + '</td></tr>\n'
    txt += "</table><BR>\n"
    txt += "<H3>Status</h3>\n"
    txt += "Pre-Alpha stage\n"
    txt += "<BR><BR>\n"
    txt += get_footer()
    return txt

@app.route('/', methods=['POST'])
def search_post():
    return(_search(request.form['search_text']))
 
def _search(search_text):
    txt = aikif_web_menu()
    txt += web.build_search_form()
    import page_search
    txt += page_search.get_page(search_text)
    return txt



    
@app.route("/todo")
def page_todo():
    txt = aikif_web_menu('Todo')
    txt += web.build_search_form()
    txt += "<H3>Dev Tasks</h3>\n"
    txt += "<LI>implement mapping functionality of business rules</LI>\n"
    txt += "<LI>web interface to control agents, including feedback status</LI>\n"
    txt += "<LI></LI>\n"
    txt += "<H3>Data Tasks</h3>\n"
    txt += "<LI>define structures for core tables: events, people, facts, locations</LI>\n"
    txt += "<LI>define flexible structure for raw data to knowledge to learning</LI>\n"
    txt += "<LI>collect data output from existing proc_*.py needs to be properly integrated</LI>\n"
    txt += "<LI>finish function to completely import random spreadsheet</LI>\n"
    txt += "<H3>Config Tasks</h3>\n"
    txt += "<LI>setup for users to auto build database</LI>\n"
    txt += "<LI>get webserver running, deploy to restricted site</LI>\n"
    txt += "<BR><BR>\n"
    txt += get_footer()
    return txt

@app.route("/projects")
def page_projects():
    txt = aikif_web_menu('Projects')
    import page_projects
    txt += page_projects.get_page()
    txt += get_footer()
    return txt

@app.route("/data")
def page_data():
    txt = aikif_web_menu('Data')
    import page_data
    txt += page_data.get_page()
    txt += get_footer()
    return txt

@app.route("/data/<dataFile>")
def page_data_show(dataFile):
    txt = aikif_web_menu('Data')
    import page_data
    txt += page_data.get_page(dataFile)
    txt += get_footer()
    return txt
    
    

@app.route("/agents")
def page_agents():
    txt = aikif_web_menu('Agents')
    import page_agents as agt
    txt += agt.get_page()
    txt += get_footer()
    return txt


@app.route("/agents", methods=['POST'])
def edit_agents():
    res = ''
    editedinfo = []
    print('hi - about to get form values', request.form)
    #editedinfo.append(request.form['Agent Name']) # request.form['search_text']
    #editedinfo.append(request.form['Program Location'])
    #editedinfo.append(request.form['params'])
    
    for i in range(0,3):
        editedinfo.append(request.form['col_' + str(i)])
        
    #print('update-form ',   request.form['update-form'] )
    #print('add-form ',   request.form['add-form'] )
    #print('delete-form ',   request.form['delete-form'] )
    
    try:
        res = request.form['update-form']
    except:
        pass
    try: 
        res = request.form['add-form']
    except:
        pass
    try:
        res = request.form['delete-form']
    except:
        pass
    
    return res + str(editedinfo)
    
@app.route("/programs")
def page_programs():
    txt = aikif_web_menu('Programs')
    import page_programs as prg
    txt += prg.get_page()
    return txt
    
@app.route("/programs/rebuild")
def page_programs_rebuild():
    txt = aikif_web_menu('Programs')
    import page_programs as prg
    prg.rebuild()
    txt += prg.get_page()
    return txt

@app.route("/about")
def page_about():
    txt = aikif_web_menu('About')
    import page_about as abt
    txt += abt.get_page()
    txt += get_footer()
    return txt

    
def page_error(calling_page):
    txt = '<BR><BR>'
    txt += '<H2>Error - problem calling ' + calling_page + '</H2>'
    txt += get_footer()
    return txt
    
def aikif_web_menu(cur=''):
    """ returns the web page header containing standard AIKIF top level web menu """
    pgeHdg = ''
    pgeBlurb = ''
    if cur == '': 
        cur = 'Home'
    txt = get_header(cur) #"<div id=top_menu>"
    txt += '<div id = "container">\n'
    txt += '   <div id = "header">\n'
    txt += '   <!-- Banner -->\n'
    txt += '   <img src = "' + os.path.join('/static','aikif_banner.jpg') + '" alt="AIKIF Banner"/>\n'
    txt += '   <ul id = "menu_list">\n'
    for m in menu:
        if m[1] == cur:
            txt += '      <LI id="top_menu_selected"><a href=' + m[0] + '>' + m[1] + '</a></li>\n'
            pgeHdg = m[1]
            try:
                pgeBlurb = m[2]
            except Exception:
                pass
        else:
            txt += '      <LI id="top_menu"><a href=' + m[0] + '>' + m[1] + '</a></li>\n'
    txt += "    </ul>\n    </div>\n\n"
    txt += '<H1>AIKIF ' + pgeHdg + '</H1>\n'
    txt += '<H4>' + pgeBlurb + '</H4>\n'
    return txt

###################### TEMPLATES #########################

def get_header(pge=''):
    txt = '<HTML><HEAD>\n'
    txt += '<title>AIKIF:' + pge + '</title>\n'
    txt += '<!-- Stylesheets for responsive design -->\n'
    txt += '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n'
    txt += '<link rel="stylesheet" type="text/css" href="' + os.path.join('/static','aikif.css') + '" media="screen" />\n'
    txt += '<link rel="stylesheet" href="' + os.path.join('/static','aikif_mob.css')
    txt += '" media="only screen and (min-device-width : 320px) and (max-device-width : 480px)">\n'
    txt += '</HEAD>\n'
    txt += '<body>\n'
    return txt
    
def get_footer(pge=''):
    txt = '\n\n<BR><BR><BR>\n<div id="footer">\n'
    txt += pge
    txt += '<HR><a href="http://www.acutesoftware.com.au/aikif/index.html">AIKIF web interface</a> - '
    txt += 'written by Duncan Murray : djmurray@acutesoftware.com.au<BR>\n'
    txt += AIKIF_WEB_VERSION + ':' + AIKIF_VERSION_NUM + '\n'
    txt += 'Python version:' + sys.version + '\n'
    txt += '</div></BODY></HTML>\n'
    return txt

def escape_html(s):
    res = s
    res = res.replace('&', "&amp;")
    res = res.replace('>', "&gt;")
    res = res.replace('<', "&lt;")
    res = res.replace('"', "&quot;")
    return res

def format_list_as_html_table_row(lst):
    txt = '<TR>'
    for i in lst:
        txt = txt + '<TD>' + i + '</TD>'
    txt = txt + '</TR>'	
    return txt
    
def format_csv_to_html(csvFile, opHTML):
    """
    print(len(opHTML))
    with open(csvFile) as csv_file:
        for row in csv.reader(csv_file, delimiter=','):
            txt += "<TR>"
            for col in row:
                txt += "<TD>"
                txt += escape_html(col)
                txt += "</TD>"
            txt += "</TR>"
        txt += "</TABLE>"
    """
    txt = 'TODO format_csv_to_html to convert' + csvFile + ' to ' + opHTML
    return txt
    

    
if __name__ == "__main__":
    start_server()
