def remove_even(l):
	for i in l:
		if i%2!=0:
			l.remove(i)
	print l
	return l
remove_even([5,6,77,45,22,12,24])
remove_even([4,5,4,7,9,11])
remove_even([5,6,77,45,22,12,24])
