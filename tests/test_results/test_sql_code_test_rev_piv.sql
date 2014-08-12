
-----------------------------
--Reverse Pivot
--------------------------

INSERT INTO C_SALES_UNPIVOT (
Question, Sales, Expenses, YEAR, Person, UPDATE_DATE) (
SELECT 
'Q1', Sales, Expenses, YEAR, Person, SYSDATE 
FROM C_SALES_UNPIVOT);
INSERT INTO C_SALES_UNPIVOT (
Question, Sales, Expenses, YEAR, Person, UPDATE_DATE) (
SELECT 
'Q2', Sales, Expenses, YEAR, Person, SYSDATE 
FROM C_SALES_UNPIVOT);
