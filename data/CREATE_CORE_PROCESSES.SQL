---------------------------------------------
-- CREATE Fact Table - CORE_PROCESSES
---------------------------------------------
DROP TABLE CORE_PROCESSES CASCADE CONSTRAINTS;
CREATE TABLE CORE_PROCESSES (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_PROCESSES ON CORE_PROCESSES (id,name,key,value );
