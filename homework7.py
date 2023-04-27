import sqlite3
from sqlite3 import Error

stud_list = [('Сергей', 'Ившин', 'теннис', '1979-01-20', 10, False),
             ('Алексей', 'Савко', 'футбол', '1976-03-22', 8, True),
             ('Светлана', 'Самородова', 'йога', '1986-03-11', 6, True),
             ('Валентин', 'Джунковский', 'путешествия', '1982-07-22', 12, True),
             ('Николай', 'Благонадеждин', 'рыбалка', '1989-01-14', 10, True),
             ('Анна', 'Сметанкина', 'шоппинг', '1991-03-18', 12, False),
             ('Наталья', 'Гарафутдинова', 'йога', '1976-04-28', 8, True),
             ('Александр', 'Паклин', 'фитнес', '1986-01-14', 9, True),
             ('Игорь', 'Тышлин', 'футбол', '1983-07-17', 10, True),
             ('Алексей', 'Полукханов', 'фитнес', '1973-09-03', 14, True),
             ]
db_test = 'db_test.db'
sql_ct = '''
CREATE TABLE IF NOT EXISTS students
(id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
surname TEXT NOT NULL,
hobby TEXT DEFAULT NULL,
date_of_birth DATE NOT NULL,
test_points DOUBLE (3,2) NOT NULL DEFAULT 0.0,
is_married BOOLEAN DEFAULT FALSE);
'''


def create_connection(db=db_test):
    connect = None
    try:
        connect = sqlite3.connect(db)
    except Error:
        print(Error)
    return connect


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error:
        print(Error)


def create_student_rows(conn, students):
    sql = '''INSERT INTO students (name, surname, hobby, date_of_birth, test_points, is_married)
    VALUES (?,?,?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, students)
        conn.commit()
    except Error:
        print(Error)


def reed_students(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def update_student_name(conn, id, name):
    sql = '''UPDATE students SET name=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name, id))
        conn.commit()
    except Error:
        print(Error)


def delete_student_row(conn, id):
    sql = '''DELETE FROM students WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except Error:
        print(Error)


def update_all_data(conn, name, surname, hobby, date_of_birth, test_points, is_married, id):
    sql = '''UPDATE students SET name=?, surname=?, hobby=?, date_of_birth=?, test_points=?, is_married=? WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,(name, surname, hobby, date_of_birth, test_points, is_married, id))
        conn.commit()
    except Error:
        print(Error)

conn = create_connection()

create_table(conn, sql_ct)
create_student_rows(conn, stud_list)
delete_student_row(conn, 2)
update_student_name(conn, 5, 'Артем')
update_all_data(conn,'Максим','Астахов', 'хоккей', '1982-01-20', 22.0, True, 9)
reed_students(conn)