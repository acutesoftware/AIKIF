# test_fileMapping.py     written by Duncan Murray 8/4/2014
# unit testing for AIKIF - test the file mapping module
# note - only functions starting with the string 'test' get tested

import unittest
import os
import sys
import csv
sys.path.append('..//AI')
import AIKIF_utils as aikif
import fileMapping as filemap

class TestFileMap(unittest.TestCase):
 
	def setUp(self):
		pass

	def test_count_dataFileTypes(self):
		self.assertEqual( len(filemap.dataFileTypes), 7)	

	def test_count_dataSubjectAreas(self):
		self.assertGreater( 20 , len(filemap.dataFileTypes))	  # this list will increase

		
	def test_fileMap_findtype(self):
		self.assertEqual( filemap.FindType('thing'), 'THING')	
		self.assertEqual( filemap.FindType('Event'), 'EVENT')	
		self.assertEqual( filemap.FindType('LINK'), 'LINK')	
		self.assertEqual( filemap.FindType('OBJECT'), 'OBJECT')	
		self.assertEqual( filemap.FindType('loca'), 'LOCATION')	
		self.assertEqual( filemap.FindType('proces'), 'PROCESS')	
		self.assertEqual( filemap.FindType('actor'), 'ACTOR')	

	def test_fileMap_FindOntology(self):  # note, functions return a list (usually 1 item) of strings
		self.assertEqual( filemap.FindOntology('FILE-LECTURES'), ['SYSTEM-PC-FILE-LECTURES'])	
		self.assertEqual( filemap.FindOntology(''), ['_TOP'])	
		self.assertEqual( filemap.FindOntology('top'), ['_TOP'])	
		self.assertEqual( filemap.FindOntology('course'), ['INFO-COURSE'])	
		self.assertEqual( filemap.FindOntology('dataset'), ['INFO-DATASET'])	
		self.assertEqual( filemap.FindOntology('shop'), ['INFO-PIM-SHOPPING'])	
		self.assertEqual( filemap.FindOntology('DIARY'), ['INFO-PIM-DIARY'])	
		self.assertEqual( filemap.FindOntology('INFO-MESSAGE-EMAIL'), ['INFO-MESSAGE-EMAIL'])	
		self.assertEqual( filemap.FindOntology('PC-FILE'), ['SYSTEM-PC-FILE', 'SYSTEM-PC-FILE-LECTURES'])	# returns multiple
		self.assertEqual( filemap.FindOntology('Furniture'), ['OBJECT-ASSET-FURNITURE'])	
		self.assertEqual( filemap.FindOntology('Task'), ['INFO-PIM-TASK'])	
		self.assertEqual( filemap.FindOntology('Contact'), ['INFO-PIM-CONTACT'])	
		self.assertEqual( filemap.FindOntology('Pim-Note'), ['INFO-PIM-NOTE'])	
		self.assertEqual( filemap.FindOntology('PCusage'), ['INFO-PIM-PCUSAGE'])	
		self.assertEqual( filemap.FindOntology('email'), ['INFO-MESSAGE-EMAIL'])	
		self.assertEqual( filemap.FindOntology('message-sms'), ['INFO-MESSAGE-SMS'])	
		self.assertEqual( filemap.FindOntology('phone'), ['INFO-MESSAGE-PHONE'])	
		self.assertEqual( filemap.FindOntology('forum'), ['INFO-MESSAGE-FORUM'])	
		self.assertEqual( filemap.FindOntology('letter'), ['INFO-MESSAGE-LETTER'])	
		self.assertEqual( filemap.FindOntology('twitter'), ['INFO-SOCIAL-TWITTER'])	
		self.assertEqual( filemap.FindOntology('FACEBOOK'), ['INFO-SOCIAL-FACEBOOK'])	
		self.assertEqual( filemap.FindOntology('GoOgle+'), ['INFO-SOCIAL-GOOGLE+'])	
		self.assertEqual( filemap.FindOntology('social-other'), ['INFO-SOCIAL-OTHER'])	

	def test_fileMap_FindOntology(self):  # note, functions return a list (usually 1 item) of strings
		self.assertEqual( filemap.GetFilename('AAAAA', 'BBBBB'), 'AAAAA_BBBBB.CSV')	
		self.assertEqual( filemap.GetFilename('X', 'Y'), 'X_Y.CSV')	

		
		
if __name__ == '__main__':
	unittest.main()