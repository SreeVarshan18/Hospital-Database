import sqlite3 as s
connection = s.connect("Hospital.db")

connection.execute('''CREATE TABLE DOCTOR(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,              
                   DOCTOR_NAME TEXT,
                   QUALIFICATION TEXT,
                   ADDRESS TEXT,
                   PHONE_NUMBER INTEGER,
                   EMAIL TEXT
                   )''')

print("Table created Successfully")