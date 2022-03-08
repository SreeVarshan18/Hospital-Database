import sqlite3 as s

connection = s.connect("Hospital.db")

getPhone = input("Enter Phone Number: ")

result = connection.execute("SELECT * FROM DOCTOR WHERE PHONE_NUMBER="+getPhone)

for i in result:
    print("ID: ", i[0])
    print("Doctor Name: ", i[1])
    print("Qualification: ", i[2])
    print("Address: ", i[3])
    print("Phone Number: ", i[4])
    print("Email: ", i[5])
