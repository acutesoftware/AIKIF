---------------------------------------------
-- CREATE Fact Table - CORE_OBJECTS
---------------------------------------------
DROP TABLE CORE_OBJECTS CASCADE CONSTRAINTS;
CREATE TABLE CORE_OBJECTS (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_OBJECTS ON CORE_OBJECTS (id,name,key,value );
