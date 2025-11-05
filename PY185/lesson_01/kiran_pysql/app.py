import psycopg2

connection = psycopg2.connect(dbname = 'films')

cursor = connection.cursor()
cursor.execute('SELECT * FROM directors')

rows = cursor.fetchall()
print(rows[0])

cursor.close()
connection.close()

