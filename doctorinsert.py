import sqlite3 as s

connection = s.connect("Hospital.db")

getDname = input("Enter Doctor Name: ")
getQuali = input("Enter Qualification: ")
getAddress = input("Enter Address: ")
getPhoneno = input("Enter Phone Number: ")
getEmail = input("Enter Email: ")




connection.execute(" INSERT INTO DOCTOR(DOCTOR_NAME, QUALIFICATION, ADDRESS, PHONE_NUMBER, EMAIL) \
 VALUES('"+getDname+"','"+getQuali+"','"+getAddress+"',"+getPhoneno+",'"+getEmail+"')")
connection.commit()
connection.close()
print("Inserted Successfully")