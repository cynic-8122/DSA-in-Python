class ComplexNumber() :
	real = 0
	img = 0

	def __init__(self, real, img) :
		self.real = real
		self.img = img

	def multiply(self, c1, c2) :
		ans = (c1.real)*(c2.real) - (c1.img)*(c2.img)
		return ans

	def display(real) :
		
