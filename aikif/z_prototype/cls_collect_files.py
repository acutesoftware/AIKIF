# cls_collect_files.py	written by Duncan Murray 13/5/2014
# class for filelist collections in AIKIF

# NOTE - DO NOT USE THIS - should be replaced by agent_filelist.py

import cls_collect
import os
import fnmatch

class clsCollectFiles(cls_collect.clsCollect):
	"""
	Collects file info for AIKIF
	"""
	def __init__(self, fldr=None, pattern="*.*"):
		self.fldr = fldr
		self.pattern = pattern
		self.tot_bytes = 0
		self.tot_files = 0
		self.tot_fldrs = 0
		self.filelist = []
		self.folders = []

	def collect_filelist(self):
		print("collecting files from " , self.fldr)	
		self.filelist = []
		self.folders = []
		for root, dirs, files in os.walk(self.fldr):
			self.tot_fldrs += 1
			self.folders.append(root)
			#print(root)
			for filename in fnmatch.filter(files, self.pattern):
				file_size = os.path.getsize((os.path.join(root, filename))) 
				self.tot_bytes += file_size
				self.tot_files += 1
				self.filelist.append(os.path.join(root, filename))
				#print(filename)
	
	def get_tot_fldrs(self):
		return self.tot_fldrs
		
	def get_tot_files(self):
		return self.tot_files
		
	def get_tot_bytes(self):
		return self.tot_bytes
		
	def get_filelist(self):
		print("there are " , str(len(self.filelist)), " files found")
		return self.filelist
		
	def get_folders(self):
		print("there are " , str(len(self.folders)), " folders found")
		return self.folders
		