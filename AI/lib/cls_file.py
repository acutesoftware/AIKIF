# cls_file.py
import os
        
class File(object):
	"""
	handles various file conversions, reading, writing 
	as well as	general file operations (delete, copy, launch)
	"""
	
	def __init__(self, fname):
		self.fullname = fname
		self.name = fname  # convert to short name
		self.size = 1 # TODO
		self.date_modified = 1 # todo
		self.lines = 1
		
	def __str__(self):
		# when printing a file class it should print the name, size, date
		# as well as top 10 lines (first 80 chars in each line)
		txt = self.name + ' (' + str(self.size) + ')\n'
		return txt
		



	def append_text(self, txt):
		""" adds a line of text to a file """
		with open(self.fullname, "a") as myfile:
			myfile.write(txt)

	def convert_to_csv(self, op_csv_file, delim):
		""" function to simply convert the diary files to csv - testing """
		in_txt = csv.reader(open(self.fullname, "r"), delimiter = delim)
		ofile  = open(op_csv_file, 'w', newline='')
		out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		if in_txt != "":
			out_csv.writerows(in_txt)

	def launch(self, params=''):
		""" launch a file using os.system() - used for starting html pages """
		os.system("start " + self.fullname)    

	def delete(self):
		""" delete a file, dont really care if it doesnt exist """
		if self.fullname == "":
			pass
		else:
			try:
				os.remove(self.fullname)
			except:
				print("Cant delete ",self.fullname)

	def load_file_to_string(self):
		""" load a file to a string """
		with open(self.fullname, 'r') as f:
			txt = f.read()
		return txt
		
	def load_file_to_list(self):
		""" load a file to a list """
		lst = []
		with open(self.fullname, 'r') as f:
			for line in f:
				lst.append(line) 
		return lst	
