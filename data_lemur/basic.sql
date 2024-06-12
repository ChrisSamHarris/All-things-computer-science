SELECT
    *
FROM
    reviews
WHERE
    stars = 4
    AND product_id != 50001;

SELECT
    *
FROM
    reviews
WHERE
    stars > 3
    AND stars < 5s
    AND product_id != 50001;

SELECT
    *
FROM
    medals
WHERE
    type = "GOLD"
    AND year BETWEEN 2000
    AND 2010;

SELECT
    manufacturer,
    drug,
    units_sold
FROM
    pharmacy_sales
WHERE
    (
        manufacturer = 'Biogen'
        OR manufacturer = 'AbbVie'
        OR manufacturer = 'Eli Lilly'
    )
    AND units_sold BETWEEN 100000
    AND 105000;

SELECT
    manufacturer,
    drug,
    units_sold
FROM
    pharmacy_sales
WHERE
    manufacturer IN ('Roche', 'Bayer', 'AstraZeneca')
    AND units_sold NOT BETWEEN 55000
    AND 550000;

-- Find all customers whose first name starts with "F" and the last letter in their last name is "ck".
SELECT
    *
FROM
    customers
WHERE
    customer_name LIKE 'F%ck'
LIMIT
    20;

-- Find all customers where the 2nd and 3rd letter in their name is "e".
SELECT
    *
FROM
    customers
WHERE
    customer_name LIKE '_ee%'
LIMIT
    20;

-- Find all customers who are between the ages of 18 and 22 (inclusive), live in either Victoria, Tasmania, Queensland,
--  their gender isn't "n/a", and their name starts with either 'A' or 'B'.
SELECT
    *
FROM
    customers
WHERE 
    age BETWEEN 18 AND 22 
    AND state IN ('Victoria', 'Tasmania', 'Queensland')
    AND gender NOT LIKE '___'
    AND (customer_name LIKE 'A%' OR customer_name LIKE 'B%')
LIMIT
    20;