import sqlite3

# A4
connect = sqlite3.connect("users.db")
# Карандаш с рукой
cursor = connect.cursor()
#
#
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (30) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT
    )
''')
# connect.commit()
#
# # CRUD Create-Read-Update-Delete
#
#
#
# def create_user(name, age, hobby):
#     # cursor.execute(f'''
#     #     INSERT INTO user(name, age, hobby)
#     #     VALUES ("{name}", "{age}", "{hobby}")
#     # ''')
#     cursor.execute(
#         'INSERT INTO user(name, age, hobby) VALUES(?,?,?)',
#         (name, age, hobby)
#     )
#     connect.commit()
#     print('пользователь создан!!')
#
# # create_user("Ardager", 20, "Спать")
# # create_user("Slava", 21, "Плавать")
# # create_user("Oleg", 22, "Лыжи")
# # create_user("Vasya", 23, "Горы")
# # create_user("Игорь", 24, "Дорамы-Аниме!!")
#
async def read_users():
    cursor.execute('SELECT hobby, name FROM user WHERE age > 23')
    data = cursor.fetchmany(5)
    print(data)
    # for i in data:
    #     print(f"NAME: {i[0]}, AGE: {i[1]}, HOBBY: {i[2]}")
#
 read_users()
#
# def update_user(new_name, rowid):
#     cursor.execute(
#         'UPDATE user SET name = ? WHERE rowid = ?',
#         (new_name, rowid)
#     )
#     connect.commit()
#     print('user updated!!')
#
# # update_user('Ardager', 3)
#
# def delete_user(name):
#     cursor.execute('DELETE FROM user WHERE  id = ?', (name,))
#     connect.commit()
#     print('user deleted!!')
#
# delete_user(3)
#


test = [1]
test2 = (1,)
test3 ={
    "key": 123
}


def tests():
    a = 1
    b = "test"
    c = "test2"