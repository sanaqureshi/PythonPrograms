def max_of_three(a,b,c):
	imax=a
	if(b>imax) and (b>c):
		imax=b
	elif(c>imax):
		imax=c
	return imax

print(max_of_three(4,5,6))
