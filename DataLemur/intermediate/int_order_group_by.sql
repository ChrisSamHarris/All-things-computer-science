
-- manufacturer = 'Pfizer';
-- GROUP BY can be used to aggregate aspects of the table independently and summarise data
-- GROUP BY, as you saw earlier, is all about grouping your data into categories
SELECT
    category,
    SUM(spend)
FROM
    product_spend
GROUP BY
    category;

-- Average spend on each product in 2022
SELECT
    product,
    AVG(SPEND)
FROM
    product_spend
WHERE
    transaction_date >= '01/01/2022'
    and transaction_date <= '12/31/2022'
GROUP BY
    product;

-- For every FAANG stock in the stock_prices dataset, write a SQL query to find the lowest price each stock ever opened at?
-- Be sure to also order your results by price, in descending order.
SELECT
    ticker,
    MIN(open)
FROM
    stock_prices
GROUP BY
    ticker
ORDER BY
    2 DESC;


-- Suppose you are given a table of candidates and their skills. How many candidates possess each of the different skills? Sort your answers based on 
-- the count of candidates, from highest to lowest.
SELECT
    skill,
    count(candidate_id)
FROM
    candidates
GROUP BY
    skill
ORDER BY
    count DESC;

-- ORDER BY helps you output your rows in a specific order, such as alphabetically on some text column, or from smallest to biggest, for some text column.

