class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList :
	def __init__(self):
		self.head = None

	def addinbeginning(self, data):
		if self.head :
			self.head = Node(data, self.head)

		else :
			self.head = Node(data)

	def removefrombeginning(self):
		if self.head :
			self.head = self.head.next

		else :
			print(" INVALID COMMAND ")


class Stack :
	def __init__(self, size):
		self.size = size
		self.__ll = LinkedList()
		self.__count = 0

	def push(self, val):
		if self.__count >= self.size :
			print("STACK IS ALREADY FULL ")
			return

		self.__count += 1
		self.__ll.addinbeginning(val)

	def pop(self):
		if self.__count == 0 :
			print("STACK IS EMPTY")
			return

		self.__count -= 1
		temp = self.__ll.head.data
		self.__ll.removefrombeginning()
		print(temp)

	def top(self):
		if self.__count == 0 :
			print("STACK IS EMPTY")
			return

		temp = self.__ll.head.data
		print(temp)

	def IsEmpty(self):
		return self.__count == 0

	def IsFull(self):
		return self.__count == self.size


s = Stack(2)
s.push(5)
s.top()
s.pop()
print(s.IsFull())
print(s.IsEmpty())