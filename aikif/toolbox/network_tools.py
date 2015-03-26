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

def download_file(p_realm, p_url, p_op_file, p_username, p_password, p_logon_url=''):
    # https://docs.python.org/3/library/urllib.request.html#examples
    # Create an OpenerDirector with support for Basic HTTP Authentication...
    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(realm=p_realm,
                              uri=p_url,
                              user=p_username,
                              passwd=p_password)
    opener = urllib.request.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    urllib.request.install_opener(opener)
    if p_logon_url == '':
        p_logon_url = p_url
    urllib.request.urlopen(p_logon_url)

