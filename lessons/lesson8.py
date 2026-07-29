import sqlite3


connect = sqlite3.connect('grades.db')
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (20) NOT NULL,
        age INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grade(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        grade INTEGER NOT NULL,
        subject VARCHAR(30) NOT NULL,
        student_id INTEGER NOT NULL,
        FOREIGN KEY (student_id) REFERENCES student(id)
    )
''')
connect.commit()

def create_data():
    # data = [
    #     ('ARDAGER', 11),
    #     ('OLEG',12),
    #     ('OLEG',14),
    #     ('SLAVA',15)
    # ]
    # cursor.executemany(
    #     'INSERT INTO student (name, age) VALUES (?, ?)',
    #     data
    # )
    data = [
        ('Алгебра', 5, 2),
        ('Физика', 5, 3),
    ]
    cursor.executemany(
        'INSERT INTO grade (subject, grade, student_id) VALUES (?, ?, ?)',
        data
    )
    connect.commit()
    print('Студенты добавлены!!')
# create_data()


def get_student_grade():
    cursor.execute('''
    SELECT student.name, grade.grade, grade.subject 
    FROM student FULL OUTER JOIN grade ON student.id = grade.student_id
    ''')
    data = cursor.fetchall()
    for i in data:
        print(f"{i[0]} - {i[1]} - {i[2]}")

# get_student_grade()



def  get_old_student():
    # MAX, MIN, AVG, COUNT, SUM
    cursor.execute('SELECT COUNT(age) FROM student')
    data = cursor.fetchall()

    print(data)
# get_old_student()

def get_best_student():
    cursor.execute(
        '''
        SELECT name FROM student WHERE id IN (
            SELECT student_id FROM grade WHERE grade = 5
            )
        '''
    )
    data = cursor.fetchall()
    print(data)

# get_best_student()

def create_my_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
            SELECT name FROM student WHERE id IN (
            SELECT student_id FROM grade WHERE grade = 5
            )
    ''')
    print("редставление создано")
    connect.commit()

# create_my_view()

def get_view():
    cursor.execute('SELECT * FROM my_view')
    data = cursor.fetchall()
    print(data)

get_view()