# -*- coding: utf-8 -*-
# cls_redis.py	 written by Duncan Murray 31/8/2014
"""
 Simple wrapper for redis database functionality
 

USAGE:

    import cls_redis as db
    db.???

NOTES
install redis as follows:
   > pip install redis

install redis server as follows:
  download https://github.com/ServiceStack/redis-windows
  run E:\apps\redis\redis64-2.8.9\redis-server.exe
 
test server via client:
    > E:\apps\redis\redis64-2.8.9\redis-cli.exe
    > set task "build boat"
    > get task
    >>   boat
 
useful redis commands:
    > INFO
    >> (returns details of memory, usage, stats)
    > KEYS *
    >> (returns [often HUGE] complete list of keys)
    
To clean the database, simply kill the server and restart

To save database: 
    TODO
 
"""
import os
import sys
import datetime
import csv
try:
    import redis 
except:
    print('you need to run pip install redis \nand also install the server via https://github.com/ServiceStack/redis-windows')
    exit(1)

from if_database import Database


def TEST():
    print('wrapper for redis databases')
    host = '127.0.0.1'
    port = 6379
    db = 0
        
    d = redis_server(host, port , db)
    d.connect()
    print(d.server)
    d.set('test123', 'this is a test')
    print(d.get('test123'))
    
class redis_server(Database):
    def __init__(self, host, port , db):
        """ override the database base class to get a 
        connection string to a local redis server 
        (this is not how class will be implemented - just testing for now)
        """
        super().__init__([host + ':' + str(port), str(db), '', ''])
        self.connection = redis.StrictRedis(host, port , db);

    def get(self, key):  
        """ get a set of keys from redis """
        res = []
        res = self.connection.get(key)
        print(res)
        return res
        
    def set(self, key, val):  
        """ add data """
        res = []
        res = self.connection.set(key, val)
        print(res)
        
        
    def export_to_CSV(fldr, printHeader = True):
        opFile = fldr + table + '.CSV'
        print ('Saving ' + table + ' to ' + opFile)
        #cred = [server, database, username, password]
        print(connection_string)

    
if __name__ == '__main__':
    TEST()	
    