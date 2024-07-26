-- The DISTINCT SQL command is used in conjunction with the SELECT statement to return only distinct (different) values. 
-- You can use DISTINCT with aggregate functions – the most common one being COUNT. Here's an example that finds the number of unique user's who made trades:
SELECT
    COUNT(DISTINCT user_id)
FROM
    trades;

-- Assume you're given a table containing data on Amazon customers and their spending on products in different category. 
-- Write a query using COUNT DISTINCT to identify the number of unique products within each product category
SELECT
    category,
    COUNT(DISTINCT product)
FROM
    product_spend
GROUP BY
    category

    