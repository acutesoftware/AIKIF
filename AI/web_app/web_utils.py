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

def filelist2html(lst, fldr):
	txt = '<TABLE width=100% border=0>'
	for l in lst:
		txt += '<TR>'
		if type(l) is str:
			txt+= '<TD>' + link_file(l, fldr) + '</TD>\n'
		elif type(l) is list:
			txt+= '<TD>'
			for i in l:
				txt+= link_file(i, fldr) + ', '
			txt+= '</TD>'
		else:
			txt+= '<TD>' + str(l) + '</TD>\n'
		txt += '</TR>\n'
	txt += '</TABLE><BR>\n'
	return txt

def link_file(f, fldr):
	""" creates a html link for a file using folder fldr """
	return '<a href="' + fldr + f + '">' + f + '</a>'
	

def dict_to_htmlrow(d):
	res = "<TR>\n"
	for k, v in d.iteritems():
		if type(v) == str:
			res = res + '<TD>' + k + ':</TD><TD>' + v + '</TD>\n'
		else:
			res = res + '<TD>' + k + ':</TD><TD>' + str(v) + '</TD>\n'
	#print res
	res += '</TR>\n'
	return res
	