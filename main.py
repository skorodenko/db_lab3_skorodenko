import psycopg2
import matplotlib.pyplot as plt

username = 'skorodenko'
password = '1234321'
database = 'postgres'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE OR REPLACE VIEW avg_temp_by_city AS
SELECT c.name, avg(r.temperature) FROM city c
INNER JOIN records r
ON c.id = r.id_city
GROUP BY c.name;
'''
query_2 = '''
CREATE OR REPLACE VIEW count_cities_by_hemispheres AS
SELECT e.name, COUNT(*) FROM city c
INNER JOIN eastwest e
ON e.id = c.id_eastwest
GROUP BY e.name;
'''
query_3 = '''
CREATE OR REPLACE VIEW temperature_year_reykjavik AS
SELECT r.year, r.temperature FROM city c
INNER JOIN records r
ON c.id = r.id_city
WHERE c.name = 'Reykjavik'
ORDER BY r.year;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    cur.execute(query_1)
    cur.execute('SELECT * FROM avg_temp_by_city')
    cities = []
    avg_temp = []
    for row in cur:
        cities.append(row[0])
        avg_temp.append(row[1])
    bar_ax.bar(cities, avg_temp, width=0.5)

    cur.execute(query_2)
    cur.execute('SELECT * FROM count_cities_by_hemispheres')
    labels = []
    count = []
    for row in cur:
        labels.append(row[0])
        count.append(row[1])
    pie_ax.pie(count, labels=labels)

    cur.execute(query_3)
    cur.execute('SELECT * FROM temperature_year_reykjavik')
    year = []
    temp = []
    for row in cur:
        year.append(row[0])
        temp.append(row[1])
    graph_ax.plot(year, temp, marker='o')

plt.show()
