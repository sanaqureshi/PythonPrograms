# 8. Define a function max() that takes two numbers as arguments and returns the largest of them.

def max(firstNo, secondNo):
	if firstNo > secondNo :
		return firstNo
	else :
		return secondNo

def getNumbersFromUser():
	FirstNumber = int(input("Enter First Number :"))
	SecondNumber = int(input("Enter Second Number :"))
	return FirstNumber, SecondNumber

def main():
	FirstNumber, SecondNumber = getNumbersFromUser()
	print('The Maximum Number Is : ', max(FirstNumber, SecondNumber))
main()

''' OUTPUT :
[root@python PythonPrograms]# python Ass8.py
Enter First Number :7
Enter Second Number :8
('The Maximum Number Is : ', 8)
'''
