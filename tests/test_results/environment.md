#environment.md
Details on development environment, imports, code fixes todo.
Created by check_python_env.py


###Python version
3.4.1 (v3.4.1:c0e311e010fc, May 18 2014, 10:45:13) [MSC v.1600 64 bit (AMD64)]

##Required packages
###Packages needed to be installed
pypyodbc Fail<BR>

###Packages required and already installed
os, sys, requests, codecs, re, csv, operator, datetime, xml, platform, socket, getopt, unittest, random, binascii, time, xlrd, glob, flask, json, sqlite3, string, math, getpass, subprocess, fnmatch, ctypes, ctypes<BR><BR>

##List of all imports in all modules
<BR>
lib_folder<BR>
lib.cls_filelist as mod_fl  # Note - prefix with aikif. once deployed<BR>
shutil<BR>
aikif.api_main as api  # ok, we dont *need* this, but good to get base URL<BR>
redis<BR>
rdflib<BR>
???_tools<BR>
aikif.cls_file_mapping as mod_filemap<BR>
getpass<BR>
cls_log<BR>
datetime<BR>
operator<BR>
fnmatch<BR>
tarfile<BR>
toolbox.cls_grid as mod_grid<BR>
aikif.config as mod_cfg<BR>
codecs<BR>
fileMapping as filemap<BR>
a datatable (grid) by using the schema:table:column as keys.<BR>
aikif.toolbox.cls_grid as mod_grid #<BR>
aikif.agents.agent as mod_agt<BR>
pypyodbc<BR>
aikif.dataTools.if_redis as mod_redis<BR>
lib_file as fle<BR>
requests<BR>
AIKIF_utils as aikif<BR>
aikif.environments.happiness as mod_hap_env<BR>
aikif.lib.cls_filelist<BR>
cls_datatable<BR>
dummy_learn_1 as your_ai<BR>
programs as mod_prg<BR>
collections<BR>
cls_grid as mod_grid # aikif.toolbox.<BR>
aikif.toolbox.image_tools as mod_img<BR>
random<BR>
aikif.toolbox.Toolbox as mod_tool<BR>
re<BR>
aikif.agents.agent as agt<BR>
xml<BR>
aikif.toolbox.html_tools as mod_html<BR>
urllib.request<BR>
rawdata.content<BR>
cls_plan_search as mod_search<BR>
urllib<BR>
statements = []<BR>
aikif.cls_log<BR>
sql_tools<BR>
logging<BR>
Tkinter as Tkinter<BR>
json as json<BR>
lib_data as dat<BR>
aikif.dataTools.cls_datatable as cl<BR>
aikif.agents.explore.agent_explore_grid as agt<BR>
aikif.lib.cls_filelist as fl<BR>
aikif.lib.cls_plan_search as mod_plan<BR>
json<BR>
aikif.lib.cls_context as context<BR>
config as mod_cfg<BR>
toolbox.maths_ml_algorithms as ml<BR>
page_about as abt<BR>
aikif.cls_file_mapping as filemap<BR>
aikif.web_app.web_utils as web<BR>
aikif.toolbox.data_structures as mod_dat<BR>
aikif.examples.happiness_solver as mod_happy<BR>
subprocess<BR>
image_tools as cl<BR>
pandas as pd<BR>
aikif.run_agents as agt<BR>
aikif.toolbox.cls_grid<BR>
mutagenx<BR>
file_tools<BR>
add<BR>
zipfile<BR>
unittest as unittest<BR>
argparse<BR>
page_agents as agt<BR>
lib_net as net<BR>
email<BR>
puzzle_sliding_block as mod_puz<BR>
aikif.dataTools.cls_datatable as mod_dt<BR>
page_data<BR>
review_ontology<BR>
aikif.environments.worlds as my_world<BR>
agents.gather.agent_filelist as agt  # Note - when deployed, prefix with aikif.<BR>
aikif.toolbox.cls_grid_life as mod_grid<BR>
world_generator<BR>
zip_tools<BR>
web_utils<BR>
aikif.cls_log as mod_log    # TODO - change this before publish (prefix aikif. )<BR>
tkinter as Tkinter<BR>
AIKIF_utils as ai<BR>
aikif.cls_log as mod_log<BR>
os<BR>
sqlite3<BR>
cx_Oracle<BR>
aikif.config as cfg<BR>
text_tools<BR>
index<BR>
codecs, re<BR>
aikif.dataTools.generateTestData as mod_gen<BR>
string<BR>
aikif.agents.gather.agent_email as email_agt<BR>
agent_map_data as mod_map<BR>
aikif.dataTools.cls_datatable as mod_table<BR>
data_structures as ds<BR>
psutil<BR>
csv<BR>
aikif.AI_CLI as mod_cli<BR>
aikif.knowledge as knowledge<BR>
tools<BR>
cgi<BR>
sys<BR>
aikif.agents.aggregate.agg_context as mod_agg<BR>
aikif.core_data as mod_core<BR>
xml_tools<BR>
xlrd as xl        # NOTE - xlrd imports fine from python shell, but this line cant find it<BR>
cls_collect<BR>
imaplib<BR>
page_projects<BR>
heapq<BR>
aikif.core_data as c<BR>
win32com<BR>
aikif.environments.happiness as mod_env<BR>
aikif.lib.cls_file as mod_file<BR>
cls_redis as db<BR>
sys, os<BR>
aikif.install_data as inst<BR>
aikif.dataTools.cls_datatable as cls_datatable<BR>
unittest<BR>
load_PC_usage as mod_usage<BR>
aikif.lib.cls_file as cl<BR>
os, sys<BR>
queue<BR>
aikif.toolbox.cls_grid as grd<BR>
aikif.environments.environment as mod_env<BR>
aikif.project as prj<BR>
aikif.project as project<BR>
programs<BR>
security as sec<BR>
page_programs as prg<BR>
game_of_life_console as gol<BR>
aikif.toolbox.data_structures as ds<BR>
aikif.lib.cls_filelist as cl<BR>
time<BR>
math<BR>
page_programs<BR>
dataTools.dataTools as dt<BR>
create_database<BR>
PIL<BR>
cls_file_mapping as filemap<BR>
aikif.config<BR>
core_data_usage<BR>
parser<BR>
the tool and call the function, passing the args.<BR>
agent_image_metadata as mod_img<BR>
statements.append(line.strip()[7:])<BR>
aikif.toolbox.network_tools as mod_net<BR>
socket<BR>
smtplib<BR>
gzip<BR>
xml.dom.minidom<BR>
AIKIF_utils as aikif                 # Note - when deployed, prefix with aikif.<BR>
aikif.dataTools.cls_sql_code_generator as sql<BR>
aikif.project as mod_prj<BR>
aikif.knowledge<BR>
aikif.mapper as mod_map<BR>
aikif.agents.agent as mod_agent<BR>
aikif.cls_collect_files as cl<BR>
urllib.parse as urlparse<BR>
mutagenx.id3<BR>
time, os, sys<BR>
base64<BR>
flask<BR>
web_aikif<BR>
aikif.dataTools.cls_dataset as cl<BR>
aikif.dataTools.cls_datatable as mod_datatable<BR>
cls_grid_life<BR>
aikif.agents.agent_map_data as mod_map<BR>
glob<BR>
tkinter<BR>
page_search<BR>
binascii<BR>
aikif.programs as mod_prg<BR>
worlds<BR>
project as project<BR>
xml.etree.ElementTree as ET<BR>
rawdata.generate<BR>
as_util_data as dat<BR>
aikif.toolbox.image_tools as img<BR>
ctypes<BR>
Toolbox as mod_tool<BR>
bias as mod_bias<BR>
pprint<BR>
aikif.toolbox.audio_tools as aud<BR>
aikif.dataTools.if_excel as mod_xl<BR>
aikif.lib.cls_filelist as mod_fl<BR>
agent_learn_aixi as mod_aixi<BR>
aikif.index as ndx<BR>
