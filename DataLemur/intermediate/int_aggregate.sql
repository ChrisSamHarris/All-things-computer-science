-- AGGREGATE FUNCTIONS, GROUP BY, ORDER BY,


-- Find all customers who are between the ages of 18 and 22 (inclusive), live in either Victoria, Tasmania, Queensland,
--  their gender isn't "n/a", and their name starts with either 'A' or 'B'.
SELECT
    *
FROM
    customers
WHERE
    age BETWEEN 18
    AND 22
    AND state IN ('Victoria', 'Tasmania', 'Queensland')
    AND gender NOT LIKE '___'
    AND (
        customer_name LIKE 'A%'
        OR customer_name LIKE 'B%'
    )
LIMIT
    20;

-- AGGREGATE FUNCTIONS = SUM, MIN, MAX, AVG, COUNT
SELECT
    COUNT(drug),
    SUM(total_sales)
FROM
    pharmacy_sales
WHERE
    manufacturer IN ('Pfizer');
