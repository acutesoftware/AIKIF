# test_fileMapping.py     written by Duncan Murray 8/4/2014
# unit testing for AIKIF - test the file mapping module
# note - only functions starting with the string 'test' get tested

import unittest
import os
import sys
import csv
#sys.path.append('..' + os.sep + 'aikif')
import aikif.cls_file_mapping as mod_filemap

class TestFileMap(unittest.TestCase):
 
	def setUp(self):
		self.filemap = mod_filemap.FileMap('.')

	def test_01_count_dataFileTypes(self):
		self.assertEqual( len(mod_filemap.dataFileTypes), 7)	

	def test_02_count_dataSubjectAreas(self):
		self.assertGreater( 20 , len(mod_filemap.dataFileTypes))	  # this list will increase

		
	def test_03_fileMap_find_type(self):
		self.assertEqual(self.filemap.find_type('thing'), 'THING')	
		self.assertEqual(self.filemap.find_type('Event'), 'EVENT')	
		self.assertEqual(self.filemap.find_type('LINK'), 'LINK')	
		self.assertEqual(self.filemap.find_type('OBJECT'), 'OBJECT')	
		self.assertEqual(self.filemap.find_type('loca'), 'LOCATION')	
		self.assertEqual(self.filemap.find_type('proces'), 'PROCESS')	
		self.assertEqual(self.filemap.find_type('actor'), 'ACTOR')	

	def test_04_fileMap_find_ontology(self):  # note, functions return a list (usually 1 item) of strings
		self.assertEqual(self.filemap.find_ontology('FILE-LECTURES'), ['SYSTEM-PC-FILE-LECTURES'])	
		self.assertEqual(self.filemap.find_ontology(''), ['_TOP'])	
		self.assertEqual(self.filemap.find_ontology('top'), ['_TOP'])	
		self.assertEqual(self.filemap.find_ontology('course'), ['INFO-COURSE'])	
		self.assertEqual(self.filemap.find_ontology('dataset'), ['INFO-DATASET'])	
		self.assertEqual(self.filemap.find_ontology('shop'), ['INFO-PIM-SHOPPING'])	
		self.assertEqual(self.filemap.find_ontology('DIARY'), ['INFO-PIM-DIARY'])	
		self.assertEqual(self.filemap.find_ontology('INFO-MESSAGE-EMAIL'), ['INFO-MESSAGE-EMAIL'])	
		self.assertEqual(self.filemap.find_ontology('PC-FILE'), ['SYSTEM-PC-FILE', 'SYSTEM-PC-FILE-LECTURES', 'SYSTEM-PC-FILE-PROGRAM'])	# returns multiple
		self.assertEqual(self.filemap.find_ontology('Task'), ['INFO-PIM-TASK'])	
		self.assertEqual(self.filemap.find_ontology('Contact'), ['INFO-PIM-CONTACT'])	
		self.assertEqual(self.filemap.find_ontology('Pim-Note'), ['INFO-PIM-NOTE'])	
		self.assertEqual(self.filemap.find_ontology('PCusage'), ['INFO-PIM-PCUSAGE'])	
		self.assertEqual(self.filemap.find_ontology('email'), ['INFO-MESSAGE-EMAIL'])	
		self.assertEqual(self.filemap.find_ontology('message-sms'), ['INFO-MESSAGE-SMS'])	
		self.assertEqual(self.filemap.find_ontology('phone'), ['INFO-MESSAGE-PHONE'])	
		self.assertEqual(self.filemap.find_ontology('forum'), ['INFO-MESSAGE-FORUM'])	
		self.assertEqual(self.filemap.find_ontology('letter'), ['INFO-MESSAGE-LETTER'])	
		self.assertEqual(self.filemap.find_ontology('twitter'), ['INFO-SOCIAL-TWITTER'])	
		self.assertEqual(self.filemap.find_ontology('FACEBOOK'), ['INFO-SOCIAL-FACEBOOK'])	
		self.assertEqual(self.filemap.find_ontology('GoOgle+'), ['INFO-SOCIAL-GOOGLE+'])	
		self.assertEqual(self.filemap.find_ontology('social-other'), ['INFO-SOCIAL-OTHER'])	

	def test_05_fileMap_get_filename(self):  
		self.assertEqual(self.filemap.get_filename('AAAAA', 'BBBBB'), 'AAAAA_BBBBB.CSV')	
		self.assertEqual(self.filemap.get_filename('X', 'Y'), 'X_Y.CSV')	

	def test_06_fileMap_get_full_filename(self):  
		self.assertEqual(self.filemap.get_full_filename('AAAAA', 'BBBBB'), self.filemap.get_datapath() + os.sep + 'core' + os.sep  + 'AAAAA_BBBBB.CSV')	

		
		
if __name__ == '__main__':
	unittest.main()