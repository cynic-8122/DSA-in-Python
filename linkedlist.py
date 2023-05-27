class Node():
	def __init__(self, data = None, next = None) :
		self.data = data
		self.next = next 

class LinkedList() :
	def __init__(self) :
		self.head = None

	def insert_at_beginning(self, data) :
		head = Node(data, self.head)
		self.head = head

	def print(self) :
		llstr = ""
		itr = self.head
		while itr :
			llstr += str(itr.data) + "-->"
			itr = itr.next

		print(llstr)

	def insert_at_last(self, data) :

		node = Node(data)
		if self.head is None :
			self.head = node

		else :
			itr = self.head
			while itr.next :
				itr = itr.next
			itr.next = node
	def length(self) :
		count = 0
		itr = self.head 
		while itr :
			count += 1
			itr = itr.next 
		return count 

	def insert_at_index(self, index_value, value) :
		if index_value == 0 :
			insert_at_beginning(value)
			return
		if index_value < 0 and index_value >= -(self.length()):
			index_value += self.length() 

		if index_value >= self.length() :
			insert_at_last(value)
			return

		if index_value < -(self.length()) :
			print("INVALID INDEX")
			return
		count = 0 
		itr = self.head 
		while itr :
			if count == (index_value - 1):
				itr.next = Node(value, itr.next)
				break
			itr = itr.next
			count += 1

	def insert_after_value(self, data_after, data_to_insert):
		check = True
		itr = self.head
		while itr :
			if itr.data == data_after :
				check = False
				itr.next = Node(data_to_insert, itr.next)
				break
			itr = itr.next
		if check :
			print("GIVEN VALUE DOES NOT EXIST")

	def remove_by_value(self, value):
		check = True
		itr = self.head
		if self.head.data == value :
			self.head = itr.next
			return
		while itr.next :
			if itr.next.data == value :
				check = False
				itr.next = itr.next.next
				break
			itr = itr.next
		if check :
			print("GIVEN VALUE DOES NOT EXIST")
	def insert_values(self, data_list) :
		for i in range(len(data_list)):
			a = data_list[i]
			self.insert_at_last(a)

ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()
ll.remove_by_value("orange") # remove orange from linked list
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple") 
ll.remove_by_value("grapes")
ll.print()










