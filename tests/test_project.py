# test_project.py		written by Duncan Murray 18/2/2015

import unittest
import os
import sys

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif') 
sys.path.append(root_folder)
data_tools_fldr = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." + os.sep + 'aikif' + os.sep + 'dataTools') 
sys.path.append(data_tools_fldr)
import project
import cls_datatable

class TestProject(unittest.TestCase):

      
    def test_01_project_init(self):
        proj1 = project.Project(name='Acute Software', type='business', desc='Custom Software development', fldr='')
        proj1.add_detail('website', 'http://www.acutesoftware.com.au')
        proj1.add_detail('email', 'djmurray@acutesoftware.com.au')
        self.assertEqual(proj1.nme, 'Acute Software')
        self.assertEqual(proj1.details[0][0],'website')
        self.assertEqual(proj1.details[0][1],'http://www.acutesoftware.com.au')
        self.assertEqual(proj1.details[1][0],'email')
        self.assertEqual(proj1.details[1][1],'djmurray@acutesoftware.com.au')
        
    def test_02_record(self):
        proj2 = project.Project(name='Sales Log', type='business', desc='Record list of sales', fldr='')
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

        my_biz = project.Project(name='Acute Software', type='business', desc='Custom Software development', fldr='')
        my_biz.add_detail('website', 'http://www.acutesoftware.com.au')
        my_biz.add_detail('email', 'djmurray@acutesoftware.com.au')

        
        all_projects = project.Projects()
        all_projects.add_project(proj_diary)
        all_projects.add_project(my_biz)
        
        self.assertEqual(len(all_projects.project_list), 2)
        self.assertEqual(len(str(all_projects)), 134)
   
 
      
if __name__ == '__main__':
    unittest.main()