# log_browser_history.py		written by Duncan Murray 13/1/2014 

#OUTPUT:
# Reading Chrome history from C:\Users\....\AppData\Local\Google\Chrome\User Data\Default
# Exported 44868 records to chrome_history.csv


import os
import datetime
import sqlite3
import codecs, re
import time
import sys
from os.path import expanduser

#from datetime import datetime
# NOTE - bug as at 3/10/2014 - 'no such table urls' when run from python 3.44868

pattern = "(((http)|(https))(://)(www.)|().*?)\.[a-z]*/"
SQL_STATEMENT = 'SELECT urls.url, urls.title, urls.visit_count, urls.typed_count, urls.last_visit_time, visits.visit_time, urls.hidden, visits.from_visit, urls.id, visits.transition  FROM urls, visits WHERE urls.id = visits.url;'


try:
	opFile = sys.argv[1]
except:
	opFile = os.getcwd() + '\\chrome_history.csv'


storage = codecs.open(opFile, 'w', 'utf-8')

def DateConv(webkit_timestamp):
	return date_from_webkit(webkit_timestamp)
 
def date_from_webkit_ORIG_RETURNS_GMT_TIME(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    return epoch_start + delta
	
def date_from_webkit(webkit_timestamp):
	UTC_OFFSET_TIMEDELTA = datetime.datetime.utcnow() - datetime.datetime.now()
	epoch_start = datetime.datetime(1601,1,1)
	delta = datetime.timedelta(microseconds=int(webkit_timestamp))
	return epoch_start + delta - UTC_OFFSET_TIMEDELTA

def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

home = expanduser("~")
basePath = home + r"\AppData\Local\Google\Chrome\User Data\Default" 
#basePath = 'C:\\Users\\Duncan\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
print ("Reading Chrome history from " + basePath)
#paths = [basePath + "\\Archived History", basePath + "\\History"]  # causes error because no results found
paths = [basePath + "\\History"] 


def GetBrowserHistoryChrome():
	numRecs = 0
	storage.write('"url","visit_count","typed_count","last_visit_time","visit_time","hidden","from_visit","id","transition","title"\n')
	for path in paths:
		c = sqlite3.connect(path)
		for row in c.execute(SQL_STATEMENT):
			#storage.write( row[0] + ", " + row[1] + ", " + str(row[2])+ ", ")
			storage.write( '"' + row[0] + '","' + str(row[2]) + '","' + str(row[3]) + '","' + str(DateConv(row[4]))[0:21]  + '","' + str(DateConv(row[5]))[0:21] + '","' + str(row[6]) + '","' + str(row[7]) + '","' + str(row[8]) + '","' + str(row[9]) + '","' + row[1] + '"\n'  )
			numRecs = numRecs + 1
			#date_time = date_from_webkit(row[1])
			#url = re.search(pattern, row[0])
			#try: urlc = url.group(0)
			#except: urlc = "ERROR"
			#storage.write(str(date_time)[0:19] + "\t" + urlc + "\n")
	print('Exported ' + str(numRecs) + ' records to ' + opFile)		
# Main


		
if __name__ == '__main__':
	GetBrowserHistoryChrome()	



		