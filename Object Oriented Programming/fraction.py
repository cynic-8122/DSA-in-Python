def HCF(a, b):
	if a == 0:
		return b

	return HCF(b%a, a)
class Fraction :
	def __init__(self, num = 0, den = 1):
		self.num = num
		self.den = den

	
	def simplify(self):
		x = HCF(self.num, self.den)
		self.num = self.num//x 
		self.den = self.den//x 

	def print(self):
		if self.den == 0 :
			print("INVALID")

		elif self.num == 0 or self.den == 1 :
			print(self.num)
			
		else:
			print(f"{self.num}/{self.den}")

a, b = [int(x) for x in input().split()]
f = Fraction(a, b)
f.simplify()
f.print()




