import pandas as pd
import psycopg

filename = "house price.csv"
data = pd.read_csv(filename, parse_dates=["date"])


try:
    connection = psycopg.connect(
    dbname="House_Pricing",
    user="practice_user",
    password="password",
    host="localhost",
    port="5432"
    )

    cursor = connection.cursor()


    for row in data.itertuples(index=False):
        cursor.execute(
            """
            INSERT INTO housing_prices ( 
                date,  
                price,  
                bedrooms,  
                bathrooms,  
                sqft_living, 
                sqft_lot, 
                floors, 
                waterfront,
                view,
                condition,
                sqft_above,
                sqft_basement,
                yr_built,
                yr_renovated,
                street,
                city,
                statezip,
                country
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s
            )
            """,
            (
                row.date, 
                row.price, 
                row.bedrooms, 
                row.bathrooms, 
                row.sqft_living, 
                row.sqft_lot, 
                row.floors, 
                row.waterfront, 
                row.view, 
                row.condition, 
                row.sqft_above, 
                row.sqft_basement, 
                row.yr_built, 
                row.yr_renovated,
                row.street,
                row.city, 
                row.statezip, 
                row.country
            )
        )

    connection.commit()
    print(f"File \"{filename}\" rows imported successfully!")
    print(f'Imported {len(data)} rows from "{filename}".')

except Exception as e:
    connection.rollback()
    print(f"Import failed: {e}")

finally:
    cursor.close()
    connection.close()

