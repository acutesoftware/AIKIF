# test_cls_file.py     written by Duncan Murray 22/6/2014
# unit testing for collection class

import unittest
import os
import sys
import csv
import datetime

root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + ".." ) 
sys.path.append(root_folder + os.sep + 'aikif' + os.sep + 'lib' )

import cls_file as cl
 
img_file = root_folder + os.sep + 'doc' + os.sep + 'AIKIF-Overview.jpg'


  
class TestClassFile(unittest.TestCase):
 
    def setUp(self):
        self.fname = 'test_results' + os.sep + 'cls_file_test_data.txt'
        self.fname = 'cls_file_test_data.txt'

    def test_01_file_create(self):
        self.assertEqual(1, 1)  # dummy
        f = cl.TextFile(self.fname)
        f.delete()
        f.append_text('# test file for cls_file\n')
        f.append_text('this is the 2nd line\n')
        f.append_text('this is the last line\n')
        
    def test_02_file_print(self):
        f = cl.File(self.fname)
        self.assertTrue(len(str(f)) > 5)

    def test_03_file_load_string(self):
        f = cl.TextFile(self.fname)
        txt = f.load_file_to_string()
        self.assertEqual(len(txt), 68) 
        
        # now try with a dud file
        f_dud = cl.TextFile('blahdfgkjdlfgkjldkfgj.txt')
        self.assertEqual(f_dud.load_file_to_string(), '')
        

    def test_04_file_load_list(self):
        f = cl.TextFile(self.fname)
        lst = f.load_file_to_list()
        self.assertEqual(len(lst), 3) 
        # now try with a dud file
        f_dud = cl.TextFile('blahdfgkjdlfgkjldkfgj.txt')
        self.assertEqual(len(f_dud.load_file_to_string()), 0)
        
  
    def test_06_launch(self):
        f = cl.File(self.fname)
        #self.assertTrue(f.launch())  # TODO - enable this, but change to be non modal 
        self.assertEqual(str(f)[0:20], '====================')
        



    def test_07_get_file_sample(self):
        f = cl.TextFile(self.fname)
        self.assertTrue(len(str(f)) > 10)
        sample = f.get_file_sample(2)
        self.assertEqual(len(sample.split('\n')) - 1, 2)

    def test_08_convert_to_csv(self):
        chr31_delimited_data = """D20130611000920130611PCFile0122 15UsageFacebook - Google Chrome
D20130611001020130611PCFile0123 1UsageGoogle - Google Chrome
D20130611001120130611PCFile0400 61UsageDesktop
D20130611001220130611PCFile0500 60UsageDesktop
"""
        with open('chr31_delimited_data_file.dat', 'w') as d:
            d.write(chr31_delimited_data)
            
        f = cl.TextFile('chr31_delimited_data_file.dat')
        #self.assertEqual(f.get_file_sample(1), '00000 D20130611000920130611PCFile0122 15UsageFacebook - Google Chrome')
        
        f.convert_to_csv('chr31_delimited_data_file.csv', chr(31))
        
        f_csv = cl.TextFile('chr31_delimited_data_file.csv')
        self.assertEqual(f_csv.get_file_sample(1), '00000 "D201306110009","20130611","PCFile","0122"," 15","Usage","","","","","","","","","Facebook - Google Chrome",""\n')
    
    def test_09_date_as_string(self):
        f = cl.File('chr31_delimited_data_file.dat')
        dte_ok = f.date_modified
        self.assertEqual(len(f.GetDateAsString(dte_ok)), 19)
        self.assertEqual(len(f.GetDateAsString('this is not a date')), 0)
        #dte2 = datetime.datetime.strptime('201603031230','%Y%m%d%H%M') # datetime.datetime(2016, 3, 3, 12, 30)
        #print('dte2 = ', dte2)
        #self.assertEqual(f.GetDateAsString(dte2)[0:11], '2016-03-03')

    def test_10_count_line_in_file(self):
        t = cl.TextFile('chr31_delimited_data_file.csv')
        self.assertEqual(t.count_lines_in_file(), 4)
        
        # check for non file
        self.assertEqual(t.count_lines_in_file('no such filename'), 0)
    
    
    def test_11_get_file_sample(self):
        t11 = cl.TextFile(self.fname)
        self.assertEqual(t11.get_file_sample(1), '00000 # test file for cls_file\n')
        self.assertEqual(len(t11.get_file_sample(999)), 86)  # returns full sample file
 

    def test_20_image_file(self):
        i = cl.ImageFile(img_file)
        self.assertTrue(len(str(i)) > 200)
        
    def test_30_audio_file(self):
        """ test will only pass locally """
        song = r"E:\backup\music\Music\_Rock\Angels\Red Back Fever\07 Red Back Fever.mp3"
        if(os.path.exists(song)):
            try:
                a = cl.AudioFile(song)
                
            except Exception as ex:
                print('mutagenx not loaded or not an audio file')

            self.assertEqual(len(str(a)), 282)
            self.assertEqual(a.size, 5735510)
        else:
            print('no audio file to test')


            
    def test_99_file_delete(self):
        f = cl.File(self.fname)
        self.assertEqual(f.exists(), True)
        f.delete()
        self.assertEqual(f.exists(), False)
        
        # try deleting a non existing file
        f_no_file = cl.File('')
        f_no_file.delete()
        
      
if __name__ == '__main__':
    unittest.main()
