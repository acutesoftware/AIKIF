---------------------------------------------
-- CREATE Fact Table - CORE_PEOPLE
---------------------------------------------
DROP TABLE CORE_PEOPLE CASCADE CONSTRAINTS;
CREATE TABLE CORE_PEOPLE (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_PEOPLE ON CORE_PEOPLE (id,name,key,value );
