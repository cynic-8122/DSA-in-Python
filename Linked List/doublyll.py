class Node :
	def __init__(self, data = None, next = None, prev = None) :
		self.data = data
		self.next = next
		self.prev = prev

class DoublyLL :
	def __init__(self):
		self.head = None
		self.tail = None
		self.__count = 0

	def insertatlast(self, val):
		if self.head == None :
			self.__count += 1
			self.head = Node(val)
			self.tail = self.head
			return

		self.__count += 1

		
		self.tail.next = Node(val, None, self.tail)
		self.tail = self.tail.next

	def insertatbeginning(self, val) :
		if self.__count == 0 :
			self.insertatlast(val)
			return

		self.__count += 1
		self.head.prev = Node(val, self.head)
		self.head = self.head.prev

	def pop(self):
		if self.__count == 0 :
			print("INVALID COMMAND \nLINKEDLIST IS ALREADY EMPTY")
			return

		self.__count -= 1
		t = self.tail.data
		self.tail = self.tail.prev
		self.tail.next = None

		return t

	def popleft(self):
		if self.__count == 0 :
			print("INVALID COMMAND \nLINKEDLIST IS ALREADY EMPTY")
			return

		self.__count -= 1
		t = self.head.data
		self.head = self.head.next
		self.head.prev = None

		return t

	def printll(self):
		if self.head == None :
			return

		ans = ""
		itr = self.head
		while itr.next :
			ans += str(itr.data) + " <-> "
			itr = itr.next

		ans += str(itr.data)
		print(ans)

	def countnodes(self):
		return self.__count

L = DoublyLL()
L.insertatlast(3)
L.insertatbeginning(2)
L.insertatlast(4)
L.printll()
L.insertatlast("End of linked list")
L.insertatbeginning("Start of linked list")
L.printll()
print("Data of the node popped out ", L.popleft())
print("Data of the node popped out ", L.pop())
print(L.countnodes())