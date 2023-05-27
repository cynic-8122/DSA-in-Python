class Node :
	def __init__(self, data = None, next = None) :
		self.data = data
		self.next = next

class LinkedList :
	def __init__(self):
		self.head = head
		self.tail = tail

	def insertatlast(self, val):
		if self.head == None :
			self.head = Node(val)
			self.tail = self.head
			return

		self.tail.next = Node(val)
		self.tail = self.tail.next

	def dequeue(self):
		if self.head == None :
			print("INVALID COMMAND ")
			return

		temp = self.head.data
		self.head = self.head.next
		return temp

class Queue :
	def __init__(self):
		self.__ll = LinkedList()
		self.__count = 0

	def isEmpty(self):
		return self.__count == 0

	def enqueue(self, data):
		self.__count += 1
		self.__ll.insertatlast(data)

	def dequeue(self):
		if self.isEmpty() :
			print("INVALID COMMAND ")
			return

		self.__count -= 1 
		return self.__ll.dequeue()

	def front(self):
		if self.isEmpty() :
			print("QUEUE IS EMPTY ")
			return

		return self.__ll.head.data 


class Stack :
	def __init__(self):
		self.__q1 = Queue()
		self.__q2 = Queue()
		self.__count = 0

	def push(self, val):
		


