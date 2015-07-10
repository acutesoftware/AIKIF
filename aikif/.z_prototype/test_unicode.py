# test_unicode.py   written by Duncan Murray 27/1/2015

import logging

logging.basicConfig(level=logging.INFO, filename='unicode.log', filemode='w')

logger = logging.getLogger("test_unicode.main")


ip_data = [{'type':'asc', 'dat':'the quick brown fox jumped over the lazy dog'},
           {'type':'hex','dat': b'\x01\x00\xd1\x11\x8cz\x00\xc0O\xc2\x97\xeb\x01\xe2\xeb\xbeD\xfc|H'},
           {'type':'bte','dat': [98,45,121,232,109]},
           {'type':'uni','dat': 'répertoire'}
           ]

def main():
    """ sample code to show differences in ascii / hex / unicode """
    try:
        print_ip_data(ip_data)      # display all input data
    except:
        logger.exception("Error printing")
        print("Error printing")
        
    try:
        print(ip_data[3]['dat'].decode("utf-8", "strict")  )
    except:
        logger.exception("Error decode(utf-8, strict)")
        print('Error decode("utf-8", "strict")'  )
        
    
def print_ip_data(ip):  
    for num, row in enumerate(ip_data):
        try:
            print(num, row['type'], ' = ', row['dat'])
        except:
            print('cant print row ', str(num))
     
def hex_to_ascii(ip): 
    for c in ip_data[1]['dat']:
        #print(c, ord('\u' + str(c)))
        print(type(c), c)
        try:
            print(chr(c))
        except:
            print('cant convert to chr')
            
            
if __name__ == '__main__':
    main()              