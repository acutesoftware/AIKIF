# page_about.py	written by Duncan Murray 31/5/2014
# handles the about page for AIKIF web interface


#import aikif.web_app.web_utils as web

def get_page(dataFile=''):
	txt = ''
	txt += "This is an example framework to capture the flow of information initially "
	txt += "for personal data management, but ultimately useful for AI applications.<BR>"
	txt += "Initially it will be populated and tested for human use, but includes tests "
	txt += "and verification process for future 'General AI's.<BR>"
    txt += dataFile + "<BR>"
	return txt
	
	

	