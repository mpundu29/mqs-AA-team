
CREATE TABLE AAPLL -- create second table for processing data
LIKE AAPL;

INSERT AAPLL -- fill table with data
SELECT *
FROM AAPL;

UPDATE AAPLL
SET `Date` = STR_TO_DATE(`Date`, '%m/%d/%Y'); -- format date column

UPDATE AAPLL
SET `Close/Last` = REPLACE(`Close/Last`, '$', ''); -- remove $

ALTER TABLE AAPLL -- turn date column into date datatype
MODIFY COLUMN `Date` DATE,
ADD logReturns DOUBLE; 

ALTER TABLE AAPLL
MODIFY COLUMN `Close/Last` DOUBLE;

UPDATE AAPLL 
JOIN (
    SELECT
        `Date`,
        LN(`Close/Last` / LAG(`Close/Last`) OVER (ORDER BY `Date`)) AS log_return
    FROM AAPLL
) r
ON AAPLL.`Date` = r.`Date`
SET AAPLL.logReturns = r.log_return;



SELECT `Date`, 
	logReturns,
    volitility
FROM (
	SELECT `Date`, 
			ROUND(LN(`CLose/Last` / LAG(`Close/Last`) OVER(ORDER BY `Date`)), 4) logReturns, -- calculate log returns (ordered by date, rounded to 4)
            
            STDDEV_SAMP(logReturns) OVER(ORDER BY `Date` ROWS BETWEEN 100 PRECEDING AND CURRENT ROW ) volitility -- take standard deviation 
	FROM AAPLL
) calculation
WHERE `Date` >= '2024-10-01' AND `Date` < '2025-10-01'; -- sort by time range

SELECT * 
FROM AAPLL; -- view final results






