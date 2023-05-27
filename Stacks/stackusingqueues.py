class Queue :
	def __init__(self):
		self.arr = []
		self.__count = 0

	def push(self, value):
		self.__count += 1
		self.arr.append(value)

	def pop(self):
		if self.__count == 0:
			print("Queue is empty already ")
			return

		self.__count -= 1
		return self.arr.pop(0)

	def isEmpty(self):
		return self.__count == 0

	def Size(self):
		return self.__count

Q1 = Queue()
Q2 = Queue()

'''
method1: Making the push function more costly
'''
arr = [int(x) for x in input().split()]

for x in arr :
	Q2.push(x)
	while not Q1.isEmpty() :
		Q2.push(Q1.pop())

	#print(Q1.isEmpty())
	#print(Q2.arr)
	Q1, Q2 = Q2, Q1

while not Q1.isEmpty() :
	print(Q1.pop())

'''
metod 2 ;
Making the pop fuction costly 
'''
print("____________________________________________")
Q1new = Queue()
Q2new = Queue()

for x in arr :
	Q1new.push(x)

while not Q1new.isEmpty() :
	t = Q1new.pop()
	if Q1new.isEmpty() :
		print(t)
		Q1new, Q2new = Q2new, Q1new

	else :
		Q2new.push(t)

	