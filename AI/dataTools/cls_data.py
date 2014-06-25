# cls_data.py	written by Duncan Murray 25/6/2014


class Data(object):
	"""
	Base class - not sure if this is needed, but the 
	intention is to use handle multiple datasets
	"""
	def __init__(self, name):
		self.name = name
		
		
	def __str__(self):
		return self.name
		

