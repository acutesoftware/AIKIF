# coding: utf-8
# network_tools.py  written by Duncan Murray 26/3/2015

import urllib
import urllib.request
import aikif.config as mod_cfg
    
#import urllib2 as request	
import getpass
import socket


def TEST():
    url = 'http://www.google.com'
    print('downloaded ' + str(len(get_web_page(url))) + ' bytes from ' + url)

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

def get_web_page(url):
	txtString = '404'
	try:
		rawText = urllib.request.urlopen(url).read()
		txtString =  str( rawText, encoding='utf8' )
	except UnicodeError:
		pass
	return txtString
    
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

def get_protected_page(url, user, pwd, filename):
    """
    having problems with urllib on a specific site so trying requests
    """
    import requests
    r = requests.get(url, auth=(user, pwd))
    print(r.status_code)
    print(len(str(r)))
    if r.status_code == 200:
        print('success')
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(4096):
                fd.write(chunk)
    else:
        print('failed = ' + str(r.status_code))
        
def download_file(p_realm, p_url, p_op_file, p_username, p_password):
    """
    Currently not working...
    # https://docs.python.org/3/library/urllib.request.html#examples
    # Create an OpenerDirector with support for Basic HTTP Authentication...
    """
    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(realm=p_realm,
                              uri=p_url,
                              user=p_username,
                              passwd=p_password)
    opener = urllib.request.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    urllib.request.install_opener(opener)

    web = urllib.request.urlopen(p_url)
    with open(p_op_file, 'w') as f:
        f.write(web.read().decode('utf-8'))
        
def download_file_proxy(p_url, p_op_file, p_username, p_password, proxies):
    """
    Currently fails behind proxy...
    # https://docs.python.org/3/library/urllib.request.html#examples
    """
    chunk_size=4096
    print('downloading file ', p_url)
    print('with credentials : ', p_username, p_password)
    import requests
    r = requests.get(p_url, auth=(p_username, p_password), proxies=proxies)
    print(r.status_code)
    with open(p_op_file, 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)    

if __name__ == '__main__':
    TEST()    
    