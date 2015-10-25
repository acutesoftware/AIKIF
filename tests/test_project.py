# test_project.py		written by Duncan Murray 18/2/2015

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)
import project as project
import aikif.dataTools.cls_datatable as cls_datatable
import aikif.toolbox.html_tools as mod_html

class TestProject(unittest.TestCase):

      
    def test_01_project_init(self):
        proj1 = project.Project(name='Acute Software', desc='Custom Software development', fldr='')
        proj1.add_detail('website', 'http://www.acutesoftware.com.au')
        proj1.add_detail('email', 'djmurray@acutesoftware.com.au')
        self.assertEqual(proj1.nme, 'Acute Software')
        self.assertEqual(proj1.details[0][0],'website')
        self.assertEqual(proj1.details[0][1],'http://www.acutesoftware.com.au')
        self.assertEqual(proj1.details[1][0],'email')
        self.assertEqual(proj1.details[1][1],'djmurray@acutesoftware.com.au')
        
    def test_02_record(self):
        proj2 = project.Project(name='Sales Log',  desc='Record list of sales', fldr='')
        proj2.add_detail('Note', 'List of sales taken from manual entries in test program')
        self.assertEqual(proj2.details[0][0],'Note')
        self.assertEqual(proj2.details[0][1],'List of sales taken from manual entries in test program')
        
        tbl_exp = cls_datatable.DataTable('expenses.csv', ',', col_names=['date', 'amount', 'details'])
        proj2.record(tbl_exp, 'Expense', ['2015-02-13', 49.94, 'restaurant'])
        proj2.record(tbl_exp, 'Expense', ['2015-02-15', 29.00, 'petrol'])
        proj2.record(tbl_exp, 'Expense', ['2015-02-17', 89.95, 'fringe tickets'])
        self.assertEqual(len(tbl_exp.arr), 3)
        self.assertEqual(tbl_exp.arr[1][2], 'petrol')
 
    
    def test_03_projects_init(self):
        proj_diary = project.Project(name='Diary', fldr=root_folder, desc='Diary database for PIM application')
        proj_diary.add_source('Calendar', root_folder)
        proj_diary.add_source('Bookmarks', root_folder)
        proj_diary.add_source('File Usage', root_folder)
        proj_diary.add_source('PC Usage', root_folder)
        proj_diary.add_source('TODO List', root_folder)
        self.assertEqual(len(str(proj_diary)) > 5, True)

        my_biz = project.Project(name='Acute Software', desc='Custom Software development', fldr='')
        my_biz.add_detail('website', 'http://www.acutesoftware.com.au')
        my_biz.add_detail('email', 'djmurray@acutesoftware.com.au')
        self.assertEqual(len(str(my_biz)) > 5, True)
        
        
        all_projects = project.Projects()
        all_projects.add_project(proj_diary)
        all_projects.add_project(my_biz)
        all_projects.add_ontology('mapping')
        res = all_projects.get_by_name('Diary')
        self.assertEqual(res.desc, 'Diary database for PIM application')
        
        self.assertEqual(len(all_projects.project_list), 2)
        self.assertEqual(len(str(all_projects)), 134)
   
    def test_04_project_tasks(self):
        proj04 = project.Project(name='TODO List', fldr=root_folder, desc='List of things to do')
        func = mod_html.extract_page_links
        t = project.Task(1, 'task1', func, due_date='2015-02-13', priority='High')
        proj04.add_task(t)
        print(t)
        self.assertEqual(len(proj04.tasks), 1)
        proj04.build_report('task.md', 'md')
        proj04.build_report('task.html', 'html')
        proj04.build_report('task.rst', 'rst')
        
 
    def test_11_task(self):
        p = project.Project('update Country reference', fldr='c:\test')
        func = mod_html.extract_page_links
        t1 = project.Task(1, 'task1', mod_html.extract_page_links)
        t2 = project.Task(2, 'task2', mod_html.extract_page_links)
        t3 = project.Task(3, 'task3', mod_html.extract_page_links)
        t1.add_param(param_key='url', param_val='http://www.')
        t1.add_param(param_key='dest_zip',  param_val= 'T:\\data\download\country')
        t2.add_param(param_key='tbl', param_val='S_REF_COUNTRY')
        t2.add_param('__success_test', True)

        p.add_task(t1)
        p.add_task(t2)
        p.add_task(t3)
 
        t1.execute()
        print(p)
        self.assertEqual(len(t1.params), 2)
        self.assertEqual(len(t2.params), 2)

    def test_12_task_complex_params(self):
        t12 = project.Task(1, 'task', mod_html.extract_page_links)
        t12.add_param(param_key='a_string', param_val='Hi There - this is a string')
        t12.add_param(param_key='a_number', param_val=42)
        t12.add_param(param_key='a_list', param_val=[1,2,3,7,8,9])
        t12.add_param(param_key='a_dict', param_val={'var1':'test_var1','var2':'test_var2','var3':'test_var3'})
        self.assertEqual(len(t12.params), 4)
        
        t12.add_param(param_key='mixed_dict', param_val={'var1':'test_var1','var2':['a','b','c'],'var3':6785})
        t12.add_param(param_key='deep', param_val=[7,6,5,[7,8,[{'d1':'woah'},['bb','cc'],45, 'hello']]])
        self.assertEqual(t12._force_str(t12.params[5]), '[\'deep\', [7, 6, 5, [7, 8, [{\'d1\': \'woah\'}, [\'bb\', \'cc\'], 45, \'hello\']]]]')
        self.assertEqual(str(t12.params[5]), '[\'deep\', [7, 6, 5, [7, 8, [{\'d1\': \'woah\'}, [\'bb\', \'cc\'], 45, \'hello\']]]]')
        
       
if __name__ == '__main__':
    unittest.main()