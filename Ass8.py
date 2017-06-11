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
