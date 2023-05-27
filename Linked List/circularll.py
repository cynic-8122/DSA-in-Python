class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next 

class CircularLL :
	def __init__(self, maxsize):
		self.head = None
		self.tail = None
		self.maxsize = maxsize
		self.__count = 0

	def insertNode(self, val):
		if self.head == None :
			self.head = Node(val)
			self.tail = self.head
			self.__count += 1
			return

		if self.__count >= self.maxsize :
			print('LINKED LIST IS FULL ')
			return

		self.__count += 1

		self.tail.next = Node(val, self.head)
		self.tail = self.tail.next

	def insertatbeginning(self, val):
		if self.head == None :
			self.head = Node(val)
			self.tail = self.head
			self.__count += 1
			return

		if self.__count >= self.maxsize :
			print('LINKED LIST IS FULL ')
			return

		self.__count += 1

		self.tail.next = Node(val, self.head)
		self.head = self.tail.next

	def removenodefrombeginning(self):
		if self.__count == 0 :
			print('The linked list is empty already ')
			return

		self.__count -= 1

		t = self.head.data
		self.head = self.head.next
		self.tail.next = self.head

		return t

	def removenodefromlast(self):
		if self.__count == 0 :
			print('The linked list is empty already ')
			return

		self.__count -= 1

		t = self.tail.data
		itr = self.head
		while itr.next != self.tail :
			itr = itr.next

		self.tail = itr 
		self.tail.next = self.head
		return t 

	def printll(self):
		if self.head == None :
			return

		ans = ""
		itr = self.head
		while itr != self.tail : 
			ans += str(itr.data) + " -> "
			itr = itr.next

		ans += str(itr.data)
		print(ans)

	def countnodes(self):
		return self.__count

L = CircularLL(4)
L.insertNode(10)
L.insertatbeginning(21)
L.insertNode(43)
L.printll()
L.insertNode("End of linked list")
L.insertatbeginning("Start of linked list")
L.printll()
print("Data of the node popped out ", L.removenodefromlast())
print("Data of the node popped out ", L.removenodefrombeginning())
L.printll()
print(L.countnodes())



		

