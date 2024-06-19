
# база данных
# crud
# SQL noSQL
# СУБД - система управления базами данными
# relation -

import sqlite3

# with__
# conn = sqlite3.connect('')
db = sqlite3.connect('group43.db')

cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(100) NOT NULL,
    age DATE DEFAULT 0,
    password TEXT   
)''')

# read
# select\ fetch
cursor.execute('''SELECT * FROM users''')
for row in cursor.fetchall():
    print(row)

# create
cursor.execute('''INSERT INFO users(name,age,password
                                VALUES ('fbjfdkf', 20, 'dsfd')  ''')

# UPDATE

cursor.execute('''UPDATE users SET name="крутой прогер", age=11 WHERE rowid %2  ''')


# DELETE
cursor.execute('''DELETE FROM users WHERE password<7''')
db.commit()
db.close()




#
#

#