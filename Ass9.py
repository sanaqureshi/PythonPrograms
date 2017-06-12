# 9. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max_of_three(a,b,c):
	imax=a
	if(b>imax) and (b>c):
		imax=b
	elif(c>imax):
		imax=c
	return imax

print(max_of_three(4,5,6))

''' OUTPUT :
[root@python PythonPrograms]# python Ass9.py
6
'''
