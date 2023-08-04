-- Continue exploring data types with these exercises:
-- Your company delivers fruit and vegetables to local grocery stores, and you
-- need to track the mileage driven by each driver each day to a tenth of a mile.
-- Assuming no driver would ever travel more than 999 miles in a day, what would
-- be an appropriate data type for the mileage column in your table? Why?

-- In the table listing each driver in your company, what are appropriate data
-- types for the drivers’ first and last names? Why is it a good idea to separate
-- first and last names into two columns rather than having one larger name column?

-- Assume you have a text column that includes strings formatted as dates.
-- One of the strings is written as '4//2021'. What will happen when you try to
-- convert that string to the timestamp data type?

-- Creating ideal table
CREATE TABLE drivers (
    first_name varchar(50), -- > 50 characters first/last name isn't likely
    last_name varchar(50), -- Easy to sort and search by first/last name
    miles smallint, -- smallest int type 999 < 32k
    bad_date varchar(10)
);

-- Inserting value with bas date format
INSERT INTO drivers 
VALUES 
    ('adrian', 'reload', '331', '4//2021')
;

-- Exporting data
SELECT * FROM drivers;

-- Trying CAST on bad date format
-- Throws an error
SELECT bad_date, CAST(bad_date AS TIMESTAMP) FROM drivers;