# cls_file.py
import os
        
class File(object):
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
		with open(self.fullname, "a") as myfile:
			myfile.write(txt)

	def convert_to_csv(self, op_csv_file, delim):
		# function to simply convert the diary files to csv - testing
		in_txt = csv.reader(open(self.fullname, "r"), delimiter = delim)
		#out_csv = csv.writer(open(csv_file, 'w')
		ofile  = open(op_csv_file, 'w', newline='')
		out_csv = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		#print (in_txt)
		if in_txt != "":
			out_csv.writerows(in_txt)

	def launch(self, params=''):
		os.system("start " + self.fullname)    

	def delete(self):
		if self.fullname == "":
			pass
		else:
			try:
				os.remove(self.fullname)
			except:
				print("Cant delete ",self.fullname)

	def load_file_to_string(self):
		with open(self.fullname, 'r') as f:
			txt = f.read()
		return txt
		
	def load_file_to_list(self):
		lst = []
		with open(self.fullname, 'r') as f:
			for line in f:
				lst.append(line) 
		return lst	
