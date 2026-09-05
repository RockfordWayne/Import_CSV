# Import_CSV
A small Python app to read CSV data and insert it into a SQL database.

This project was created to practice working with Python, SQL, PostgreSQL, and CSV files.

## Technology Used

- Python
- Pandas
- Psycopg
- PostgreSQL

## Project Overview

- "CSV_ImportTool.py"  -   This is the Python script that facilitates moving the data from a CSV file to a SQL database (in this case PostgreSQL) where a table has already been created.
- house price.csv"  -  This is the CSV file the python app will be utilizing.
- "Housing_Prices_table_creation.sql"  -  This is a SQL script that you can run in PostgreSQL to create the table that will receive the data from the CSV file.

## How It Works

- Pandas reads the data from the CSV file.
- Psycopg connects to PostgreSQL.
- Each row is inserted into the "housing_prices" table (or what the user decides to name it. Make sure to update the Python script if a custom file/name is used)
- The transaction commits if all rows are successfully imported
- If an error occurs, a rollback will happen

## Setup

Two packages must be installed that Python can utilize

**Windows**
Pandas
```powershell
py -m pip install pandas
```

Psycopg
```powershell
py -m pip install psycopg[binary]
```

- Create the PostgreSQL table using the "Housing_Prices_table_creation.sql" script. Pull it into your query tool and run it to generate the table.

- Update the database connection setting in the Python script to match your local PostgreSQL. (WARNING: This is for testing or practice purposes. This is not a secure way to run this.)

Run:

**Powershell**
```powershell
py CSV_ImportTool.py
```

Either a success or failure message will appear.

## Future Additions

- Move the database credentials to environment variables.
- Improve import performance for large datasets
- Add additional data validation
- Add other formats besides CSV
- Add a visual interface or command line options for file selection or column names