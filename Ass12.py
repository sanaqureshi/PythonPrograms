# 12.Define a class which has two methods: getString: to get a string from console input.

class IOString():
	def _init_(self):
		self.str1 = ""

	def get_String(self):
		self.str1 = raw_input()

	def print_String(self):
		print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

''' OUTPUT :
[root@python PythonPrograms]# python Ass12.py
Sana Qureshi
SANA QURESHI
'''
