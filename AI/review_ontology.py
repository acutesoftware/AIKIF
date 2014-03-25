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
	 'rating': 'qualifies as an upper ontology by including the most general concepts as well as more specialized concepts, related to each other not only by the subsumption relations, but by other semantic relations as well, such as part-of and cause. However, unlike Cyc, it has not been formally axiomatized so as to make the logical relations between the concepts precise. It has been widely used in Natural language processing research', 
	 'tested': 'Untested'},
	{'name': 'SUMO - Suggested Upper Merged Ontology', 
	 'url': 'http://www.ontologyportal.org/', 
	 'rating': 'includes an upper ontology, created by the IEEE working group P1600.1', 
	 'tested': 'Untested'}, 
	{'name': 'DOLCE - Descriptive Ontology for Linguistic and Cognitive Engineering ', 
	 'url': 'http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl', 
	 'rating': 'has a clear cognitive bias, in that it aims at capturing the ontological categories underlying natural language and human common sense', 
	 'tested': 'Untested'}, 
	{'name': 'DBPedia', 
	 'url': 'http://wiki.dbpedia.org/Datasets', 
	 'rating': 'The most comprehensive set of data based on Wikipedia (470M facts)', 
	 'tested': 'Untested'}, 
	{'name': 'BFO - Basic Formal Ontology', 
	 'url': 'http://www.ifomis.org/bfo', 
	 'rating': 'Incorporates both three-dimensionalist and four-dimensionalist perspectives on reality within a single framework. Has over 100 other ontologies build based on this', 
	 'tested': 'Untested'},
	{'name': 'UMBEL', 
	 'url': 'http://structureddynamics.com/resources.html#Ontologies', 
	 'rating': 'Maps to a simplified subset of the OpenCyc ontology (28,000 entries)', 
	 'tested': 'Untested'},
	{'name': 'DnS - Descriptions and Situations', 
	 'url': 'http://stlab.istc.cnr.it/stlab/The_Semantic_Technology_Laboratory_%28STLab%29', 
	 'rating': 'constructivist ontology that pushes DOLCEs descriptive stance even further allowing for context-sensitive redescriptions of the types and relations postulated by other given ontologies', 
	 'tested': 'Untested'},
	{'name': 'GFO - General Formal Ontology', 
	 'url': 'http://www.onto-med.de/', 
	 'rating': 'Unrated', 
	 'tested': 'Untested'},
	{'name': 'UFO - Unified Foundation Ontology', 
	 'url': 'http://', 
	 'rating': 'new, pretty good. tested for complex domains, combines DOLCE and GFO', 
	 'tested': 'Untested'},
	{'name': 'CIDOC Conceptual Reference Model', 
	 'url': 'http://en.wikipedia.org/wiki/CIDOC_Conceptual_Reference_Model', 
	 'rating': 'domain ontology, but includes its own version of an upper ontology in its core classes', 
	 'tested': 'Untested'}, 
	{'name': 'COSMO - COmmon Semantic MOdel', 
	 'url': 'http://404', 
	 'rating': 'The current (May 2009) OWL version of COSMO has over 6400 types (OWL classes), over 700 relations, and over 1400 restrictions', 
	 'tested': 'Untested'}, 
	{'name': 'OCHRE', 
	 'url': 'http://en.wikipedia.org/wiki/Object-centered_high-level_reference_ontology', 
	 'rating': 'has a focus on conceptual simplicity, so that the number of basic (primitive) concepts and relations is as small as possible in order to simplify the theory', 
	 'tested': 'Untested'}, 
	{'name': 'YAMATO - Yet Another More Advanced Top Ontology', 
	 'url': 'http://www.ei.sanken.osaka-u.ac.jp/hozo/onto_library/upperOnto.htm', 
	 'rating': 'complex but very advanced', 
	 'tested': 'Untested'}, 
	{'name': 'KSL Omtonlingua', 
	 'url' : 'http://www.ksl.stanford.edu/software/ontolingua/', 
	 'rating': 'Unrated', 
	 'tested': 'Untested'},
	{'name': 'DAML Ontology Library', 
	 'url': 'http://www.daml.org/ontologies/', 
	 'rating': 'Unrated', 
	 'tested': 'Untested'},
	{'name': 'OpenCyc', 
	 'url': 'http://en.wikipedia.org/wiki/Cyc#ResearchCyc', 
	 'rating': 'Proprietry but fairly precise', 
	 'tested': 'Untested'},
	{'name': 'PROTON', 
	 'url': 'http://', 
	 'rating': 'basic subsumption hierarchy which provides coverage of most of the upper-level concepts necessary for semantic annotation, indexing, and retrieval', 
	 'tested': 'Untested'}, 
	{'name': 'IDEAS', 
	 'url': 'http://', 
	 'rating': 'not intended for reasoning and inference purposes; its purpose is to be a precise model of business', 
	 'tested': 'Untested'},
	{'name': 'MarineTLO', 
	 'url': 'http://www.ics.forth.gr/isl/MarineTLO/', 
	 'rating': 'Low - aimed for Marine domain', 
	 'tested': 'Untested'}, 
	{'name': 'DIY - eg build your own Ontology', 
	 'url': 'http://localhost', 
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
sys.path.append('..//..//aspytk')
import lib_file as fle
import lib_net as net
import lib_data as dat


def main():
	ShowStatistics()
	SaveHTML_Review('review_ontology.html')
	fle.LaunchFile('review_ontology.html')

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
	fle.deleteFile(htmlFile)
	fle.AppendToFile(htmlFile, net.BuildHTMLHeader('Ontology Review', '\r\n', '0'))
	fle.AppendToFile(htmlFile, '</TABLE>')
	fle.AppendToFile(htmlFile, 'Updated 25/3/2014 - list of upper ontologies with comments/ratings for possible use in AI applications.<BR><BR>\r\n')
	fle.AppendToFile(htmlFile, '<H2>Ontology Datasets</h2>\r\n')
	for i in ontologyList:
		fle.AppendToFile(htmlFile, '<B>' + i['name']  + '</B><BR><a href=' + i['url'] + '>' + i['url'] + '</a><BR>\r\n')
		fle.AppendToFile(htmlFile, i['rating'] + '<BR><BR>\r\n')
	fle.AppendToFile(htmlFile, '<BR><BR>\r\n')
	
	# show document list of RHS
	fle.AppendToFile(htmlFile, '<H2>Useful Links for Ontological development</H2>\r\n')
	for i in documentList:
		fle.AppendToFile(htmlFile, '<B>' + i['title'] + '</B><BR>' + '<a href=' + i['url'] + '>' + i['url'] + '</a><BR>\r\n')
		fle.AppendToFile(htmlFile, i['comment'] + '<BR><BR>\r\n')
	fle.AppendToFile(htmlFile, '<BR><BR></BODY></HTML>')

def SaveHTML_Review_as_table(htmlFile):
	#print(' saving results to ' + htmlFile)
	fle.deleteFile(htmlFile)
	fle.AppendToFile(htmlFile, net.BuildHTMLHeader('Ontology Review', '\r\n', '2'))
	fle.AppendToFile(htmlFile, '<TR>\r\n')
	fle.AppendToFile(htmlFile, '<TD valign=top><TABLE border=1 valign=top width=96%>\r\n')
	fle.AppendToFile(htmlFile, '<TH>Ontology</TH><TH>Test Comments</th><TH>Rating for AI</TH></TR>\r\n')
	for i in ontologyList:
		txtRow = '<TR>'
		#print(i['name'], i['url'])
		txtRow = txtRow + '<TD><a href=' + i['url'] + '>' + i['name'] + '</a></TD>\r\n'
		txtRow = txtRow + '<TD>' + i['tested'] + '</TD>\r\n'
		txtRow = txtRow + '<TD>' + i['rating'] + '</TD>\r\n'
		txtRow = txtRow + '</TR>\r\n'	
		#fle.AppendToFile(htmlFile, net.FormatListAsHTMLTableRow(dat.dict2list(i)))
		fle.AppendToFile(htmlFile, txtRow)
	fle.AppendToFile(htmlFile, '</TABLE></TD valign=top><TD>\r\n')
	
	# show document list of RHS
	fle.AppendToFile(htmlFile, '<TABLE border=1 valign=top width=96%>\r\n')
	fle.AppendToFile(htmlFile, '<TH>Document Title</TH><TH>Comments</th></TR>\r\n')
	for i in documentList:
		txtRow = '<TR>'
		#print(i['name'], i['url'])
		txtRow = txtRow + '<TD><a href=' + i['url'] + '>' + i['title'] + '</a></TD>\r\n'
		txtRow = txtRow + '<TD>' + i['comment'] + '</TD>\r\n'
		txtRow = txtRow + '</TR>\r\n'	
		#fle.AppendToFile(htmlFile, net.FormatListAsHTMLTableRow(dat.dict2list(i)))
		fle.AppendToFile(htmlFile, txtRow)
	fle.AppendToFile(htmlFile, '</TABLE></TD><TD>\r\n')
	fle.AppendToFile(htmlFile, '</TD></TR></TABLE><BR><BR><BR><BR></BODY></HTML>')

	
		
if __name__ == '__main__':
    main()	
	
	