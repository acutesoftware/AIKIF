#!/usr/bin/python3
# coding: utf-8
# collect_pim_data.py
#
# Production example of using AIKIF to collect PIM data
# from various sources to populate the core_data database
# 

import os
import sys

# NOTE - for final release will use import aikif.name format
# but for development we will hard code paths to dev folder
root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + ".." ) 
pth = root_folder + os.sep + 'aikif'
sys.path.append(pth)
import project as prj
import core_data as mod_dat
import cls_log as mod_log
import index as mod_ndx
import knowledge as mod_know
import mapper as mod_map
import bias as mod_bias

sys.path.append(pth + os.sep + 'toolbox')
import file_tools as mod_fle
import image_tools as mod_img
import text_tools as mod_txt
import audio_tools as mod_aud

op_folder = 'T:\\user\\AIKIF\\'

p_gmail = prj.Project('Gmail', tpe='PIM', fldr='T:\\user\\AIKIF\\pers_data\\email\\gmail' , desc='Load gmail') 
p_outlook = prj.Project('Outlook', tpe='PIM', fldr='T:\\user\\AIKIF\\pers_data\\email' , desc='Load Outlook mail')  
p_file = prj.Project('File Metadata', tpe='PIM', fldr='T:\\user\\AIKIF\\pers_data\\file_metadata' , desc='Read metadata') 
p_docs = prj.Project('Documents - Local', tpe='PIM', fldr='T:\\user\\' , desc='Index documents') 
p_gdrive = prj.Project('Documents - GDrive', tpe='PIM', fldr='T:\\user\\AIKIF\\pers_data\\gdrive' , desc='Index Gdrive')
p_sites = prj.Project('Web links', tpe='PIM', fldr='T:\\user\\AIKIF\\pers_data\\gdrive' , desc='Bookmarks')   
p_ebooks = prj.Project('Ebooks', tpe='index', fldr='S:\\DATA\\eBooks' , desc='Ebooks')   
p_photos = prj.Project('Photos', tpe='PIM', fldr='P:\\' , desc='Photos') 
p_music = prj.Project('Music', tpe='PIM', fldr='M:\\' , desc='Music') 
p_diary = prj.Project('Diary', tpe='PIM', fldr='T:\\user\\AIKIF\\diary' , desc='Diary files') 
p_pcusage = prj.Project('PC Usage', tpe='PIM', fldr='T:\\user\\AIKIF\\diary' , desc='PC Usage from Infolink') 



pim_projects = prj.Projects()


pim_projects.add_project(p_gmail)
pim_projects.add_project(p_outlook)
pim_projects.add_project(p_file)
pim_projects.add_project(p_docs)
pim_projects.add_project(p_gdrive)
pim_projects.add_project(p_ebooks)
pim_projects.add_project(p_sites)
pim_projects.add_project(p_photos)
pim_projects.add_project(p_music)
pim_projects.add_project(p_diary)
pim_projects.add_project(p_pcusage)

print(pim_projects)

