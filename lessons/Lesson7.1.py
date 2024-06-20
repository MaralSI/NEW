import sqlite3

with sqlite3.connect('saper.db') as con:
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    sex INTEGER DEFAULT 1,
    old INTEGER,
    score INTEGER
         )''')

    cur.execute('''INSERT INTO users(name, sex,old,score)
    VALUES('beka2', 2, 15,234324), ('beka2', 2, 15,234324), ('beka2', 2, 15,234324)''')


    cur.execute('''SELECT * FROM users''')
    for row in cur.fetchall():
        print(row)

