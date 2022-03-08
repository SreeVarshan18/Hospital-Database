import sqlite3 as s
connection = s.connect("Hospital.db")

connection.execute('''CREATE TABLE PATIENT(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   PATIENT_ID INTEGER,
                   PATIENT_NAME TEXT,
                   ADDRESS TEXT,
                   PHONE_NUMBER INTEGER,
                   EMAIL TEXT,
                   PINCODE INTEGER
                   )''')

print("Table created Successfully")
