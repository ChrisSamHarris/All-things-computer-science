-- The CASE statement in SQL allows you to shape, transform, manipulate, and filter data based on specified conditions. 
-- It's a conditional expression tool that lets you customize query results, create new categories, and apply conditional logic.
SELECT
    column_1,
    column_2,
    CASE
        WHEN condition_1 THEN result_1
        WHEN condition_2 THEN result_2
        WHEN...THEN...
        ELSE result_3 -- If condition_1 and condition_2 are not met, return result_3 in ELSE clause
    END AS column_3_name -- Give your new column an alias
FROM
    table_1;

-- example 
SELECT
    actor,
    character,
    platform,
    avg_likes,
    CASE
        WHEN avg_likes > 14999 THEN 'Super Likes'
        WHEN avg_likes BETWEEN 5000 AND 14999 THEN 'Moderate'
        ELSE 'Low Likes'
    END AS likes_category
FROM
    marvel_avengers
ORDER BY
    avg_likes DESC;