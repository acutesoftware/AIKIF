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
    > FLUSHBD
        >> (wipes current database)
    > DBSIZE
        >> 319 (returns number of keys in the database)
    > INFO MEMORY
        # Memory
        used_memory:4414184
        used_memory_human:4.21M
        used_memory_rss:4381296
        used_memory_peak:125389080
        used_memory_peak_human:119.58M
        used_memory_lua:33792
        mem_fragmentation_ratio:0.99
        mem_allocator:dlmalloc-2.8
    > BGSAVE
        >> saves data in background without slowing prod access (ie dont use SAVE)
    
    > KEYS id*   -- returns all keys starting with id
    > KEYS *Born* -- returns all keys containing Born field (like column select)
    
    
    
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
import cls_datatable

def TEST():
    root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..' + os.sep + 'data')
    fname = root_folder + os.sep + 'core' + os.sep + 'OBJECT_INFO-COURSE.csv'    


    print('wrapper for redis databases')
    host = '127.0.0.1'
    port = 6379
    db = 0
        
    d = redis_server(host, port , db)
    d.connect()
    print(d.server)
    d.set('test123', 'this is a test')
    print(d.get('test123'))
    
    dt = cls_datatable.DataTable(fname, ',')
    dt.load_to_array()
    d.import_datatable(dt, 'aikif', 1)
    
    print(d.get("aikif:OBJECT_INFO-COURSE.csv:categories:Artificial Intelligence Planning"))
    
    """
        127.0.0.1:6379> get "aikif:OBJECT_INFO-COURSE.csv:categories:Artificial Intelligence Planning"
        "https://class.coursera.org/aiplan-002/"
    """
        
    
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
        #print(res)
     
    def import_datatable(self, l_datatable, schema='datatable', col_key=0):
        """
        import a datatable (grid) by using the schema:table:column as keys.
        e.g. Sample input ( via cls_database.py -> test.csv)
        TERM,GENDER,ID,tot1,tot2
        5320,M,78,18,66
        1310,M,78,10,12
        
        Loads the following:
        """
        key = ''
        hdr = l_datatable.get_header()
        schema_root_key = schema + ':' + os.path.basename(l_datatable.name) + ':'
        print(hdr)
        for row_num, row in enumerate(l_datatable.get_arr()):
            #print(row)
            for col_num, col in enumerate(row):
                #print('col_num, col = ', col_num, col)
                if col and col_num < len(hdr):
                    key = schema_root_key + row[col_key] + ':' + hdr[col_num]
                    self.connection.set(key, col)
                    #self.connection.lpush(key, col)
        print ('loaded ', str(row_num) , ' rows')
        
        
    def export_to_CSV(fldr, printHeader = True):
        opFile = fldr + table + '.CSV'
        print ('Saving ' + table + ' to ' + opFile)
        #cred = [server, database, username, password]
        print(connection_string)

    
if __name__ == '__main__':
    TEST()	
    