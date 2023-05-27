class Vehicle :
	def __init__(self, colour, maxspeed):
		self.colour = colour
		self.maxspeed = maxspeed

	def print(self):
		print(c.colour, end  = " ")

c  = Vehicle("Red", 150)
c.print()
