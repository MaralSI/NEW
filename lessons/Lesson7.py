# БАЗА ДАННЫХ
# crud
# SQL noSQL
# СУБД -система управления базами данных
# relation

import sqlite3

db = sqlite3.connect('group43.db')

cursor = db.cursor()


cursor.execute('''
CREATE TABLE users(
    name VARCHAR(100) NOT NULL,
    age DATE DEFAULT 0,
    password TEXT
)''')


db.commit()
db.close()