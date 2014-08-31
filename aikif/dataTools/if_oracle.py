# -*- coding: utf-8 -*-
# cls_oracle.py	 written by Duncan Murray 28/4/2014
# Simple wrapper for Oracle functionality

try:
	import cx_Oracle
except:
	print(' you need to install cx_Oracle')
	exit(1)
	
import csv
import ctypes
from if_database import Database


def TEST():
	print('wrapper for Oracle database')
	d = Oracle(['server', 'database', 'username', 'password'])
	d.save()
	
class Oracle(Database):
	def GetListOfOracleTables(self, conn, tNameFilter):
		sql = "select * from TAB where tname like '" + tNameFilter + "'"
		opList = []
		c = conn.cursor()
		c.execute(sql)
		for row_data in c:
			opList.append(row_data[0])
		return opList
		
	def Oracle2CSV(self, conn, tblName, fldrLocation = '', printHeader = True):
		csv_file_dest = fldrLocation + tblName + ".CSV"
		print('Exporting ', tblName,' to ',csv_file_dest )
		outputFile = open(csv_file_dest,'wb') # 'wb'
		output = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		sql = "select * from " + tblName
		curs2 = conn.cursor()
		curs2.execute(sql)

		if printHeader: # add column headers if requested
			cols = []
			for col in curs2.description:
				cols.append(col[0])
			output.writerow(cols)

		for row_data in curs2: # add table rows
			output.writerow(row_data)

		outputFile.close()	

	def ConnectOracle(self, schema, dbase, usr, encryptedPasswd):
		# connects to Oracle database and returns the open connection cursor
		password = base64.b64decode('XXXXXXXX')
		conn_str = schema + u'/' + password + '@' + dbase
		print(conn_str)
		conn = cx_Oracle.connect(conn_str)
		return conn
		
	def DisconnectOracle(self, conn):
		# closes the open connection cursor
		try:
			conn.close()
			print("Connection to Oracle closed")
		except:
			print("WARNING - could not close connection in DisconnectOracle")
		


	
if __name__ == '__main__':
    TEST()	
	