# БАЗА ДАННЫХ
# crud
# SQL noSQL
# СУБД -система управления базами данных
# relation

import sqlite3
db = sqlite3.connect('group43.db')
cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(100) NOT NULL,
    age DATE DEFAULT 0,
    password TEXT
)''')

# create
#
# cursor.execute('''INSERT INTO users (name,age,password)
#                                 VALUES ('beka2',21, 'qwerty')''')
#
# cursor.execute('''INSERT INTO users (name,age,password)
#                                 VALUES ('beka3',22, 'qwerty')''')
#
# cursor.execute('''INSERT INTO users (name,age,password)
#                                 VALUES ('beka4',23, 'qwerty')''')


# update

cursor.execute('''UPDATE users SET name="крутой прогер" WHERE rowid %2  ''')

# DELETE
cursor.execute(''' DELETE FROM users WHERE password<7''')

# read
# SELECT \fetch
cursor.execute('''SELECT rowid,* FROM users''')
for row in cursor.fetchall():
    print(row)
##
db.commit()
db.close()
