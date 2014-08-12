
-----------------------------
--Reverse Pivot
--------------------------

INSERT INTO C_TEST_UNPIVOT (
Category, Car, Home, Travel, Study, UPDATE_DATE) (
SELECT 
'Car', Car, Home, Travel, Study, SYSDATE 
FROM C_TEST_UNPIVOT);
INSERT INTO C_TEST_UNPIVOT (
Category, Car, Home, Travel, Study, UPDATE_DATE) (
SELECT 
'Home', Car, Home, Travel, Study, SYSDATE 
FROM C_TEST_UNPIVOT);
INSERT INTO C_TEST_UNPIVOT (
Category, Car, Home, Travel, Study, UPDATE_DATE) (
SELECT 
'Travel', Car, Home, Travel, Study, SYSDATE 
FROM C_TEST_UNPIVOT);
INSERT INTO C_TEST_UNPIVOT (
Category, Car, Home, Travel, Study, UPDATE_DATE) (
SELECT 
'Study', Car, Home, Travel, Study, SYSDATE 
FROM C_TEST_UNPIVOT);
