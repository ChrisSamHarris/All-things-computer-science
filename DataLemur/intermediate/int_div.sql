-- div is achieved through '/' 
-- CAST() is used to convert the result to a float
-- :: notation is used to convert the result to a float

SELECT 
  CAST(10 AS DECIMAL)/4,
  CAST(10 AS FLOAT)/4,
  10/CAST(6 AS DECIMAL),
  10/CAST(6 AS FLOAT); 

-- Can also divide integers by using multiplication by 1.0 
SELECT 
  10/6,
  10*1.0/6,
  10/6*1.0,
  10/(6*1.0);

SELECT 
  10::DECIMAL/4,
  10::FLOAT/4,
  10/4::DECIMAL,
  10/4::FLOAT,
  10::DECIMAL/6,
  10::FLOAT/6;

-- Calculate percentages: 
SELECT (part_column / total_column) * 100 AS percentage
FROM table;

-- Calculate percentages with rounding 
SELECT ROUND((part_column / total_column) * 100, n) AS percentage
FROM table;

