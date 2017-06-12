# 6. Write a program that takes inputs from user their name and their age. And display the year in which they will turn 100 years old.

name = raw_input("Enter Your Name : ")
age = int(raw_input("Enter Your age : "))
year = str((2017 - age)+100)
print(name + " will be 100 years old in the year " + year)

''' OUTPUT :
[root@python PythonPrograms]# python Ass6.py
Enter Your Name : Sana Qureshi
Enter Your age : 24
Sana Qureshi will be 100 years old in the year 2093
'''
