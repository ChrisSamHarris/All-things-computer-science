-- Represents the abscence of a value | Missing or unknown piece of information
-- IS NULL & IS NOT NULL | ID null and none-null values 
-- COALESCE() |  Returns the first non-null value from a list of arguments -> COALESCE(column_name, 'expression')
-- IFULL(column_X, replacement) |  Substitutes null value with a specified value

SELECT
    *
FROM
    goodreads
WHERE
    book_title IS NOT NULL;


--Tesla is investigating production bottlenecks and they need your help to extract the relevant data. Write a query to determine which parts have begun 
--the assembly process but are not yet finished.
--Assumptions:
--parts_assembly table contains all parts currently in production, each at varying stages of the assembly process.
--An unfinished part is one that lacks a finish_date.

SELECT
    part,
    assembly_step
FROM
    parts_assembly
WHERE
    finish_date is NULL;