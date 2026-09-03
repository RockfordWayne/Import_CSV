import pandas as pd
import psycopg

filename = "employees.csv"
data = pd.read_csv("employees.csv")

connection = psycopg.connect(
  dbname="your_database_name",
  user="your_username",
  password="your_password",
  host="your_host",
  port="your_port"
)

cursor = connection.cursor()

for row in data.itertuples(index=False):
    cursor.execute(
        "INSERT INTO employees (id, name, department, salary) VALUES (%s, %s, %s, %s)",
        (row.id, row.name, row.department, row.salary)
    )

connection.commit()

cursor.close()
connection.close()

print(f"File \"{filename}\" rows imported successfully!")