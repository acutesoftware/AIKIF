---------------------------------------------
-- CREATE Fact Table - CORE_FACTS
---------------------------------------------
DROP TABLE CORE_FACTS CASCADE CONSTRAINTS;
CREATE TABLE CORE_FACTS (
id VARCHAR2(200), 
 name VARCHAR2(200), 
 key VARCHAR2(200), 
 value VARCHAR2(200), 
 UPDATE_DATE DATE 
);

CREATE INDEX ndx_CORE_FACTS ON CORE_FACTS (id,name,key,value );
