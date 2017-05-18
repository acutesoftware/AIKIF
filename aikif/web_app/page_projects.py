# page_projects.py	written by Duncan Murray 27/5/2015
# handles the projects page for AIKIF web interface


from . import web_utils as web
import aikif.project as project
import aikif.dataTools.cls_datatable as cls_datatable
import aikif.config as mod_cfg
root_folder = mod_cfg.fldrs['log_folder']

def get_page():
    txt = ''
    projects_list = create_sample_projects()
    #txt += str(projects_list).replace('\n', '<BR>') + '<BR><BR>'
    txt += '<table border=1><tr><td>Name</td><td>Description</td><td>Folder</td></tr>'
    for p in projects_list:
        txt += '<tr>\n'
        txt += '<td>' + p.nme + '</td>\n'
        txt += '<td>' + p.desc + '</td>\n'
        txt += '<td>' + p.fldr + '</td>\n'
        txt += '</tr>\n'
    txt += '</table>\n'
    
    
    txt += web.build_edit_form('Add Project', '002', ['Project Name', 'Folder Location', 'Details'], '/projects')

    return txt
    
    
def create_sample_projects():
    proj1 = project.Project(name='Acute Software', desc='Custom Software development', fldr='')
    proj1.add_detail('website', 'http://www.acutesoftware.com.au')
    proj1.add_detail('email', 'djmurray@acutesoftware.com.au')
    proj2 = project.Project(name='Sales Log',  desc='Record list of sales', fldr='')
    proj2.add_detail('Note', 'List of sales taken from manual entries in test program')
    
    tbl_exp = cls_datatable.DataTable('expenses.csv', ',', col_names=['date', 'amount', 'details'])
    proj2.record(tbl_exp, 'Expense', ['2015-02-13', 49.94, 'restaurant'])
    proj2.record(tbl_exp, 'Expense', ['2015-02-15', 29.00, 'petrol'])
    proj2.record(tbl_exp, 'Expense', ['2015-02-17', 89.95, 'fringe tickets'])
    
    proj_diary = project.Project(name='Diary', fldr=root_folder, desc='Diary database for PIM application')
    proj_diary.add_source('Calendar', root_folder)
    proj_diary.add_source('Bookmarks', root_folder)
    proj_diary.add_source('File Usage', root_folder)
    proj_diary.add_source('PC Usage', root_folder)
    proj_diary.add_source('TODO List', root_folder)

    
    all_projects = project.Projects()
    all_projects.add_project(proj_diary)
    all_projects.add_project(proj1)
    all_projects.add_project(proj2)
    
    return all_projects
    
