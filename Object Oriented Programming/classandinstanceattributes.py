class Student :
	name = "Chandanpreet Singh"
	def add_age(self):
		self.age = 19

	def print_age(self):
		print(self.age)

	@staticmethod
	def isteen(age):
		return age > 16


s1 = Student()
s1.add_age()
print(s1.isteen(15))
#print(s1)
s1.print_age()
s2 = Student()
#print(s2)
s2.print_age()
