# network_tools.py  written by Duncan Murray 26/3/2015

import os
import sys
import aikif.config as mod_cfg

try:
	import urllib.request as request
except:
	#import urllib2 as request
    print('cant import urllib')
    exit(1)
    
#import urllib2 as request	
import getpass
import socket

def load_username_password(fname):
    """
    use the config class to read credentials
    """
    username, password = mod_cfg.read_credentials(fname)
    return username, password  # load_username_password

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
    
    output = open(filename,'wb')
    output.write(request.urlopen(url).read())
    output.close()    
    """
    import urllib.request
    #url = "http://www.google.com/"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    with open(filename,'wb') as f:
        #print (response.read().decode('utf-8'))
        f.write(response.read())

def download_file(p_realm, p_url, p_op_file, p_username, p_password):
    # https://docs.python.org/3/library/urllib.request.html#examples
    # Create an OpenerDirector with support for Basic HTTP Authentication...
    auth_handler = request.HTTPBasicAuthHandler()
    auth_handler.add_password(realm=p_realm,
                              uri=p_url,
                              user=p_username,
                              passwd=p_password)
    opener = request.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    request.install_opener(opener)

    web = request.urlopen(p_url)
    with open(p_op_file, 'w') as f:
        f.write(web.read().decode('utf-8'))
        
def download_file_proxy(p_realm, p_url, p_op_file, p_username, p_password, proxies):
    print('downloading file ', p_url)
    print('with credentials : ', p_username, p_password)
    r = requests.get(p_url, auth=(p_username, p_password), proxies=proxies)
    print(r.status_code)
    with open(p_op_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)    
	# currently fails at work, 
