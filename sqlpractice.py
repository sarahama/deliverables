import sqlite3

db = sqlite3.connect(':memory:')
db = sqlite3.connect('mydb')

cursor = db.cursor()
#cursor.execute('''
#    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
#                       phone TEXT, email TEXT, password TEXT)
#''')

name1 = 'Sarah'
phone1 = '5555555'
email1 = 'sarah@virginia.edu'
# A very secure password
password1 = '12345'
 
name2 = 'John'
phone2 = '5557241'
email2 = 'john@example.com'
password2 = 'abcdef'

name3 = 'A'
phone3 = '5557221'
email3 = 'a@example.com'
password3 = 'abcde1'

name4 = 'B'
phone4 = '5557991'
email4 = 'b@example.com'
password4 = 'abcde2'

name5 = 'C'
phone5 = '5558741'
email5 = 'c@example.com'
password5 = 'abcde3'

users = [(name1, phone1, email1, password1),
	 (name2, phone2, email2, password2),
	 (name3, phone3, email3, password3),
         (name4, phone4, email4, password4),
         (name5, phone5, email5, password5)]
 
# Insert user 1
cursor.executemany('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', users)
print('Users inserted')

db.commit()
