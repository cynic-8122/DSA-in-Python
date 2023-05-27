class Stack :
	def __init__(self):
		self.__arr = []
		self.__count  = 0

	def push(self, val):
		self.__arr.append(val)
		self.__count += 1

	def pop(self):
		if self.__count <= 0 :
			print("INVALID COMMAND ")
			return
		
		self.__count -= 1
		return self.__arr.pop()

	def top(self):
		if self.__count <= 0 :
			print("QUEUE IS EMPTY ")
			return

		return self.__arr[-1]

	def isEmpty(self):
		return self.__count == 0

class Queue :
	def __init__(self):
		self.__s1 = Stack()
		self.__s2 = Stack()
		self.__count = 0
		self.__front = None

	def enqueue(self, val):
		if self.isEmpty() :
			self.__front = val

		self.__count += 1
		self.__s1.push(val)

	def dequeue(self):
		if self.__count == 0 :
			print("CAREFUL BITCH \nQueue is empty ")
			return

		self.__count -= 1
		if self.__s2.isEmpty() :
			while not self.__s1.isEmpty() :
				self.__s2.push(self.__s1.pop())

			return self.__s2.pop()

		return self.__s2.pop()

	def isEmpty(self):
		return self.__s1.isEmpty() and self.__s2.isEmpty()
		
'''
	def rear(self):
		if self.isEmpty() :
			print("CAREFUL BITCH \nQueue is empty ")
			return

		return self.__s1.top()
'''

	def front(self):
		if self.isEmpty() :
			print("CAREFUL BITCH \nQueue is empty ")
			return

		if self.__s2.isEmpty() :
			return self.__front 

		return self.__s2.top()

Q = Queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print(Q.dequeue())
print(Q.front())
#print(Q.rear())

while not Q.isEmpty() :
	print(Q.dequeue())




