
------------------------------------------------------------
--  Insert staging records to Fact
------------------------------------------------------------

DELETE FROM C_FACT_TABLE;
COMMIT;
INSERT INTO C_FACT_TABLE (
    DATE,
    PRODUCT,
    CUSTOMER_NAME,
    AMOUNT,
    UPDATE_DATE) (
    SELECT 
        DATE,
        PRODUCT,
        CUSTOMER_NAME,
        AMOUNT,
        SYSDATE 
    FROM RAW_DATA_TABLE
);

------------------------------------------------------------
--  DQ Fixes
------------------------------------------------------------

UPDATE C_FACT_TABLE SET PRODUCT = 'new name' WHERE PRODUCT = 'old name'; 
UPDATE C_FACT_TABLE SET CUSTOMER_NAME = 'Corrected Name' WHERE CUSTOMER_NAME = 'wRong Name'; 
COMMIT;

------------------------------------------------------------
--  Key to Dimensions
------------------------------------------------------------

UPDATE C_FACT_TABLE op SET op.PRODUCT_KEY = NVL(
  (SELECT MAX (ip.PRODUCT_KEY)
    FROM U_PRODUCT_LIST ip WHERE substr(op.PRODUCT, 1,10) = 
       ip.product_name), -1); 

COMMIT;
