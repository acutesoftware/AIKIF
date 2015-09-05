---------------------------------------------
-- CREATE Fact Table - CORE_LOCATIONS
---------------------------------------------
DROP TABLE CORE_LOCATIONS CASCADE CONSTRAINTS;
CREATE TABLE CORE_LOCATIONS (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_LOCATIONS ON CORE_LOCATIONS (id,name,key,value );
