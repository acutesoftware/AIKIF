# network_tools.py  written by Duncan Murray 26/3/2015

import os
import sys


try:
	import urllib.request as request
except:
	import urllib2 as request
	
import getpass
import socket

def get_user_name():
    """
    get the username of the person logged on
    """
    return getpass.getuser()

def get_host_name():
    """
    get the computer name
    """
    return socket.gethostname()

def download_file_no_logon(url, filename):
    """
    download a file from a public website with no logon required
    """
    output = open(filename,'wb')
    output.write(request.urlopen(url).read())
    output.close()

