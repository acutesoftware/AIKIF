# cls_collect.py	written by Duncan Murray 13/5/2014
# Base class for collection classes for AIKIF

class clsCollect(object):
	"""
	Base Class for collection classes in AIKIF
	"""
	def __init__(self, name=None,  fldr=None):
		self.name = name
		self.fldr = fldr

