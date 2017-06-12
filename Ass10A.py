# 10.Define a function that computes the length of a given list or string.

def countStringLength(inputString):
	count = 0
	for i in inputString:
		count = count+1
	print ("Length of the String is " +str(count))
print ("Enter string")
inputString = raw_input()
countStringLength(inputString)

''' OUTPUT :
[root@python PythonPrograms]# python Ass10A.py
Enter string
Sana Qureshi
Length of the String is 12
'''
