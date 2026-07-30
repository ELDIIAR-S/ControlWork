import sqlite3

connection = sqlite3.connect("cinema.db")

with open("cinema.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

connection.executescript(sql_script)
connection.commit()
connection.close()

print("База данных успешно создана")