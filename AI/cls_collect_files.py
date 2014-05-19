# cls_collect_files.py	written by Duncan Murray 13/5/2014
# Base class for collection classes for AIKIF

import cls_collect

class clsCollectFiles(cls_collect.clsCollect):
	"""
	Collects file info for AIKIF
	"""
	def __init__(self, name=None,  fldr=None):
		self.name = name
		self.fldr = fldr
		self.filelist = []

	def collect_filelist(self):
		print("collecting files from " , self.fldr)	
		self.filelist = []
		
	
	def get_filelist(self):
		print("there are " , str(len(self.filelist)), " files found")
		return self.filelist
		