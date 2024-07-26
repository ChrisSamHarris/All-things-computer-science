-- ABS() | Absolute Difference 
-- ROUND(num, decimal places) | 
-- FLOOR() | Round down
-- CEIL() | Round up
-- POWER() | Calculate squared values 
-- MOD() or % | Calculate the remainder of a divison between two numbers 


--Imagine you are a Data Analyst working at CVS Pharmacy, and you had access to pharmacy sales data.
--For all Merck drugs, output the drug name, and the unit cost for each drug, rounded up to the nearest dollar. Order it from cheapest to most expensive drug.
SELECT
    drug,
    CEIL(total_sales / units_sold) as unit_cost
FROM
    pharmacy_sales
WHERE
    manufacturer like '%Merck%'
GROUP BY
    drug,
    units_sold,
    total_sales
ORDER BY
    unit_cost;