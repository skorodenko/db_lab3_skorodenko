import csv
import decimal
import psycopg2

username = "skorodenko"
password = "1234321"
database = "postgres"
host = "localhost"
port = "5432"

INPUT_CSV = "kaggle_data.csv"

# Дані імпортуються через .sql файл, тому тут приведу тільки приклад.
insert_query = "INSERT INTO country (name) VALUES (%s);"

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    with open(INPUT_CSV, "r") as inf:
        reader = csv.DictReader(inf)
        unique_city_names = {row["Country"] for row in reader}
        for city in unique_city_names:
            cur.execute(insert_query, city)

    conn.commit()
