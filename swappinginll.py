class Node() :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList() :
	def __init__(self) :
		self.head = None

	def insert_at_last(self, data) :
		if self.head is None :
			self.head = Node(data)
			return

		itr = self.head
		while itr.next :
			itr = itr.next

		itr.next = Node(data)

	def insert_at_beginning(self, data) :
		if self.head is None :
			self.head = Node(data) 
			return

		self.head = Node(data, self.head)

	def print(self) :
		if self.head is None :
			print("Linked list is empty")
			return

		itr = self.head
		llstr = ""
		while itr :
			llstr += str(itr.data) + "-->"
			itr = itr.next

		print(llstr)

	def length(self) :
		count = 0
		itr = self.head
		while itr :
			count += 1
			itr = itr.next

		return count

	def swap(self, index_1, index_2) :
		
		if index_1 >= self.length() or index_2 >= self.length() :
			print("INVALID INDEX VALUES")
			return

		count = 0
		itr = self.head
		data_1, data_2 = 0, 0
		while count <= max(index_1, index_2) and itr:
			if count == min(index_1, index_2) :
				data_1 = itr.data

				

			if count == max(index_1, index_2) :
				data_2 = itr.data 
				

			itr = itr.next
			count += 1

		c = str(data_1)
		itr = self.head
		count = 0
		#print(data_1, data_2)
		while count <= max(index_1, index_2) and itr:
			if count == min(index_1, index_2) :
				#print("First if check executed")
				itr.data = data_2
				#print(count, itr.data)

			if count == max(index_1, index_2) :
				#print("Second if check executed")
				itr.data = data_1
				#print(count, itr.data)

			itr = itr.next
			count += 1
		

ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_last(20)
ll.insert_at_beginning(5)
ll.insert_at_last(25)
ll.print()
ll.swap(1, 3)
ll.print() 








