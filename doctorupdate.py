import sqlite3 as s

connection = s.connect("Hospital.db")

getPhone = input("Enter Phone Number: ")


getNdname = input("Enter New Doctor Name: ")
getNquali = input("Enter New Qualification: ")
getNaddress = input("Enter New Address: ")
getNphoneno = input("Enter New Phone Number: ")
getNemail = input("Enter New Email: ")


result = connection.execute(" UPDATE DOCTOR SET DOCTOR_NAME='"+getNdname+"', QUALIFICATION='"+getNquali+"', \
ADDRESS='"+getNaddress+"', PHONE_NUMBER="+getNphoneno+", EMAIL='"+getNemail+"' WHERE PHONE_NUMBER="+getPhone)
connection.commit()
print("Updated Successfully")
