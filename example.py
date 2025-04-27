import sqlite3

# Add connection to Data
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE Date='2088'")
now = cursor.fetchall()


# Query certain data
cursor.execute("SELECT Band, Date FROM events WHERE Date='2088'")
rows = cursor.fetchall()

print(now)
print(rows)
