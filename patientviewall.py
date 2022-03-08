import sqlite3 as s

connection = s.connect("Hospital.db")

result = connection.execute("SELECT * FROM PATIENT")

for i in result:
    print("ID: ", i[0])
    print("Patient ID: ", i[1])
    print("Patient Name: ", i[2])
    print("Address: ", i[3])
    print("Phone Number: ", i[4])
    print("Email: ", i[5])
    print("Pincode: ", i[6])

