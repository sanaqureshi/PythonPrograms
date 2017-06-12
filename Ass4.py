# 4. Write a Python program to count the number of lines in a text file.

filename = "text.txt"
numLines = 0
numWords = 0
numChars = 0
with open (filename, 'r') as file:
	for line in file:
		#Let's create a file for words
		wordList = line.split()
		numLines += 1
		numWords += len(wordList)
		numChars += len(line)
print "Lines:%i\n Words:%i\n Characters:%i\n" %(numLines,numWords,numChars)

''' OUTPUT :
[root@python PythonPrograms]# python Ass4.py
Lines:1
Words:56 
Characters:341
'''
