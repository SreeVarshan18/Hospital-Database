import sqlite3 as s

connection = s.connect("Hospital.db")

getDoctorname = input("Enter Doctor Name: ")

result = connection.execute("SELECT * FROM DOCTOR WHERE DOCTOR_NAME='"+getDoctorname+"'")

for i in result:
    print("ID: ", i[0])
    print("Doctor Name: ", i[1])
    print("Qualification: ", i[2])
    print("Address: ", i[3])
    print("Phone Number: ", i[4])
    print("Email: ", i[5])
