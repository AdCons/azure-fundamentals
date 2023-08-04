# Practical SQL 2nd Edition

Practical SQL is for people who encounter data in their everyday lives and want to learn how to analyze, manage, and transform it.

## Chapter 1: Setting Up Your Coding Environment

### Database Management System (DBMS)

***PostgreSQL*** is a ***Database Management System (DBMS)***, which means it’s software that allows you to define, manage, and query databases.

When you installed PostgreSQL, it created a ***Database Server***—an instance of the application running on your computer—that includes a default database called ***postgres***.

```sql
-- Check installation and the version of PostgreSQL:
SELECT version();
```

### pgAdmin

With ***pgAdmin***, you get a ***graphical interface*** where you can configure multiple aspects of your ***PostgreSQL server*** and databases, and—most appropriately for this book—use a SQL query tool for writing, running, and saving queries.

## Chapter 2: Creating Your First Database And Table

SQL is more than just a means for extracting knowledge from data. It’s also a language for defining the structures that hold data so we can organize relationships in the data.

### Creating a Database

A ***Database*** is a collection of objects that includes tables, functions, and much more, and this is where your actual ***data*** will lie.

```sql
-- Create a database called analysis:
CREATE DATABASE analysis;
```

### Creating a Table

A ***Table*** is a collection of ***related data*** held in a structured format within a database.

When you create a table, you assign a name to each ***column*** (sometimes referred to as a ***field*** or ***attribute***) and assign each column a ***data type***. These are the values the column will accept—such as text, integers, decimals, and dates—and the definition of the data type is one way SQL enforces the
***integrity of data***.

Data stored in a table can be accessed and analyzed, or queried, with ***SQL statements***.

```sql
-- Create a table called teachers in the analysis database:
CREATE TABLE teachers (
    id bigserial,
    first_name varchar(50),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);
```

### Inserting Rows Into a Table

***Text and dates*** require ***quotes***; numbers, including integers and decimals, ***don’t*** require quotes.

```sql
-- Inserts teacher data into the table.
INSERT INTO
    teachers (
        first_name,
        last_name,
        school,
        hire_date,
        salary
        )
VALUES 
    ('Jane', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
    ('John', 'Doe', 'Alamo Street', '2010-06-30', 39100),
    ('Alice', 'Richards', 'Manuel Salazar Street', '2005-06-30', 40000),
    ('Mary', 'Simpson', 'Main Street', '2000-12-03', 43000),
    ('David', 'Smith', 'Jackson Drive', '1995-03-15', 45000),
    ('Helen', 'Andrews', 'North East Avenue', '1997-07-02', 43000),
    ('Richard', 'Doe', 'West Drive', '2000-08-09', 45000),
    ('Susan', 'Brown', 'Central Avenue', '2002-09-30', 47000),
    ('Joseph', 'Duncan', 'West Street', '1993-05-30', 50000),
    ('Andrew', 'Peters', 'Alamo Street', '2009-06-30', 39000)
;
```

## Chapter 3: Beginning Data Exploration With **SELECT**

A ***SELECT statement*** can be simple, retrieving everything in a single table, or it can be complex enough to link dozens of tables while handling multiple calculations and filtering by exact criteria.

### Basic **SELECT** Syntax

The ***asterisk*** following the ***SELECT*** keyword is a ***wildcard***, which is like a standing for a value: it doesn’t represent anything in particular and instead represents everything that value could possibly be.

The ***FROM*** keyword indicates you want the query to return data from a particular table. The semicolon after the table name tells PostgreSQL it’s the ***end of the query*** statement.

```sql
-- Basic SELECT syntax:
SELECT * FROM teachers;

-- Open table in pgAdmin:
TABLE teachers;
```

Often, it’s more practical to ***limit*** the ***columns*** the query retrieves, especially with large databases, so you don’t have to wade through excess information. You can do this by naming columns, separated by commas, right after the ***SELECT keyword***.

```sql
-- Querying a Subset of Columns
SELECT 
    hire_date,
    first_name,
    school
FROM
    teachers;
```

### Sorting Data With ***ORDER BY***

In SQL, we order the results of a query using a clause containing the keywords ***ORDER BY*** followed by the name of the column or columns to ***sort***.

By default, ***ORDER BY*** sorts values in ***ascending order***, but here I sort in ***descending order*** by adding the ***DESC*** keyword.

The ***ORDER BY*** clause also accepts ***numbers*** instead of column names, with the number identifying the sort column according to its position in the
***SELECT*** clause.

```sql
-- Sorting data with ORDER BY
SELECT
    first_name,
    school,
    salary
FROM
    teachers
ORDER BY
    salary DESC;

-- Sorting data with ORDER BY (using column position)
SELECT
    first_name,
    school,
    salary
FROM
    teachers
ORDER BY
    3 ASC;
```

### Using ***DISTINCT*** To Find Unique Values

To understand the range of values in a column, we can use the ***DISTINCT*** keyword as part of a query that eliminates duplicates and ***shows only unique values***.

This is a helpful first step toward assessing ***data quality***.

```sql
-- Using DISTINCT to find unique values
SELECT DISTINCT
    salary
FROM
    teachers
ORDER BY
    salary DESC;
```

The ***DISTINCT*** keyword also works on ***more than one*** column at a time. If we add a column, the query returns each ***unique pair of values***.

This technique gives us the ability to ask, ***“For each x in the table, what are all the y values?”***

### Filtering Rows With ***WHERE***

The ***WHERE*** clause allows you to ***find rows*** that ***match*** a specific value, a range of values, or multiple values based on criteria supplied via an ***operator***—a keyword that lets us perform math, comparison, and logical operations.

```sql
-- Filtering rows with WHERE
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    salary BETWEEN 45000 AND 50000;
```

### Filtering Rows With ***LIKE*** and ***ILIKE***

The ***LIKE*** operator, which is part of the ***ANSI SQL standard***, is ***case sensitive***. The ***ILIKE*** operator, which is a ***PostgreSQL-only implementation***, is ***case insensitive***.

- ***Percent sign (%)***: A wildcard matching ***one or more*** characters.
- ***Underscore (_)***: A wildcard matching ***just one*** character.

```sql
-- Using LIKE and ILIKE with WHERE
-- LIKE is case sensitive
SELECT
    *
FROM
    teachers
WHERE 
    first_name LIKE 'j%h_';
-- ILIKE is case insensitive
SELECT
    *
FROM
    teachers
WHERE 
    first_name ILIKE 'j%h_';
```

### Combining Operators with ***AND*** and ***OR***

***Comparison operators*** become even more useful when we ***combine them***. To do this, we connect them using the logical operators ***AND*** and ***OR*** along with, if needed, parentheses.

```sql
-- Combining Operators with AND
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    salary >= 39000
    AND first_name ILIKE 'j%';

-- Combining Operators with OR
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    (salary >= 45000 AND salary <= 50000)
    OR first_name ILIKE 'j%';
```

When we place statements inside parentheses, those ***are evaluated as a group*** before being combined with other criteria.

### Putting All Together

You can ***combine*** comparison operator statements using the ***AND*** and ***OR*** keywords to provide multiple criteria for filtering, and you can include an ***ORDER BY*** clause to rank the results.

```sql
-- Putting All Together
SELECT
    first_name,
    school,
    salary
FROM
    teachers
WHERE
    (salary >= 45000 AND salary <= 49000)
    OR first_name ILIKE 'j%'
ORDER BY
    salary DESC;
```

***SQL*** is particular about the ***order of keywords***, so follow this convention.

```sql
SELECT column_names
FROM table_name
WHERE criteria
ORDER BY column_names;
```

Sorting, filtering, and choosing only the ***most important*** columns from a table can yield a surprising amount of information from your ***data*** and help you find the ***story it tells***.

## Chapter 4: Understanding Data Types

It’s important to understand ***data types*** because storing data in the appropriate format is ***fundamental*** to building usable databases and performing ***accurate analysis***.

In a ***SQL database***, each column in a table can hold ***one and only one*** data type.

```sql
CREATE TABLE eagle_watch (
    observation_date date,
    eagles_seen integer,
    notes text
);
```

These data types fall into the three categories you’ll encounter most:

1. ***Characters***: Any character or symbol.
2. ***Numbers***: Includes whole numbers and fractions.
3. ***Dates and times***: Temporal information.

### Understanding Character

Character string types are ***general-purpose*** types suitable for any combination of text, numbers, and symbols.

1. ***char (n)***: A fixed-length column where the character length is specified by n. If you insert fewer than n characters in any row, PostgreSQL pads the rest of that column with spaces.
2. ***varchar (n)***: A variable-length column where the maximum character length is specified by n. If you insert fewer characters than n, PostgreSQL will not store extra spaces.
3. ***text***: A variable-length column of unlimited length (up to 1 Gb).

```sql
-- Creating a table with character data types
CREATE TABLE char_data_types (
    char_column char(10),
    varchar_column varchar(10),
    text_column text
);

-- Inserting data into the table, matches number of columns
INSERT INTO
    char_data_types
VALUES
    ('abc', 'abc', 'abc'),
    ('def', 'def', 'def');

-- Exporting data to a CSV file
-- COPY ... TO ... exports data from a table to a file
-- COPY ... FROM ... imports data from a file to a table
-- The WITH clause specifies the format of the file
COPY char_data_types TO 'X:\practical-sql-2nd\char_data_types.csv'
WITH (FORMAT CSV, HEADER, DELIMITER '|');
```

```csv
char_column|varchar_column|text_column
abc       |abc|abc
def       |def|def
abc       |abc|abc
defghi    |defghi|defghi
```

The ***varchar*** and ***text*** columns store only the characters you inserted. According to ***PostgreSQL*** documentation, there is no substantial ***difference*** in performance among the three types.

### Understanding Numbers

The SQL number types include the following:

1. ***Integers***: whole numbers, both positive and negative, including zero.
    - ***smallint***: A 2 bytes small integer that can hold values from -32768 to +32767.
    - ***integer***: A 4 bytes integer that can hold values from -2147483648 to +2147483647.
    - ***bigint***: An 8 bytes large integer that can hold values from -9223372036854775808 to +9223372036854775807.
2. ***Fixed-point***
3. ***Floating-point***

Sometimes, it’s helpful to create a column that holds integers that auto increment each time you add a row to the table.

1. ***smallserial***: A ***2 bytes*** small integer that can hold values from 1 to 32767 for auto-numbered identity columns.
2. ***serial***: A ***4 bytes*** integer that can hold values from 1 to 2147483647 for auto-numbered identity columns.
3. ***bigserial***: An ***8 bytes*** large integer that can hold values from 1 to 9223372036854775807 for auto-numbered identity columns.

```sql
CREATE TABLE people (
    id serial,
    person_name varchar(50)
);
```

The ***IDENTITY*** syntax is more verbose, but some database users prefer it for its ***cross-compatibility*** with other database systems.

1. ***GENERATED ALWAYS AS IDENTITY*** tells the database to always fill the column with an auto-incremented value. A user cannot insert a value into the id column without manually overriding that setting.
2. ***GENERATED BY DEFAULT AS IDENTITY*** tells the database to fill the column with an auto-incremented value by default if the user does not supply one.

For now, we’ll stick with the first option, ***using ALWAYS***.
    
```sql
CREATE TABLE people (
    id integer GENERATED ALWAYS AS IDENTITY,
    person_name varchar(50)
);
```

The ***fixed-point*** type is ***numeric(precision,scale)***. You give the argument precision as the maximum number of digits to the ***left and right*** of the decimal point, and the argument scale as the number of digits allowable on the ***right*** of the decimal point.

The ***real*** type allows precision to ***6*** decimal digits, and ***double*** precision to ***15*** decimal digits of precision, both of which include the number of digits on both sides of the point.

```sql
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
    (2.1357987654, 2.1357987654, 2.1357987654)
;

-- Exploring the data
SELECT * FROM number_data_types;
```

#### Choosing a Number Type

1. Use ***integers*** when possible.
2. If you’re working with decimal data and need calculations to be ***exact***, choose ***numeric*** or its equivalent, ***decimal***.
3. Float types will save ***space***, but the ***inexactness*** of floating-point math won’t pass muster in many applications.
4. Choose a ***big enough*** number type.
5. When using numeric or decimal, set the ***precision large enough*** to accommodate the number of digits on ***both sides*** of the decimal point.
6. With whole numbers, use ***bigint*** unless you’re ***absolutely sure*** column values will be ***constrained*** to fit into the ***smaller integer*** or ***smallint*** type.

### Understanding Dates and Times

Whenever you enter a ***date*** into a search form, you’re reaping the benefit of databases having an awareness of the current time (received from the server) plus the ability to handle formats for ***dates***, ***times***, and the nuances of the calendar, such as leap years and time zones.

1. ***timestamp***: Records date and time. Add the keywords with ***time zone*** to ensure that the time recorded for an event includes the time zone where it occurred.
2. ***date***: Records just the date.
3. ***time***: Records just the time.
4. ***interval***: Holds a ***value representing a unit of time*** expressed in the format quantity unit.

```sql
-- Creating a table with date and time data types
CREATE TABLE date_time_types (
    timestamp_column timestamp with time zone,
    interval_column interval
);

-- Inserting data into the table
INSERT INTO
    date_time_types
VALUES
    ('2022-12-31 01:00 EST', '2 days'), -- EST
    ('2022-12-31 01:00 UTC', '1 year'), -- UTC  (Coordinated Universal Time)
    ('2022-12-31 01:00 -8', '1 month'), -- UTC-8
    ('2022-12-31 01:00 Australia/Melbourne', '1 century'), -- Area and location
    (now(), '1 week'); -- Transaction time from hardware

-- Exploring the data
-- pgAdmin reports the date and time relative to my time zone
SELECT * FROM date_time_types;
```

***International Organization for Standardization (ISO)*** format for dates and times: ***YYYY-MM-DD HH:MM:SS***.

### Using the interval Data Type in Calculations

The ***interval data*** type is useful for easy-to-understand ***calculations on date and time data***. Computed columns are called ***expressions***.

```sql
-- Calculating with date and time data types
SELECT
    timestamp_column,
    interval_column,
    timestamp_column - interval_column AS new_date
FROM date_time_types;
```

### Understanding JSON and JSONB

***JSON***, short for ***JavaScript Object Notation***, is a structured data format used for both storing data and exchanging data between computer systems. Organizes information in a collection of ***key/value pairs*** as well as lists of values. Here’s a simple example:

```json
{
    "name": "Jane",
    "age": 30,
    "address": {
        "street": "123 Main Street",
        "city": "New York",
        "state": "NY"
    },
    "children": [
        {
            "name": "Alice",
            "age": 5
        },
        {
            "name": "Bob",
            "age": 8
        }
    ]
}
```

A ***key*** also can have as its value a collection of additional ***key/value pairs***. The ***JSON standard*** enforces rules about formatting, such as separating keys and values with a colon and enclosing key names in double quotes.

1. ***json***: Stores JSON data in a text format.
2. ***jsonb***: Stores JSON data in a binary format. Supports indexing.

### Using Miscellaneous Types

1. ***boolean***: Stores true/false values.
2. ***Geometric types***: include points, lines, circles, and other two-dimensional objects
3. ***Text search types***: include tsvector and tsquery, which are used for full-text search.
4. ***Network address types***: include IP addresses and MAC addresses.
5. ***Universal unique identifier (UUID)***: A 128-bit number used to identify information in computer systems. Sometimes used as a unique key value in tables.
6. ***Range types***: let you specify a range of values like integers, dates, and times.
7. ***Binary data types***: include bytea, which stores binary strings, and bit and bit varying, which store bit strings.
8. ***XML***: stores information in that structured format.

### Transforming Values from One Data Type to Another with CAST

Occasionally, you may need to ***transform*** a value from its stored data type to ***another type***. You can perform these conversions using the ***CAST() function***.

The ***CAST() function*** succeeds only when the target data type can accommodate the original value.

```sql
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
```

### Using CAST Shortcut Notation

However, PostgreSQL also offers a less obvious shortcut notation that takes less space: ***the double colon***.

Insert the ***double colon*** in between the name of the column and the data type you want to convert it to.

```sql
-- Using CAST shortcut notation
SELECT timestamp_column, CAST(timestamp_column AS varchar(10)), timestamp_column::varchar(10)
FROM date_time_types;
```

Use whichever suits you, but ***be aware*** that the ***double colon*** is a ***PostgreSQL-only*** implementation not found in other SQL variants, and so ***won’t port***.
