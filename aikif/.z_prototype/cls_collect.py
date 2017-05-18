# cls_collect.py	written by Duncan Murray 13/5/2014
# Base class for collection classes for AIKIF

class clsCollect(object):
	"""
	Base Class for collection classes in AIKIF. Purpose is
    to provide consistent logging and tracking of collections
    
	"""
	def __init__(self, name=None,  fldr=None):
		self.name = name
		self.fldr = fldr

	def log(self, msg):
		print(("log: ", msg))