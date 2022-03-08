import sqlite3 as s

connection = s.connect("Hospital.db")

result = connection.execute("SELECT * FROM DOCTOR")



for i in result:
    print("ID: ", i[0])
    print("Doctor Name: ", i[1])
    print("Qualification: ", i[2])
    print("Address: ", i[3])
    print("Phone Number: ", i[4])
    print("Email: ", i[5])
