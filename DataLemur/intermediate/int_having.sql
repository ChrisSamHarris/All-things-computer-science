-- Overcome the error of 'aggregate functions are not allowed in WHERE' 
-- HAVING allows you to filter data based on values from aggregate functions like SUM, COUNT, AVG, MAX, and MIN
SELECT
    ticker,
    AVG(open)
FROM
    stock_prices -- WHERE AVG(open) > 200; -- This will throw an error
GROUP BY
    ticker
HAVING
    AVG(open) > 200;

-- WHERE filters on values in individual rows 
-- HAVING filters on values aggregated from groups of rows; AFTER grouping
-- Use SQL's HAVING & MIN commands to find all FAANG stocks whose open share price was always greater than $100.
SELECT
    ticker,
    MIN(open) as min
FROM
    stock_prices -- "stock_prices.ticker" must appear in the GROUP BY clause or be used in an aggregate function
GROUP BY
    ticker
HAVING
    MIN(open) > 100 -- HAVING with multiple conditions
SELECT
    ticker,
    AVG(open),
    MIN(open)
FROM
    stock_prices
GROUP BY
    ticker
HAVING
    AVG(open) > 200
    AND MIN(open) > 100;

-- Given a table of candidates and their technical skills, list the candidate IDs of candidates who have more than 2 technical skills.
SELECT
    candidate_id
FROM
    candidates
GROUP BY
    candidate_id
HAVING
    count(candidate_id) > 2


-- Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.
--Write a query to list the candidates who possess all of the required skills for the job. Sort the output by candidate ID in ascending order.
SELECT
  candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL') 
GROUP BY candidate_id
HAVING count(skill) = 3