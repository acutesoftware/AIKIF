# cls_collect_files.py	written by Duncan Murray 13/5/2014
# Base class for collection classes for AIKIF

import cls_collect
import os
import fnmatch

class clsCollectFiles(cls_collect.clsCollect):
	"""
	Collects file info for AIKIF
	"""
	def __init__(self, name=None,  fldr=None):
		self.name = name
		self.fldr = fldr
		self.tot_bytes = 0
		self.tot_files = 0
		self.tot_fldrs = 0
		self.filelist = []

	def collect_filelist(self):
		print("collecting files from " , self.fldr)	
		self.filelist = []
		for root, dirs, files in os.walk(self.fldr):
			self.tot_fldrs += 1
			for filename in fnmatch.filter(files, "*.*"):
				#file_size = GetFileSize(os.path.join(root, filename)) 
				self.filelist.append(os.path.join(root, filename))
	
	def get_filelist(self, fldr):
		print("there are " , str(len(self.filelist)), " files found")
		return self.filelist
		