import sqlite3

# Add connection to Data
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE Date='2088'")
rows1 = cursor.fetchall()


# Query certain data
cursor.execute("SELECT Band, Date FROM events WHERE Date='2088'")
rows2 = cursor.fetchall()

print(rows1)
print(rows2)

new_rows = [('Cat', 'Cat City', '2088')]

# Insert values new_rows into Data
rows3 = cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

