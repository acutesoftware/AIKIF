# -*- coding: utf-8 -*-
# cls_mssqlserver.py	 written by Duncan Murray 28/4/2014
# Simple wrapper for MS SQL Server functionality

#  install https://pypi.python.org/pypi/pypyodbc/ 
#  extract folder to D:\install\python\pypyodbc-1.3.1
# shell to folder, run setup.py
# in your main program:
	# import lib_data_SQLServer as sql
	# sql.CreateAccessDatabase('test.mdb')

import datetime
import csv
try:
	import pypyodbc 
except:
	print('you need to install https://pypi.python.org/pypi/pypyodbc/ ')
	exit(1)

from cls_database import Database


def TEST():
	testFile = 'D:\\database.mdb'
	print('wrapper for MS SQL Server and Access databases')
	
	d = MSSQL_server(['server', 'database', 'username', 'password'])
	d.save()
	print(d.server)
	
class MSSQL_server(Database):

	def CreateAccessDatabase(fname):
		pypyodbc.win_create_mdb(fname)
		connection = pypyodbc.win_connect_mdb(fname)
		connection.cursor().execute('CREATE TABLE t1 (id COUNTER PRIMARY KEY, name CHAR(25));').commit()
		connection.close()

	def CompactAccessDatabase(fname):
		pypyodbc.win_compact_mdb(fname,'D:\\compacted.mdb')

	def SQLServer_to_CSV(cred, schema, table, fldr, printHeader = True):
		opFile = fldr + table + '.CSV'
		print ('Saving ' + table + ' to ' + opFile)
		#cred = [server, database, username, password]
		connection_string ='Driver={SQL Server Native Client 11.0};Server=' + cred[0] + ';Database=' + cred[1] + ';Uid=' + cred[2] + ';Pwd=' + cred[3] + ';'
		#print(connection_string)
		conn = pypyodbc.connect(connection_string)
		cur = conn.cursor()	
		sqlToExec = 'SELECT * FROM ' + schema + '.' + table + ';'
		cur.execute(sqlToExec)
		op = open(opFile,'wb') # 'wb'
		if printHeader: # add column headers if requested
			txt = ''
			cols = []
			for col in cur.description:
			 txt += '"' + force_string(col[0]) + '",'
			op.write(txt + '\n')
		for row_data in cur: # add table rows			.encode('utf-8')
			txt = ''
			for col in row_data:
				txt += '"' + force_string(col) + '",'
			op.write(txt + '\n')
		op.close()	
		cur.close()
		conn.close()

	def force_string(obj):
		if type(obj) is str:
			return obj
		else:
			try:
				return str(obj)
			except:
				return 'Convert Error'
	
if __name__ == '__main__':
    TEST()	
	