def intersect(a,b):
	"""return the intersection of two lists """
	return list(set(a) & set(b))
if _name_ == "_main_" :
	a=[1,3,6,78,35,55]
	b=[12,24,35,24,88,120,155]
	print intersect(a,b)
