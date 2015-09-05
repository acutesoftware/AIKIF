---------------------------------------------
-- CREATE Fact Table - CORE_EVENTS
---------------------------------------------
DROP TABLE CORE_EVENTS CASCADE CONSTRAINTS;
CREATE TABLE CORE_EVENTS (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_EVENTS ON CORE_EVENTS (id,name,key,value );
