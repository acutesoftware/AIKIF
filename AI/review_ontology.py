# coding: utf-8
# review_ontology.py	written by Duncan Murray 24/3/2014
# script to document and test samples of ontologies for
# possible use in AIKIF.  Consensus seems to be to build 
# your own ontology but this seems redundant (would be best 
# to re-use what is already done, THOUGH the idea is to keep
# your ontology as simple as it needs to be - so who knows...

# This script lists the sources and a short comment of each
# as well as functions to download and extract samples of each.

ontologyList = [  # links to various upper ontologies - http://en.wikipedia.org/wiki/Upper_ontology
	{'name': 'WordNet', 
	 'url': 'http://wordnet.princeton.edu/wordnet/download/', 
	 'data': 'http://wordnetcode.princeton.edu/wn3.1.dict.tar.gz', 	 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\WordNet\\dict\\data.noun', 
	 'rating': 'Best word list, not in OWL format, though qualifies as an upper ontology by including the most general concepts as well as more specialized concepts, related to each other not only by the subsumption relations, but by other semantic relations as well, such as part-of and cause. However, unlike Cyc, it has not been formally axiomatized so as to make the logical relations between the concepts precise. It has been widely used in Natural language processing research', 
	 'tested': 'Untested'},
	{'name': 'SUMO - Suggested Upper Merged Ontology', 
	 'url': 'http://www.ontologyportal.org/', 
	 'data': 'http://sigmakee.cvs.sourceforge.net/viewvc/sigmakee/KBs/?view=tar', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\SUMO\\KBs\\Mid-level-ontology.kif', 
	 'rating': 'Created by the IEEE working group P1600.1 - has multiple files by subject area which includes an upper ontology (which file?)', 
	 'tested': 'Untested'}, 
	{'name': 'DOLCE - Descriptive Ontology for Linguistic and Cognitive Engineering ', 
	 'url': 'http://www.loa.istc.cnr.it/', 
	 'data': 'http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\DOLCE\\DOLCE-Lite.owl', 
	 'rating': 'Not an active project on website, but has a clear cognitive bias, in that it aims at capturing the ontological categories underlying natural language and human common sense', 
	 'tested': 'Untested'}, 
	{'name': 'DBPedia', 
	 'url': 'http://wiki.dbpedia.org/Datasets', 
	 'data': 'http://wiki.dbpedia.org/Downloads39', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\wikipedia_categories\\dbpedia-ontology.owl.bz2.owl.bz2.owl', 
	 'rating': 'The most comprehensive set of data based on Wikipedia (470M facts)', 
	 'tested': 'Untested'}, 
	{'name': 'BFO - Basic Formal Ontology', 
	 'url': 'http://www.ifomis.org/bfo', 
	 'data': 'http://www.ifomis.org/bfo/1.1', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\BFO\\bfo-1.1.owl', 
	 'rating': 'Incorporates both three-dimensionalist and four-dimensionalist perspectives on reality within a single framework. Has over 100 other ontologies build based on this', 
	 'tested': 'Untested'},
	{'name': 'UMBEL', 
	 'url': 'http://structureddynamics.com/resources.html#Ontologies', 
	 'data': 'https://github.com/structureddynamics/UMBEL/blob/master/Ontology/umbel.n3', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\UMBEL\\umbel.n3', 
	 'rating': 'Maps to a simplified subset of the OpenCyc ontology (28,000 entries)', 
	 'tested': 'Untested'},
	{'name': 'DnS - Descriptions and Situations (implementation of DOLCE+DnS-Ultralite abbreviated to DUL) ', 
	 'url': 'http://stlab.istc.cnr.it/stlab/The_Semantic_Technology_Laboratory_%28STLab%29', 
	 'data': 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\DnS\\DUL.owl', 
	 'rating': 'constructivist ontology that pushes DOLCEs descriptive stance even further allowing for context-sensitive redescriptions of the types and relations postulated by other given ontologies', 
	 'tested': 'Untested'},
	{'name': 'GFO - General Formal Ontology', 
	 'url': 'http://www.onto-med.de/ontologies/index.jsp', 
	 'data': 'http://www.onto-med.de/ontologies/gfo.owl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\GFO\\gfo-ato.owl', 
	 'rating': 'have developed a top level ontology and a biological core ontology. OWL file is copyright, but redistribution allowed', 
	 'tested': 'Untested'},
	{'name': 'UFO - Unified Foundation Ontology', 
	 'url': 'https://oxygen.informatik.tu-cottbus.de/drupal7/ufo/', 
	 'data': '', 
	 'localFile': '', 
	 'rating': 'new, pretty good. tested for complex domains, combines DOLCE and GFO. Count not find single download OWL file', 
	 'tested': 'Untested'},
	{'name': 'CIDOC Conceptual Reference Model', 
	 'url': 'http://en.wikipedia.org/wiki/CIDOC_Conceptual_Reference_Model', 
	 'data': 'http://www.cidoc-crm.org/rdfs/cidoc_crm_v5.0.4_official_release.rdfs', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\CIDOC\\cidoc_crm_v5.0.4_official_release.rdfs', 
	 'rating': 'provides an extensible ontology for concepts and information in cultural heritage and museum documentation. Includes its own version of an upper ontology in its core classes', 
	 'tested': 'Untested'}, 
	{'name': 'COSMO - COmmon Semantic MOdel', 
	 'url': 'http://ontolog.cim3.net/cgi-bin/wiki.pl?COSMO', 
	 'data': 'http://www.micra.com/COSMO/COSMO.owl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\COSMO\\COSMO.owl', 
	 'rating': 'The current (May 2009) OWL version of COSMO has over 6400 types (OWL classes), over 700 relations, and over 1400 restrictions', 
	 'tested': 'Untested'}, 
	{'name': 'YAMATO - Yet Another More Advanced Top Ontology', 
	 'url': 'http://www.ei.sanken.osaka-u.ac.jp/hozo/onto_library/upperOnto.htm', 
	 'data': 'http://www.ei.sanken.osaka-u.ac.jp/hozo/onto_library/download.php?filename=YAMATO20120714owl.zip', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\YAMATO\\YAMATO20120714.owl', 
	 'rating': 'complex but very advanced', 
	 'tested': 'Untested'}, 
	{'name': 'OpenCyc', 
	 'url': 'http://en.wikipedia.org/wiki/Cyc#OpenCyc', 
	 'data': 'http://sourceforge.net/projects/texai/files/open-cyc-rdf/1.1/open-cyc.rdf.ZIP/download', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\OpenCyc\\open-cyc.rdf', 
	 'rating': 'Proprietry but fairly precise', 
	 'tested': 'Untested'},
	{'name': 'PROTON', 
	 'url': 'http://www.ontotext.com/proton-ontology', 
	 'data': 'http://www.ontotext.com/sites/default/files/proton/protontop.ttl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\PROTON\\protontop.ttl', 
	 'rating': 'basic subsumption hierarchy which provides coverage of most of the upper-level concepts necessary for semantic annotation, indexing, and retrieval', 
	 'tested': 'Untested'}, 
	{'name': 'IDEAS', 
	 'url': 'http://www.ideasgroup.org/7Documents/', 
	 'data': 'http://www.ideasgroup.org/file_download/5/IDEAS+Foundation+v1_0+Released+2009-04-24.xmi.zip', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\IDEAS\\IDEAS Foundation v1_0 Released 2009-04-24.xmi', 
	 'rating': 'The most common usage of IDEAS will be in direct exchange of information between architectural modelling tools are repositories', 
	 'tested': 'Untested'},
	{'name': 'MarineTLO', 
	 'url': 'http://www.ics.forth.gr/isl/MarineTLO/', 
	 'data': 'http://www.ics.forth.gr/isl/MarineTLO/v3/core_v3.owl', 
	 'localFile': 'S:\\DATA\\opendata\\ontology\\MarineTLO\\core_v3.owl', 
	 'rating': 'MarineTLO is a top-level ontology for the marine domain (also applicable to the terrestrial domain)', 
	 'tested': 'Untested'}, 
	{'name': 'DIY - eg build your own Ontology', 
	 'url': 'http://localhost', 
	 'data': '', 
	 'localFile': '', 
	 'rating': 'Not ideal - better to use existing sets, but best method to get a concise set of tuples', 
	 'tested': 'Untested'}
]

documentList = [  # links to various documents, tools and general ontology related notes
	{'title'			: 'A Comparison of Upper Ontologies (Technical Report DISI-TR-06-21)', 
		'url'			: 'http://www.disi.unige.it/person/MascardiV/Download/DISI-TR-06-21.pdf',
		'author'		: 'Viviana Mascardi1, Valentina Cordi, Paolo Rosso - Universita degli Studi di Genova, Italy', 
		'year'			: '', 
		'localSavedFile': 'comparison-of-ontologies-DISI-TR-06-21.pdf', 
		'comment'		: 'Summary of ontologies - compares BFO, cyc, DOLCE, GFO, PROTON, Sowas, SUMO'},
	{'title': 'Ontology-based data integration', 
		'url': 'http://en.wikipedia.org/wiki/Ontology-based_data_integration',
		'author': 'Wikipedia', 'year': '2013', 'localSavedFile': '', 
		'comment': 'short article with examples of approaches to use'},
	{'title': 'Python RDF library', 
		'url': 'https://github.com/RDFLib/rdflib', 
		'author': '', 'year': '2013', 'localSavedFile': '', 
		'comment': 'good simple examples for using RDFLIB at https://rdflib.readthedocs.org/en/latest/'},
	{'title': 'Protege - ontology editor', 
		'url': 'http://protege.stanford.edu/products.php#desktop-protege', 
		'author': 'Stanford', 'year': '', 'localSavedFile': '', 
		'comment': 'feature rich ontology editing environment with full support for the OWL 2 Web Ontology Language, and direct in-memory connections to description logic reasoners like HermiT and Pellet'},
	{'title': 'ontogenesis - upper level ontologies', 
		'url': 'http://ontogenesis.knowledgeblog.org/740',
		'author': 'Robert Hoehndorf', 'year': '2010', 
		'localSavedFile': 'ontogenesis.html', 
		'comment': 'basic overview of ontologies with descriptions of time/space and objects/processes'},
	{'title': 'DAML Ontology Library', 
	 'url': 'http://www.daml.org/ontologies/', 
	 'author': 'http://www.daml.org/ontologies/uri.html', 'year':'', 
	 'localSavedFile': 'S:\\DATA\\opendata\\ontology\\DAML\\uri.html', 
	 'comment': 'Not a single ontology, but has links to other ontologies of various grains'},
	{'title': 'Toward the Use of an Upper Ontology for U.S. Government and U.S. Military Domains: An Evaluation', 
		'url': 'http://oai.dtic.mil/oai/oai?verb=getRecord&metadataPrefix=html&identifier=ADA459575',
		'author': 'MITRE Corp report for US Government', 'year': '2004', 
		'localSavedFile': 'ADA459575.pdf', 
		'comment': 'very good explanation of the types of ontological choices such as 3d/4d, descriptive vs revisionary, mult vs reduct, ...'},
	{'title': 'ROMULUS - A repository of foundational ontologies', 
		'url': 'http://www.thezfiles.co.za/ROMULUS/downloads.html',
		'author': 'Zubeida Casmod Dawood', 'year': '2014',
		'localSavedFile': 'ROMULUS.html',
		'comment': 'Very good list of links to ontologies'},
	{'title': 'Ontological realism: A methodology for coordinated evolution of scientic ontologies', 
		'url': 'http://iospress.metapress.com/content/1551884412214u67/fulltext.pdf',
		'author': 'Barry Smith and Werner Ceusters - University of Buffalo', 'year': '2010',
		'localSavedFile': 'ontological-realisation.pdf',
		'comment': 'technical focus on biological and biomedical ontologies within the framework of the OBO (Open Biomedical Ontologies) Foundry initiative'	},
	{'title': 'Ontology Development 101: A Guide to Creating Your First Ontology', 
		'author': 'Natalya F. Noy and Deborah L. McGuinness - Stanford University', 'year': '2000?', 
		'url': 'http://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html',
		'localSavedFile': 'ontology101-noy-mcguinness.html', 
		'comment': 'Good introduction and examples of building an ontology - key points: reuse parts if possible, but build yourself to keep it short and valid'},
	{'title': 'KSL Ontonlingua', 
	 'url' : 'http://www.ksl.stanford.edu/software/ontolingua/', 
	 'author': 'Standford', 
	 'year': '2012', 
	 'localSavedFile': '', 
	 'comment': 'Ontolingua provides a distributed collaborative environment to browse, create, edit, modify, and use ontologies. The server supports over 150 active users, some of whom have provided us with descriptions of their projects. '},
	{'title': 'OCHRE', 
	 'url': 'http://en.wikipedia.org/wiki/Object-centered_high-level_reference_ontology', 
		'author'		: '', 
		'year'			: '', 
		'localSavedFile': 'S:\\DATA\\opendata\\ontology\\OCHRE\\ki2003epaper.pdf', 
	    'comment': 'Descriptive document, not an actual ontology - has a focus on conceptual simplicity, so that the number of basic (primitive) concepts and relations is as small as possible in order to simplify the theory'}, 
	{'title'			: 'Onto-Med Report Nr. 8', 
		'url'			: 'http://www.onto-med.de/publications/2010/gfo-basic-principles.pdf',
		'author'		: 'Onto-Med in  Leipzig', 
		'year'			: '', 
		'localSavedFile': 'gfo-basic-principles.pdf', 
		'comment'		: 'basic principles of GFO'}
]

commentsList = [
	{'src': 'comment', 'comment': 'there is no single correct ontology for any domain', 'url': 'http://protege.stanford.edu/publications/ontology_development/ontology101-noy-mcguinness.html'},
	{'src': 'conclusion', 'comment': 'use an existing top level ontology as a starting point, but base remaining ones on DOLCE', 'url': 'n/a'}
]

import os
import sys


def main():
	ShowStatistics()
	SaveHTML_Review('review_ontology.html')
	os.system('start review_ontology.html')

	#ShowConclusion()

def ShowStatistics():
	print('Ontologies 	= ' + str(len(ontologyList)))
	print('Documents 	= ' + str(len(documentList)))
	print('Comments 	= ' + str(len(commentsList)))
	
	
def ShowConclusion():
	print('Conclusion: ')
	for i in commentsList:
		#print(i['src'], i['comment'])
		if i['src'] == 'conclusion':
			print(i['comment'])


	
def ShowData():
	print('------ Ontologies-------\n')	
	for i in ontologyList:
		#print(i['name'], i['url'])
		print(i)
		
	print('------ Documents-------\n')	
	for i in documentList:
		print(i['title'], i['url'])

	print('------ COMMENTS-------\n')	
	for i in commentsList:
		print(i['comment'])
		


def SaveHTML_Review(htmlFile):
	#print(' saving results to ' + htmlFile)
	deleteFile(htmlFile)
	AppendToFile(htmlFile, BuildHTMLHeader('Ontology Review', '\r\n', '0'))
	AppendToFile(htmlFile, '</TABLE>')
	AppendToFile(htmlFile, 'Updated 25/3/2014 - list of upper ontologies with comments/ratings for possible use in AI applications.<BR><BR>\r\n')
	AppendToFile(htmlFile, '<H2>Ontology Datasets</h2>\r\n')
	for i in ontologyList:
		AppendToFile(htmlFile, '<B>' + i['name']  + '</B><BR>')
		AppendToFile(htmlFile, 'page = <a href=' + i['url'] + '>' + i['url'] + '</a><BR>')
		AppendToFile(htmlFile, 'data = <a href=' + i['data'] + '>' + i['data'] + '</a><BR>\r\n')
		AppendToFile(htmlFile, i['rating'] + '<BR>\r\n')
		AppendToFile(htmlFile,  TestLocalFile(i['localFile']) + '<BR><BR>\r\n')
	AppendToFile(htmlFile, '<BR><BR>\r\n')
	
	# show document list of RHS
	AppendToFile(htmlFile, '<H2>Useful Links for Ontological development</H2>\r\n')
	for i in documentList:
		AppendToFile(htmlFile, '<B>' + i['title'] + '</B><BR>' + '<a href=' + i['url'] + '>' + i['url'] + '</a><BR>\r\n')
		AppendToFile(htmlFile, i['comment'] + '<BR><BR>\r\n')
	AppendToFile(htmlFile, '<BR><BR></BODY></HTML>')

def BuildHTMLHeader(title, linefeed='\n', border='1'):
    res = "<HTML><HEAD><title>" + linefeed
    res = res + title + "</title>" + linefeed
    res = res + CreateCssString("Arial", "10pt", linefeed ) + linefeed
    res = res + "</HEAD><BODY><H1>"
    res = res + title + "</H1><TABLE border=" + border + ">"
    return res
	
def CreateCssString(fontFamily, baseFontSize, linefeed='\n'):
    css = "<STYLE>" + linefeed
    css = css + "BODY {      font-size:" + baseFontSize + "; FONT-FAMILY:" + fontFamily + "; }" + linefeed
    css = css + "A:link {    font-size:" + baseFontSize + "; COLOR: blue;TEXT-DECORATION:none}" + linefeed
    css = css + "A:visited { color: #003399; font-size:" + baseFontSize + ";TEXT-DECORATION:none }" + linefeed
    css = css + "A:hover {   color:#FF3300;TEXT-DECORATION:underline}" + linefeed
    css = css + "TD {        font-size:" + baseFontSize + "; valign=top; FONT-FAMILY:Arial; padding: 1px 2px 2px 1px;  }" + linefeed
    css = css + "H1 {        font-size:200%; padding: 1px 0px 0px 0px; margin:0px; }" + linefeed
    css = css + "H2 {        font-size:160%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:0px; }" + linefeed
    css = css + "H3 {        font-size:100%; FONT-WEIGHT:BOLD; padding:1px; letter-spacing:0.1em; }" + linefeed
    css = css + "H4 {        font-size:140%; FONT-WEIGHT:NORMAL; margin:0px 0px 0px 0px; padding:1px; }" + linefeed
    css = css + "</STYLE>" + linefeed
    return css
  
	
def deleteFile(f):
    if f == "":
        pass
    else:
        try:
            os.remove(f)
        except:
            print("Cant delete ",f)

def AppendToFile(fname, txt):
    with open(fname, "a") as myfile:
        myfile.write(txt)
	
def GetFileSize(localFile):
	return os.path.getsize(localFile)
	
def GetTotalNumFiles(localFile):
	fldr = os.path.dirname(localFile)
	fileList = os.listdir(fldr)
	numfiles = len([name for name in fileList if os.path.isfile(fldr + '\\' + name)])
	return numfiles
	
def GetTotalFileSizesForFolder(localFile):
	fldr = os.path.dirname(localFile)
	fileList = os.listdir(fldr)
	num = sum(os.path.getsize(fldr + '\\' + f) for f in fileList if os.path.isfile(fldr + '\\' + f))
	return num

def DoesFileExist(localFile):	
	success = False
	try:
		if os.path.isfile(localFile):
			success = True
	except:
		pass
	return success
	
def TestLocalFile(localFile):
	result = 'Not downloaded'
	if DoesFileExist(localFile):
			print('Collecting stats for ' + localFile)
			result = '<I>Sample file saved to ' + localFile + ' (' + format(GetFileSize(localFile), ',d') + ' bytes)<BR>'
			result = result + '' + format(GetTotalNumFiles(localFile), ',d')
			result = result + ' files in folder, totalling ' + format(GetTotalFileSizesForFolder(localFile), ',d') + ' bytes</I>'
	return result
	
def SaveHTML_Review_as_table(htmlFile):
	#print(' saving results to ' + htmlFile)
	deleteFile(htmlFile)
	AppendToFile(htmlFile, BuildHTMLHeader('Ontology Review', '\r\n', '2'))
	AppendToFile(htmlFile, '<TR>\r\n')
	AppendToFile(htmlFile, '<TD valign=top><TABLE border=1 valign=top width=96%>\r\n')
	AppendToFile(htmlFile, '<TH>Ontology</TH><TH>Test Comments</th><TH>Rating for AI</TH></TR>\r\n')
	for i in ontologyList:
		txtRow = '<TR>'
		#print(i['name'], i['url'])
		txtRow = txtRow + '<TD><a href=' + i['url'] + '>' + i['name'] + '</a></TD>\r\n'
		txtRow = txtRow + '<TD>' + i['tested'] + '</TD>\r\n'
		txtRow = txtRow + '<TD>' + i['rating'] + '</TD>\r\n'
		txtRow = txtRow + '</TR>\r\n'	
		#fle.AppendToFile(htmlFile, net.FormatListAsHTMLTableRow(dat.dict2list(i)))
		AppendToFile(htmlFile, txtRow)
	AppendToFile(htmlFile, '</TABLE></TD valign=top><TD>\r\n')
	
	# show document list of RHS
	AppendToFile(htmlFile, '<TABLE border=1 valign=top width=96%>\r\n')
	AppendToFile(htmlFile, '<TH>Document Title</TH><TH>Comments</th></TR>\r\n')
	for i in documentList:
		txtRow = '<TR>'
		#print(i['name'], i['url'])
		txtRow = txtRow + '<TD><a href=' + i['url'] + '>' + i['title'] + '</a></TD>\r\n'
		txtRow = txtRow + '<TD>' + i['comment'] + '</TD>\r\n'
		txtRow = txtRow + '</TR>\r\n'	
		#AppendToFile(htmlFile, net.FormatListAsHTMLTableRow(dat.dict2list(i)))
		AppendToFile(htmlFile, txtRow)
	AppendToFile(htmlFile, '</TABLE></TD><TD>\r\n')
	AppendToFile(htmlFile, '</TD></TR></TABLE><BR><BR><BR><BR></BODY></HTML>')

	
		
if __name__ == '__main__':
    main()	
	
	