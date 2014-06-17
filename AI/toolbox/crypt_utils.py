# crypt_utils.py	written by Duncan Murray 1/5/2014
# originally forked from lib_crypt.py		written by Duncan Murray 1/5/2014
# functions for various ciphers, encryptions, translators

"""
OUTPUT
encode64 : hi there
binary   : 0b110100001101001001000000111010001101000011001010111001001100101
decode64 : hi there
reverse  : ereht ih
reverse2 : ereht ih
caeser   : hi there shifted 0 = hithere
caeser   : hi there shifted 1 = ijuifsf
caeser   : hi there shifted 2 = jkvjgtg
sentence : the quick brown fox jumped over the lazy dog
jumbled  : dog over brown the fox lazy quick jumped the


"""

import random
import math
import binascii
import string
import sys

try:
	from Crypto.Cipher import AES
except:
	print('You need to install https://pypi.python.org/pypi/pycrypto/2.6.1')

def solve(encrypted_text):
	""" 
	takes an array of bytes and applies several methods to 
	decrypt or unjumble to find words
	"""
	print('attempting to decrypt ' + encrypted_text)
	print('TODO')
	
def check_for_words(txt):
	"""
	checks for english words in a string to see if decrypted
	"""
	print('TODO')
	return False
	

def test_base64(msg):
	bin = txt2bin(msg)
	print('encode64 : ' + msg )
	print('binary   : ' + bin)
	reCoded = bin2txt(bin)
	print('decode64 : ' + reCoded)

def test_caeser(txt):
	for i in range(0,3):
		if sys.version[0:2] == '2.':
			res = caesar(txt, 0)
		else:   # Running alternate caeser function Python 3.3
			res = caeser2(txt, i)
		print('caeser   : ' + txt + ' shifted ' + str(i) + ' = ' + res)
	
def test_crypto(msg):
	try:
		secret = encrypt_AES('key123', msg, 'iv456')
		result = decrypt_AES('key123', secret, 'iv456')
		print()
		print('original  = ' + msg)
		print('encrypted = ' + secret)
		print('decrypted = ' + result)
	except:
		print('encryption test failed')

	
def encode64(visible_text): 
	""" encodes a string to base 64 - not encryption but handy for hiding text from shoulder surfing  """
	return base64.b64encode(bytes(visible_text, 'utf-8')).decode('utf-8') 
	
def decode64(poorly_hidden_text): 
	""" decodes base 64 string to clear text   """
	return base64.b64decode(poorly_hidden_text).decode('utf-8')
	
def reverse(txt): 
	""" reverses all letters in a string """
	return txt[::-1] 
	
def reverse_slow(txt): 
	""" reverses all letters in a string - slower method """
	return ''.join(reversed(txt))


def jumble_words(txt):
	""" takes a sentence and randomly shuffles the word positions """
	words = txt.split(' ')
	for i in range(0,200):
		pos1 = random.randint(0, len(words)-1)
		pos2 = random.randint(0, len(words)-1)
		words[pos1], words[pos2] = words[pos2], words[pos1] 
	return ' '.join(w for w in words)


def caesar(msg, shift):
	""" caeser cipher jumbles text by bit shifting -  requires Python 2.7 """
	letters = string.ascii_lowercase
	shuffled = letters[shift:] + letters[:shift]
	table = string.maketrans(letters, shuffled) 
	return msg.translate(table)

	
def caeser2(msg, shift):
	""" caeser cipher jumbles text by bit shifting - longer version """
	cipherText = ""
	for ch in msg:
		if ch.isalpha():
			stayInAlphabet = ord(ch) + shift 
			if stayInAlphabet > ord('z'):
				stayInAlphabet -= 26
			finalLetter = chr(stayInAlphabet)
			cipherText += finalLetter
	return cipherText
	
def encrypt_AES(key, plain_text, IV456):
	obj = AES.new(key, AES.MODE_CBC, IV456)
	return obj.encrypt(plain_text)
	
def decrypt_AEX(key, ciphertext, IV456):	
    obj = AES.new(key, AES.MODE_CBC, IV456)
    return obj.decrypt(ciphertext)

	
def txt2bin(txt): 
	""" convert text to binary string - The code expects ascii characters in range: [ -~] """
	return bin(int(binascii.hexlify(txt.encode('ascii', 'strict')), 16))

def bin2txt(bin):
	""" convert binary string to text """
	n = int(bin, 2)
	return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()	


def test_full_range():
	""" lists the ASCII characters - currently buggy after 128 """
	for i in range(0, 128):
		char = chr(i)
		print(str(i) + '  ' + char + ' ' + txt2bin(char))

def pprint_binary(txt):
	""" splits a binary string starting with 0b into a nice 2 x 4 digit display"""
	op = txt[2:].zfill(7)
	return op[:4] + '-' + op[4:]
		

