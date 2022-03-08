import sqlite3 as s

connection = s.connect("Hospital.db")

getPid = input("Enter Patient ID: ")
getPname = input("Enter Patient Name: ")
getAddress = input("Enter Address: ")
getPhoneno = input("Enter Phone Number: ")
getEmail = input("Enter Email: ")
getPincode = input("Enter Pincode: ")



connection.execute(" INSERT INTO PATIENT(PATIENT_ID, PATIENT_NAME, ADDRESS, PHONE_NUMBER, EMAIL, PINCODE) \
 VALUES("+getPid+",'"+getPname+"','"+getAddress+"',"+getPhoneno+",'"+getEmail+"',"+getPincode+")")
connection.commit()
connection.close()
print("Inserted Successfully")