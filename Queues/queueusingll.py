class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList :
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head

		self.tail.next = Node(data)
		self.tail = self.tail.next

	def dequeue(self):
		if self.head == None :
			print("INVALID COMMAND ")
			return

		temp = self.head.data
		self.head = self.head.next
		return temp


class Queue :
	def __init__(self, maxsize = 0):
		self.maxsize = maxsize 
		self.__count = 0
		self.__ll = LinkedList()

	def enqueue(self, val):
		if self.__count >= maxsize :
			print("QUEUE IS FULL ")
			return

		self.__ll.enqueue(val)
		self.__count += 1

	def dequeue(self):
		if self.__count <= 0 :
			print("INVALID COMMAND ")
			return

		self.__count -= 1
		return self.__ll.dequeue()

	def size(self):
		return self.__count 

	def front(self):
		if self.__count <= 0 :
			print("QUEUE IS EMPTY ")
			return
			
		return self.__ll.head.data

	def rear(self):
		if self.__count <= 0 :
			print("QUEUE IS EMPTY ")
			return
		return self.__ll.tail.data

	def isEmpty(self):
		return self.size() == 0


