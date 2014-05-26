# web_utils.py	written by Duncan Murray 26/5/2014
# functions to convert data to HTML, etc for web dev

def list2html(lst):
	txt = '<TABLE width=100% border=0>'
	for l in lst:
		txt += '<TR>\n'
		if type(l) is str:
			txt+= '<TD>' + l + '</TD>\n'
		elif type(l) is list:
			txt+= '<TD>'
			for i in l:
				txt+= i + ', '
			txt+= '</TD>'
		else:
			txt+= '<TD>' + str(l) + '</TD>\n'
		txt += '</TR>\n'
	txt += '</TABLE><BR>\n'
	return txt
	
		