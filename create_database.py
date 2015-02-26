# create_data_base.py
import sys, os

if sys.version[0:1] != '3':
    print ("Python Version = " + sys.version)
    print('==== WARNING - use a bat file to start Python 3 ======')
    exit(1)

import aikif.dataTools.cls_datatable as mod_table

# create a REAL csv file 
tbl_sales = mod_table.DataTable('C_SALES', 'data' + os.sep + 'sales.csv', ['date', 'amount', 'product'])
tbl_sales.add(['2015-01-09', 24.95, 'Timer'])
tbl_sales.add(['2015-02-17', 45.00, 'Diary'])
tbl_sales.add(['2015-02-19', 24.95, 'Timer'])
print(tbl_sales)
tbl_sales.save_csv('data' + os.sep + 'my_sales.csv')   

# create the SQL of a file
from aikif.dataTools.cls_sql_code_generator import SQLCodeGenerator
t2 = SQLCodeGenerator('C_SALES')
t2.set_column_list(['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT', 'PRODUCT_KEY', 'CUSTOMER_KEY'])

t2.create_script_staging_table('S_SALES', ['DATE', 'PRODUCT', 'CUSTOMER_NAME', 'AMOUNT'])
t2.create_index('S_SALES', ['DATE', 'PRODUCT', 'CUSTOMER_NAME'])

t2.create_script_fact()
t2.create_index('C_SALES', ['DATE', 'PRODUCT_KEY', 'CUSTOMER_KEY'])

t2.save_ddl('data' + os.sep + 'create_sales_fact.sql')

"""
---------------------------------------------
-- CREATE Staging Table - S_SALES
---------------------------------------------
DROP TABLE S_SALES CASCADE CONSTRAINTS;
CREATE TABLE S_SALES (
DATE VARCHAR2(200), 
 PRODUCT VARCHAR2(200), 
 CUSTOMER_NAME VARCHAR2(200), 
 AMOUNT VARCHAR2(200), 
 UPDATE_DATE  DATE 
);

CREATE INDEX ndx_S_SALES ON S_SALES (DATE,PRODUCT,CUSTOMER_NAME );
---------------------------------------------
-- CREATE Fact Table - C_SALES
---------------------------------------------
DROP TABLE C_SALES CASCADE CONSTRAINTS;
CREATE TABLE C_SALES (
DATE VARCHAR2(200), 
 PRODUCT VARCHAR2(200), 
 CUSTOMER_NAME VARCHAR2(200), 
 AMOUNT VARCHAR2(200), 
 PRODUCT_KEY VARCHAR2(200), 
 CUSTOMER_KEY VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_C_SALES ON C_SALES (DATE,PRODUCT_KEY,CUSTOMER_KEY );

"""


t2.aggregate('C_AGG_PRODUCT', 'PRODUCT', 'sum(AMOUNT)')
t2.save('data' + os.sep + 'create_sales_agg_product.sql')

"""
 DROP TABLE C_AGG_PRODUCT;
 CREATE TABLE C_AGG_PRODUCT AS (
    SELECT PRODUCT, sum(AMOUNT) AS result 
    FROM C_SALES GROUP BY PRODUCT
);
"""