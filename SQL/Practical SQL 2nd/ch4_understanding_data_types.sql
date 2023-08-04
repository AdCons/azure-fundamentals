-- Creating a table with character data types
CREATE TABLE char_data_types (
    char_column char(10),
    varchar_column varchar(10),
    text_column text
);

-- Inserting data into the table
INSERT INTO
    char_data_types
VALUES
    ('abc', 'abc', 'abc'),
    ('defghi', 'defghi', 'defghi');

-- Exporting data to a CSV file
COPY char_data_types TO 'X:\practical-sql-2nd\char_data_types.csv'
WITH (FORMAT CSV, HEADER, DELIMITER '|');

-- Creating a table with number data types
CREATE TABLE number_data_types (
    numeric_column numeric(20, 5), -- 15 digits to the left, 5 to the right, pad with 0s
    real_column real, -- 6 digits of precision, no padding
    double_columns double precision -- 15 digits of precision, no padding
);
-- Inserting data into the table
INSERT INTO
    number_data_types
VALUES
    (.7, .7, .7),
    (2.13579, 2.13579, 2.13579),
    (2.1357987654, 2.1357987654, 2.1357987654);

-- Exploring the data
SELECT * FROM number_data_types;

-- Creating a table with date and time data types
CREATE TABLE date_time_types (
    timestamp_column timestamp with time zone,
    interval_column interval
);

-- Inserting data into the table
INSERT INTO
    date_time_types
VALUES
    ('2022-12-31 01:00 EST', '2 days'),
    ('2022-12-31 01:00 -8', '1 month'),
    ('2022-12-31 01:00 Australia/Melbourne', '1 century'),
    (now(), '1 week');

-- Exploring the data
SELECT * FROM date_time_types;

-- Calculating with date and time data types
SELECT
    timestamp_column,
    interval_column,
    timestamp_column - interval_column AS new_date
FROM date_time_types;

-- Transforming values from one data type to another with CAST

-- It will work
SELECT
    timestamp_column,
    CAST(timestamp_column AS varchar(10))
FROM
    date_time_types;

-- It will work
SELECT numeric_column, CAST(numeric_column AS integer), CAST(numeric_column AS text)
FROM number_data_types;

-- It will fail
SELECT CAST(char_column AS integer)
FROM char_data_types;

-- Using CAST shortcut notation
SELECT timestamp_column, CAST(timestamp_column AS varchar(10)), timestamp_column::varchar(10)
FROM date_time_types;