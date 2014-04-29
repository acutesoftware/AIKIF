DROP TABLE test CASCADE CONSTRAINTS;
CREATE TABLE test ( 
    id VARCHAR2(200), 
    code VARCHAR2(200), 
    desc VARCHAR2(200), 
    REC_EXTRACT_DATE DATE
);

INSERT INTO test (id, code, desc, REC_EXTRACT_DATE) VALUES (
'id', 'code', 'desc',  sysdate ); 
INSERT INTO test (id, code, desc, REC_EXTRACT_DATE) VALUES (
'1', 'S', 'AAA',  sysdate ); 
INSERT INTO test (id, code, desc, REC_EXTRACT_DATE) VALUES (
'2', 'B', 'BBB',  sysdate ); 
INSERT INTO test (id, code, desc, REC_EXTRACT_DATE) VALUES (
'3', 'X', 'Long description',  sysdate ); 
COMMIT;