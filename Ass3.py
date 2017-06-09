import sqlite3
conn = sqlite3.connect('employee.db')
c = conn.cursor()

#Create table
c.execute("DROP TABLE IF EXISTS Employee_Details")
c.execute('''CREATE TABLE Employee_Details(Emp_Id, Emp_Name, Salary, Mobile_No)''')
print"Table has created Successfully"

#Insert a row of data
c.execute("INSERT INTO Employee_Details VALUES('50021', 'Sana Qureshi', '25000', 7045186692)")
print "Details inserted succesfully"

#Display data
c.execute("SELECT Emp_Id, Emp_Name, Salary, Mobile_No from Employee_Details")
for row in c:
	print "Emp_Id = " , row[0]
	print "Emp_Name = " , row[1]
	print "Salary = " , row[2]
	print "Mobile_No = " , row[3] , "\n"
print "Details displayed successfully"

#Update Data
c.execute("UPDATE Employee_Details SET Salary = 5000 WHERE Emp_Id = 1")
conn.commit()
print "Table has successfully Updated"
print "No. of Rows Updated : " , conn.total_changes

#Display data
c.execute("SELECT Emp_Id, Emp_Name, Salary, Mobile_No FROM Employee_Details")
for row in c:
	print "Emp_Id = " , row[0]
	print "Emp_Name = " , row[1]
	print "Salary = " , row[2]
	print "Mobile_No = " , row[3] , "\n"
print "Details updated successfully "

#Insert a row
c.execute("INSERT INTO Employee_Details VALUES ('50022', 'Priyanka Lilhare' , '20000' , '9769639922')")
print " Details inserted successfully"

#Display Data
c.execute ("SELECT Emp_Id, Emp_Name, Salary , Mobile_No FROM Employee_Details")
for row in c:
	print "Emp_Id = " , row[0]
	print "Emp_Name = " , row[1]
	print "Salary = " , row[2]
	print "Mobile_No = " , row[3] , "\n"
print "Details updated successfully"

#Delete Data
c.execute("DELETE FROM Employee_Details WHERE Emp_Id = 2 ")
conn.commit()
print "No. of rows deleted : " , conn.total_changes
c.execute("SELECT Emp_Id, Emp_Name, Salary, Mobile_No FROM Employee_Details")
for row in c:
	print "Emp_Id = " , row[0]
	print "Emp_Name = ", row[1]
	print "Salary = " , row[2]
	print "Mobile_No = " , row[3], "\n"
print "Details deleted successfully"

#Display data
c.execute("SELECT Emp_Id, Emp_Name, Salary, Mobile_No FROM Employee_Details")
for row in c:
	print "Emp_Id = ", row[0]
	print "Emp_Name = " , row[1]
	print "Salary = " , row[2]
	print "Mobile_No = " , row[3]
print "Display Updated Details "
conn.commit()
conn.close()
