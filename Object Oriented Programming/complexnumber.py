class ComplexNumber :
	def __init__(self, real = 0, img = 0):
		self.real = real
		self.img = img

	def mod(self):
		return ((self.real)**2 + (self.img)**2)**(0.5)

	def add(self, c2):
		self.real += c2.real
		self.img += c2.img

	def multiply(self, c2):
		newreal = (self.real)*(c2.real) - (self.img)*(c2.img)
		newimg = (self.real)*(c2.img) + (c2.real)*(self.img)

		self.real = newreal
		self.img  = newimg

	def conjugate(self):
		self.img = -(self.img)

	def divide(self, c2):
		c2.conjugate()
		self.multiply(c2)
		x = (c2.mod())**2
		self.real /= x 
		self.img /= x 


	def print(self):
		if self.img > 0 :
			print(F"{self.real} + {self.img}i")
		else :
			print(F"{self.real} - {abs(self.img)}i")



a, b , c, d = [int(x) for x in input().split()]
c1 = ComplexNumber(a, b)
c2 = ComplexNumber(c, d)
c1.print()
c2.print()
c1.multiply(c2)
print("MULTIPLY")
c1.print()
c2.print()
c2.divide(c1)
print("DIVIDE")
c1.print()
c2.print()
c1.conjugate()
c2.conjugate()
c1.print()
c2.print()
c1.add(c2)
c1.print()
c2.print()
c2.add(c1)
c1.print()
c2.print()

