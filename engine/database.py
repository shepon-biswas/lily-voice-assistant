import sqlite3

connection = sqlite3.connect("lily.db")

cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'Microsoft excel', 'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')"
# cursor.execute(query)
# connection.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null, 'wikipedia', 'https://www.wikipedia.org/')"
cursor.execute(query)
connection.commit()