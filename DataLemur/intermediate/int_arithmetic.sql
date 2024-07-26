-- use math expressions to transform column values - Addition, Division, Subtraction, Modulus, Multiplication, Exponentiation (^) and negation (-NUM)
SELECT
    particle_speed / 10.0 + speed_offset
FROM
    particle_sensor_data
WHERE
    (particle_position ^ 2) * 10.0 > 500
    AND sensor_type = 'photon'
    AND measurement_day % 7 = 0;

-- CVS Health is trying to better understand its pharmacy sales, and how well different products are selling. Each drug can only be produced by one manufacturer.
-- Write a query to find the top 3 most profitable drugs sold, and how much profit they made. Assume that there are no ties in the profits. Display the result from the highest to the lowest total profit
SELECT
    drug,
    total_sales - cogs as total_profit
FROM
    pharmacy_sales
ORDER by
    total_profit DESC
LIMIT
    3;

--Your team at JPMorgan Chase is preparing to launch a new credit card, and to gain some insights, you're analyzing how many credit cards were issued each month.
-- Write a query that outputs the name of each credit card and the difference in the number of issued cards between the month with the highest issuance cards and the lowest issuance. 
-- Arrange the results based on the largest disparity.
SELECT
    card_name,
    MAX(issued_amount) - MIN(issued_amount) as difference
FROM
    monthly_cards_issued
GROUP BY
    card_name
ORDER BY
    difference DESC;

-- Display the stocks which had "big-mover months" (up or down 10%), and how many of those months they had. Order your results from the stocks with the most, to least, "big-mover months".
SELECT ticker, COUNT(ticker)
FROM stock_prices 
WHERE (close-open)/ open > 0.10 OR (close - open)/open < -0.10
GROUP BY ticker
ORDER BY count desc ;
