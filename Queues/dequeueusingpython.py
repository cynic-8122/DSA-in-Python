class Node :
	def __init__(self, data = None, next = None, prev = None) :
		self.data = data
		self.next = next
		self.prev = prev

class DoublyLinkedList :
	def __init__(self):
		self.head = None
		self.tail = None

	def insertatlast(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.tail.next = Node(data, None, self.tail)
		self.tail = self.tail.next

	def insertatbeginning(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.head.prev = Node(data, self.head)
		self.head = self.head.prev


class Dequeue :
	def __init__(self):
		self.__count = 0
		self.__dll = DoublyLinkedList()

	def isEmpty(self):
		return self.__count == 0

	def insertrear(self, val):
		self.__count += 1
		self.__dll.insertatlast(val)

	def insertfront(self, val):
		self.__count += 1
		self.__dll.insertatbeginning(val)

	def front(self):
		if self.isEmpty() :
			print("DEQUEUE IS EMPTY ")
			return

		return self.__dll.head.data

	def rear(self):
		if self.isEmpty() :
			print("DEQUEUE IS EMPTY ")
			return

		return self.__dll.tail.data

	def deletefront(self):
		if self.isEmpty() :
			print("DEQUEUE IS EMPTY \nCAN'T DELETE FRONT ELEMENT ")
			return

		self.__count -= 1
		temp = self.__dll.head.data
		self.__dll.head = self.__dll.head.next
		return temp

	def deleterear(self):
		if self.isEmpty() :
			print("DEQUEUE IS EMPTY \nCAN'T DELETE REAR ELEMENT ")
			return

		self.__count -= 1
		temp = self.__dll.tail.data
		self.__dll.tail = self.__dll.tail.prev
		return temp

	def size(self):
		return self.__count

		





