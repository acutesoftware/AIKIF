# -*- coding: utf-8 -*-
# check_redis_limit.py	 written by Duncan Murray 31/8/2014

"""
Generates a random spreadsheet and loads it repeatedly
with incremental keys ( takes hours, but didnt get anywhere NEAR the limit

-------------------------------------------------------------------------
load_lots_of_strings = works!
Creates a list about a page long as a list of floats and the dbsize increments ok

Current Memory =  4.21M
dbsize= 20000  Total memory= 148.97M
dbsize= 40000  Total memory= 293.96M
dbsize= 60000  Total memory= 438.66M
dbsize= 80000  Total memory= 583.29M
dbsize= 100000  Total memory= 727.91M
dbsize= 120000  Total memory= 872.54M
dbsize= 140000  Total memory= 1017.16M
dbsize= 160000  Total memory= 1.14G
dbsize= 180000  Total memory= 1.28G
dbsize= 200000  Total memory= 1.42G
...
dbsize= 440000  Total memory= 3.12G
dbsize= 460000  Total memory= 3.26G
dbsize= 480000  Total memory= 3.40G
dbsize= 500000  Total memory= 3.54G
dbsize= 520000  Total memory= 3.68G
...
dbsize= 700000  Total memory= 4.97G
dbsize= 720000  Total memory= 5.11G
dbsize= 740000  Total memory= 5.25G
dbsize= 760000  Total memory= 5.39G
dbsize= 780000  Total memory= 5.53G
...
dbsize= 1000000  Total memory= 7.08G
dbsize= 1020000  Total memory= 7.22G
dbsize= 1040000  Total memory= 7.36G
...
dbsize= 1280000  Total memory= 9.06G
dbsize= 1300000  Total memory= 9.20G
dbsize= 1320000  Total memory= 9.34G
...
Memory via Windows (PC appearing to get slow ? paging)

	16.0 GB DDR3

	Speed:	1600 MHz
	Slots used:	2 of 4
	Form factor:	DIMM
	Hardware reserved:	113 MB

	Available	9.0 GB
	Cached	5.9 GB
	Committed	9.4/31.9 GB
	Paged pool	267 MB
	Non-paged pool	148 MB
	In use	6.8 GB




sample key: (value is same length == approx 3926 chars)
127.0.0.1:6379> keys n00021:45:120*
1) "n00021:45:120:[0.0, 12.162162162162161, 24.324324324324323, 36.4864864864864
84, 48.648648648648646, 60.81081081081081, 72.97297297297297, 85.13513513513513,
 97.29729729729729, 109.45945945945945, 121.62162162162161, 133.78378378378378,
145.94594594594594, 158.1081081081081, 170.27027027027026, 182.43243243243242, 1
94.59459459459458, 206.75675675675674, 218.9189189189189, 231.08108108108107, 24
3.24324324324323, 255.4054054054054, 267.56756756756755, 279.72972972972974, 291
.8918918918919, 304.05405405405406, 316.2162162162162, 328.3783783783784, 340.54
05405405405, 352.7027027027027, 364.86486486486484, 377.02702702702703, 389.1891
8918918916, 401.35135135135135, 413.5135135135135, 425.6756756756757, 437.837837
8378378, 450.0, 462.16216216216213, 474.3243243243243, 486.48648648648646, 498.6
4864864864865, 510.8108108108108, 522.9729729729729, 535.1351351351351, 547.2972
972972973, 559.4594594594595, 571.6216216216216, 583.7837837837837, 595.94594594
59459, 608.1081081081081, 620.2702702702702, 632.4324324324324, 644.594594594594
6, 656.7567567567568, 668.9189189189188, 681.081081081081, 693.2432432432432, 70
5.4054054054054, 717.5675675675675, 729.7297297297297, 741.8918918918919, 754.05
40540540541, 766.2162162162161, 778.3783783783783, 790.5405405405405, 802.702702
7027027, 814.8648648648648, 827.027027027027, 839.1891891891892, 851.35135135135
14, 863.5135135135134, 875.6756756756756, 887.8378378378378, 900.0, 912.16216216
21621, 924.3243243243243, 936.4864864864865, 948.6486486486486, 960.810810810810
7, 972.9729729729729, 985.1351351351351, 997.2972972972973, 1009.4594594594594,
1021.6216216216216, 1033.7837837837837, 1045.9459459459458, 1058.1081081081081,
1070.2702702702702, 1082.4324324324323, 1094.5945945945946, 1106.7567567567567,
1118.918918918919, 1131.081081081081, 1143.2432432432431, 1155.4054054054054, 11
67.5675675675675, 1179.7297297297296, 1191.8918918918919, 1204.054054054054, 121
6.2162162162163, 1228.3783783783783, 1240.5405405405404, 1252.7027027027027, 126
4.8648648648648, 1277.0270270270269, 1289.1891891891892, 1301.3513513513512, 131
3.5135135135135, 1325.6756756756756, 1337.8378378378377, 1350.0, 1362.1621621621
62, 1374.3243243243242, 1386.4864864864865, 1398.6486486486485, 1410.81081081081
08, 1422.972972972973, 1435.135135135135, 1447.2972972972973, 1459.4594594594594
, 1471.6216216216214, 1483.7837837837837, 1495.9459459459458, 1508.1081081081081
, 1520.2702702702702, 1532.4324324324323, 1544.5945945945946, 1556.7567567567567
, 1568.9189189189187, 1581.081081081081, 1593.2432432432431, 1605.4054054054054,
 1617.5675675675675, 1629.7297297297296, 1641.8918918918919, 1654.054054054054,
1666.216216216216, 1678.3783783783783, 1690.5405405405404, 1702.7027027027027, 1
714.8648648648648, 1727.0270270270269, 1739.1891891891892, 1751.3513513513512, 1
763.5135135135133, 1775.6756756756756, 1787.8378378378377, 1800.0, 1812.16216216
2162, 1824.3243243243242, 1836.4864864864865, 1848.6486486486485, 1860.810810810
8106, 1872.972972972973, 1885.135135135135, 1897.2972972972973, 1909.45945945945
94, 1921.6216216216214, 1933.7837837837837, 1945.9459459459458, 1958.10810810810
81, 1970.2702702702702, 1982.4324324324323, 1994.5945945945946, 2006.75675675675
67, 2018.9189189189187, 2031.081081081081, 2043.2432432432431, 2055.405405405405
4, 2067.5675675675675, 2079.7297297297296, 2091.8918918918916, 2104.054054054054
, 2116.2162162162163, 2128.3783783783783, 2140.5405405405404, 2152.7027027027025
, 2164.8648648648646, 2177.027027027027, 2189.189189189189, 2201.3513513513512,
2213.5135135135133, 2225.6756756756754, 2237.837837837838, 2250.0, 2262.16216216
2162, 2274.324324324324, 2286.4864864864862, 2298.6486486486488, 2310.8108108108
11, 2322.972972972973, 2335.135135135135, 2347.297297297297, 2359.459459459459,
2371.6216216216217, 2383.7837837837837, 2395.945945945946, 2408.108108108108, 24
20.27027027027]"
(0.81s)


------------------------------------------------------
Odd things with load csv:
- windows task manager didnt increase much at all, and more importantly didnt
  show the redis-server as increasing in ram usage
  
- the incremental load is using SET which overwrites, but the ids are quite unique
(random 40 letters) so would not have expected many collisions. As each 100,000 load
occurred the dbsize did not increase by 100,000 rather about 900
  [check random keys and it appears that all data was loaded though]
  

id2,DATE,name,surname,Born,Location,Quote,Score,Points
IkNbnaYdDx4o2GsI9KG6OxhLRbKqsZX755OJTcUx,1991,Bowie,Sissy,East Indies,Tokelau,sire,6,23
B6CeEKJkarJk8qsDhJ8WbfFHcsqvzzWzJgzwn2ka,2003,Kerr,Rock,Saint Vincent And The Grenadines,Netherlands,round whitefish,76,10
69AGnQ6lTvSjuOkRVNCSSiQJElSNc0WC1G4VAQi6,2003,Penn,Clitus,Kyrgyzstan,Bulgaria,sparkling,50,66
vOLXNBiUGGNV60nbWYZ7cHFMFnFCLKznrobnWWCw,2012,Malina,Belinda,Hungary,Jamaica,genus eschrichtius,81,24
AXC7BWpqW6kWFsIrHjC8h1ELdSxwLtVKLS24DkcK,1985,Becca,Marcell,Caribbean,Liechtenstein,copperhead,90,29


127.0.0.1:6379> info memory
# Memory
used_memory:64558712
used_memory_human:61.57M
used_memory_rss:64525824
used_memory_peak:90953504
used_memory_peak_human:86.74M
used_memory_lua:33792
mem_fragmentation_ratio:1.00
mem_allocator:dlmalloc-2.8
127.0.0.1:6379> dbsize
(integer) 422164

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

from aikif.dataTools.if_database import Database
import aikif.dataTools.cls_datatable as mod_dt
import aikif.dataTools.if_redis as mod_redis
import aikif.dataTools.generateTestData as mod_gen
    
def main():
    if not confirm_loadtesting():
        exit(0)
    print('Load testing redis databas...')
    
    host = '127.0.0.1'
    port = 6379
    db = 0
        
    d = mod_redis.redis_server(host, port , db)
    d.connect()
  
    print('Current Memory = ', d.connection.info()['used_memory_human'])
    load_lots_of_strings(d)
#    load_random_tables(d)
    
def load_random_tables(d):
    root_folder = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..' + os.sep + '..' + os.sep + 'data')
    fname = root_folder + os.sep + 'temp' + os.sep + 'TEMP_LOAD_TESTING.csv'
    create_test_file(fname)
    dt = mod_dt.DataTable(fname, ',')
    dt.load_to_array()
    num_loads = 400
    for load in range(20, 20 + num_loads):
        schema = 'tst' + str(load).zfill(5)
        d.import_datatable(dt, schema, 0)
        print('dbsize=',d.connection.dbsize(), ' Total memory=', d.connection.info()['used_memory_human'])


    
def load_lots_of_strings(d):
    num_loads = 40000
    for load in range(20, 20 + num_loads):
        schema = 'n' + str(load).zfill(5)
        for i in range(100):
            for j in range(200):
                val = [j*i/3.7 for j in range(200)]
                key = schema + ':' + str(i)  + ':' + str(j)+ ':' + str(val)
                res = d.set(key, val)
        print('dbsize=',d.connection.dbsize(), ' Total memory=', d.connection.info()['used_memory_human'])


        
    
def confirm_loadtesting():
    print("\n--------WARNING--------\nThis will load test the redis database\n")
    if input('Press 6 to continue') != '6':
        print("Aborting")
        return False
    return True

def create_test_file(fname):
    """ create a very large random test file """
    colLabel = [ 'id2',     'DATE', 'name',   'surname',  'Born',  'Location',  'Quote', 'Score', 'Points']
    colTypes = [ 'STRING', 'DATE', 'PEOPLE', 'PEOPLE',   'PLACE', 'PLACE',     'WORD',  'INT',   'INT']
    
    test_datatable = mod_dt.DataTable(fname, ',')
    test_datatable.arr = mod_gen.random_table(9,100000, colTypes, colLabel)
    test_datatable.header = colLabel
    test_datatable.save_csv(fname, False)
    
if __name__ == '__main__':
    main()	
    
    