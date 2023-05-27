class Node():
	def __init__(self, data, next = None, prev = None) :
		self.data = data
		self.next = next
		self.prev = prev

class LinkedList() :
	def __init__(self) :
		self.head = None 
		self.tail = None

	def insert_at_last(self, data) :
		if self.head is None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.tail.next = Node(data, None, self.tail)
		self.tail = self.tail.next

	def insert_at_beginning(self, data) :
		if self.head is None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.head.prev = Node(data, self.head)
		self.head = self.head.prev


	def print_forward(self) :
		if self.head is None and self.tail is None :
			print("Linked list is empty")
			return
		itr = self.head
		llstr = ""
		while itr :
			llstr += str(itr.data) + "-->"
			itr = itr.next 

		print(llstr)

	def print_reversed(self) :
		if self.tail is None and self.head is None :
			print("Linked list is empty")
			return
		itr = self.tail
		llstr = ""
		while itr :
			llstr += str(itr.data) + "<--"
			itr = itr.prev

		print(llstr)

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_last(20)
ll.insert_at_beginning(5)
ll.insert_at_last(25)
ll.print_forward()
ll.print_reversed()





