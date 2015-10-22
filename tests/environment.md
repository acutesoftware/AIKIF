#environment.md
Details on development environment, imports, code fixes todo.
Created by check_python_env.py


###Python version
3.4.3 (default, Oct 14 2015, 20:28:29) 
[GCC 4.8.4]

##Required packages
###Packages needed to be installed
pypyodbc Fail<BR>

###Packages required and already installed
os, sys, requests, codecs, re, csv, operator, datetime, xml, platform, socket, getopt, unittest, random, binascii, time, xlrd, glob, flask, json, sqlite3, string, math, getpass, subprocess, fnmatch, ctypes, ctypes<BR><BR>

##List of all imports in all modules
<BR>
cls_file as cl<BR>
web_aikif<BR>
getpass<BR>
win32com<BR>
aikif.programs as mod_prg<BR>
image_tools as cl<BR>
builtins<BR>
sys<BR>
AIKIF_utils as aikif<BR>
traceback<BR>
doctest<BR>
page_programs<BR>
aikif.dataTools.if_redis as mod_redis<BR>
aikif.toolbox.network_tools as mod_net<BR>
flask<BR>
cx_Oracle<BR>
zipfile<BR>
lzma<BR>
the tool and call the function, passing the args.<BR>
grp, pwd<BR>
sys, getopt<BR>
_md5<BR>
agent_map_data as mod_map<BR>
urllib.request<BR>
aikif.dataTools.generateTestData as mod_gen<BR>
agent_learn_aixi as mod_aixi<BR>
rdflib<BR>
aikif.toolbox.cls_grid_life as mod_grid<BR>
aikif.core_data as c<BR>
cls_log<BR>
queue<BR>
project as mod_prj<BR>
math<BR>
aikif.toolbox.image_tools as img<BR>
itertools<BR>
locale<BR>
os<BR>
nt<BR>
stat as _stat<BR>
subprocess, io<BR>
errno as _errno<BR>
__main__<BR>
weakref as _weakref<BR>
cls_log as mod_log<BR>
aikif.agents.gather.agent_email as email_agt<BR>
gc<BR>
re<BR>
page_search<BR>
ce<BR>
review_ontology<BR>
aikif.AI_CLI as mod_cli<BR>
abc<BR>
encodings<BR>
cls_context as context<BR>
sre_parse<BR>
aikif.agents.agent_map_data as mod_map<BR>
xml<BR>
aikif.examples.happiness_solver as mod_happy<BR>
weakref<BR>
urllib.parse as urlparse<BR>
aikif.lib.cls_filelist<BR>
sre_compile<BR>
lib_folder<BR>
json<BR>
functools as _functools<BR>
aikif.cls_log as mod_log    # TODO - change this before publish (prefix aikif. )<BR>
_io<BR>
aikif.run_agents as agt<BR>
cls_redis as db<BR>
aikif.environments.environment as mod_env<BR>
agent as mod_agent<BR>
aikif.toolbox.cls_grid as mod_grid #<BR>
time, os, sys<BR>
PIL<BR>
aikif.agents.agent as mod_agt<BR>
lib_file as fle<BR>
requests<BR>
glob<BR>
xml.dom.minidom<BR>
parser<BR>
zip_tools<BR>
aikif.toolbox.html_tools as mod_html<BR>
importlib<BR>
sqlite3<BR>
keyword<BR>
file_tools<BR>
linecache<BR>
cls_dataset as cl<BR>
worlds<BR>
time<BR>
heapq<BR>
aikif.lib.cls_filelist as mod_fl<BR>
aikif.mapper as mod_map<BR>
aikif.dataTools.cls_sql_code_generator as sql<BR>
dataTools.dataTools as dt<BR>
cls_file_mapping as filemap<BR>
web_utils<BR>
cls_grid as mod_grid # aikif.toolbox.<BR>
 this is no longer necessary (but code that does it still<BR>
core_data as mod_core<BR>
zlib<BR>
codecs, re<BR>
agent_explore_grid as mod_agt<BR>
_sre<BR>
aikif.config as mod_cfg<BR>
aikif.agents.aggregate.agg_context as mod_agg<BR>
aikif.dataTools.cls_datatable as mod_datatable<BR>
lib.cls_filelist as mod_fl  # Note - prefix with aikif. once deployed<BR>
base64<BR>
warnings<BR>
aikif.config as cfg<BR>
page_data<BR>
mutagenx.id3<BR>
security as sec<BR>
xml_tools<BR>
statements.append(line.strip()[7:])<BR>
urllib<BR>
cls_grid as mod_grid<BR>
???_tools<BR>
ntpath as path<BR>
stat as st<BR>
aikif.lib.cls_filelist as fl<BR>
pwd<BR>
socket<BR>
page_projects<BR>
aikif.dataTools.cls_datatable as mod_table<BR>
json as json<BR>
cls_grid_life<BR>
aikif.toolbox.data_structures as ds<BR>
sql_tools<BR>
cgi<BR>
aikif.toolbox.image_tools as mod_img<BR>
rawdata.generate<BR>
struct<BR>
cls_file_mapping as mod_filemap<BR>
text_tools<BR>
tkinter as Tkinter<BR>
page_agents as agt<BR>
fnmatch<BR>
textwrap<BR>
binascii<BR>
unittest as unittest<BR>
aikif.dataTools.if_excel as mod_xl<BR>
sys as _sys<BR>
lib_data as dat<BR>
aikif.project as mod_prj<BR>
datetime<BR>
psutil<BR>
aikif.cls_file_mapping as mod_filemap<BR>
imaplib<BR>
agents.gather.agent_filelist as agt  # Note - when deployed, prefix with aikif.<BR>
aikif.cls_collect_files as cl<BR>
aikif.toolbox.cls_grid as grd<BR>
core_data_usage<BR>
stat<BR>
mutagenx<BR>
Tkinter as Tkinter<BR>
puzzle_sliding_block as mod_puz<BR>
aikif.lib.cls_filelist as cl<BR>
smtplib<BR>
sys, os<BR>
as_util_data as dat<BR>
warnings as _warnings<BR>
aikif.environments.happiness as mod_hap_env<BR>
ctypes<BR>
redis<BR>
network_tools as mod_net<BR>
aikif.project as prj<BR>
lib.cls_filelist as mod_fl<BR>
fileMapping as filemap<BR>
__builtin__ as builtins<BR>
email<BR>
_sha512<BR>
AIKIF_utils as ai<BR>
tarfile<BR>
pypyodbc<BR>
xml.etree.ElementTree as ET<BR>
dummy_learn_1 as your_ai<BR>
shutil<BR>
bz2<BR>
xlrd as xl        # NOTE - xlrd imports fine from python shell, but this line cant find it<BR>
os, sys<BR>
logging<BR>
api_main as api<BR>
gzip<BR>
_sha1<BR>
encodings.aliases<BR>
aikif.project as project<BR>
aikif.environments.happiness as mod_env<BR>
types<BR>
token<BR>
yaml<BR>
rawdata.content<BR>
_random<BR>
aikif.dataTools.cls_datatable as cls_datatable<BR>
codecs<BR>
aikif.web_app.web_utils as web<BR>
aikif.agents.agent as agt<BR>
_hashlib<BR>
aikif.knowledge<BR>
random<BR>
unittest<BR>
bias as mod_bias<BR>
run_agents as mod_agent<BR>
_locale<BR>
functools<BR>
aikif.toolbox.data_structures as mod_dat<BR>
programs as mod_prg<BR>
io<BR>
aikif.cls_log as mod_log<BR>
locale, codecs<BR>
aikif.cls_file_mapping as filemap<BR>
cls_datatable<BR>
posixpath<BR>
aikif.toolbox.cls_grid<BR>
aikif.config<BR>
page_programs as prg<BR>
shutil as _shutil<BR>
_thread<BR>
pydoc<BR>
world_generator<BR>
cls_plan_search as mod_search<BR>
argparse<BR>
agent_image_metadata as mod_img<BR>
lib_net as net<BR>
config as mod_cfg<BR>
hashlib as _hashlib<BR>
os as _os<BR>
posixpath as path<BR>
genericpath<BR>
aikif.dataTools.cls_datatable as mod_dt<BR>
create_database<BR>
data_structures as ds<BR>
collections  # Import after _weakref to avoid circular import.<BR>
aikif.toolbox.Toolbox as mod_tool<BR>
toolbox.maths_ml_algorithms as ml<BR>
index<BR>
add<BR>
cls_collect<BR>
aikif.cls_log<BR>
_sha256<BR>
pprint<BR>
aikif.environments.worlds as my_world<BR>
cls_datatable as cl<BR>
knowledge<BR>
atexit<BR>
project as project<BR>
copy<BR>
errno<BR>
load_PC_usage as mod_usage<BR>
aikif.lib.cls_file as mod_file<BR>
builtins, sys<BR>
aikif.agents.explore.agent_explore_grid as agt<BR>
a datatable (grid) by using the schema:table:column as keys.<BR>
config as cfg<BR>
tkinter<BR>
Toolbox as mod_tool<BR>
readline<BR>
_dummy_thread as _thread<BR>
copyreg<BR>
usercustomize<BR>
aikif.lib.cls_plan_search as mod_plan<BR>
programs<BR>
tokenize<BR>
image_detection_tools as cl<BR>
csv<BR>
aikif.toolbox.audio_tools as aud<BR>
sys, errno<BR>
statements = []<BR>
page_about as abt<BR>
AIKIF_utils as aikif                 # Note - when deployed, prefix with aikif.<BR>
subprocess<BR>
collections<BR>
operator<BR>
_bootlocale<BR>
pandas as pd<BR>
config<BR>
sitecustomize<BR>
aikif.index as ndx<BR>
string<BR>
tools<BR>
mapper as mod_map<BR>
game_of_life_console as gol<BR>
aikif.install_data as inst<BR>
io as _io<BR>
sys, re<BR>
