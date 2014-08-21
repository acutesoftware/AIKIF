# coding: utf-8
# toolbox.py	written by Duncan Murray 20/3/2014	(C) Acute Software
# class to manage the functional toolbox of AIKIF

import AIKIF_utils as aikif
import fileMapping as filemap 
import os

class Toolbox():
	"""
	Class to manage the functional tools (programs or functions) that the AI can use 
	The toolbox starts as a subset of the Programs class (Programs manage the users 
	list of written programs and applications), and its purpose is to have an interface
	that an AI can use to run its own tasks.
	The toolbox is basically detailed documentation and interfaces for any program or 
	function that is robust enough to be used.
	The first use of this will be the dataTools 'identify columns' function which calls
	a solver from this managed list
	
	"""
	
	def __init__(self, fldr=None, lst=None):
		self.fldr = fldr
		if lst is None:
			self.lstTools = [] 
		else:
			self.lstTools = lst 
		aikif.LogCommand('Toolbox')
		aikif.LogDataSource(fldr)
		
	def add(self, tool):
		"""
		Adds a Tool to the list, logs the reference and TODO
		"""
		self.lstTools.append(tool)
		aikif.LogProcess(tool['file'] + '.' + tool['function'])
		print('Adding to toolbox : ', tool['file'] + '.' + tool['function'])
		
	def list(self):
		"""
		Display the list of items 
		"""
		for i in self.lstTools:
			print (i)
		return self.lstTools
	
	def tool_as_string(self, tool):
		return tool['file'] + '.' + tool['function'] + '\n'
	
	def save(self, fname=''):
		"""
		Save the list of tools to AIKIF core and optionally to local file fname
		"""
		if fname != '':
			with open(fname, 'w') as f:
				for t in self.lstTools:
					self.verify(t)
					f.write(self.tool_as_string(t))
					#f.write('\n'.join([i for i in t]))

	def verify(self, tool):
		success = True
		if os.path.isfile(tool['file']):
			print('program exists = TOK')
		else:
			print('program exists = FAIL')
			success = False
		
		return success
		
	def run(self, tool, args, silent='Y'):
		if silent == 'N':
			print('main called ' + tool['file'] + '->' + tool['function'] + ' with ', args, ' = ', tool['return'])
		mod = __import__( os.path.basename(tool['file']).split('.')[0])
		func = getattr(mod, tool['function'])
		tool['return'] = func(args)
		return tool['return']
				
		
		
		#import importlib
		#importlib.import_module(tool['file'])
		#importlib.import_module('solve_knapsack')
		
		#mod = import_this(tool['file'])
		# mod.doSomething()
		
		
		
