
import sqlite3
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS студент (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    hobby VARCHAR(100) NOT NULL,
    old INTEGER,
    score INTEGER
)
''')

cursor.execute('DELETE FROM студент')

students = [
    (1, 'Aktan', 'Bekov', 2000, 'Reading', 12),
    (2, 'Almaz', 'Avazov', 2001, 'Football', 8),
    (3, 'Lia', 'Khan', 2002, 'Music', 15),
    (4, 'Alina', 'Sadykova', 2000, 'Dance', 10),
    (5, 'Ulan', 'Aliev', 1999, 'Drawing', 7),
    (6, 'Mirbek', 'Atabekov', 2001, 'Chess', 11),
    (7, 'Aisuluu', 'Aidarova', 2000, 'Swimming', 9),
    (8, 'Aibek', 'Tashiev', 2002, 'Running', 13),
    (9, 'Aizada', 'Isaeva', 1998, 'Sewing', 14),
    (10, 'Bekbolot', 'Jumagulov', 1999, 'Cooking', 10)
]

cursor.executemany('''
INSERT INTO студент (id,name,surname,hobby,old,score)
VALUES (?, ?, ?, ?, ?, ?)
''', students)

cursor.execute('''
SELECT * FROM студент WHERE LENGTH(surname) > 10
''')

long_surnames_students = cursor.fetchall()
print("Студенты с фамилией больше 10 символов:")
for student in long_surnames_students:
    print(student)

cursor.execute('''
UPDATE студент SET name = 'genius' WHERE score > 10
''')
cursor.execute('''
SELECT * FROM студент WHERE name = 'genius'
''')
genius_students = cursor.fetchall()
print("Студенты с именем 'genius':")
for student in genius_students:
    print(student)

cursor.execute('''
DELETE FROM студент WHERE id % 2 = 0
''')

cursor.execute('''
SELECT * FROM студент
''')
remaining_students = cursor.fetchall()
print("Оставшиеся студенты:")
for student in remaining_students:
    print(student)

conn.commit()
conn.close()