class Node() :
	def __init__(self, data = None, next = None) :
		self.data = data
		self.next = next

class LinkedList() :
	def __init__(self) :
		self.head = None

	def merge_k_sorted_lists(self, lists) :
		if self.head is None :
			self.head = Node(lists[0][0])
			itr = self.head
			for i in range(1, len(lists[0])) :
				print(f"inserting {lists[0][i]} after {itr.data}")
				itr.next = Node(lists[0][i])
				itr = itr.next

		for i in range(1, len(lists)) :
			itr =  self.head
			j = 0
			while j < len(lists[i]) and itr.next:
				if itr.data <= lists[i][j] :
					if itr.next.data > lists[i][j] :
						print(f"inserting {lists[i][j]} after {itr.data}")
						itr.next = Node(lists[i][j], itr.next)
						itr = itr.next
						j += 1
					else :
						itr = itr.next
				else :
					print(f"inserting {lists[i][j]} before {self.head.data}")
					self.head = Node(lists[i][j], self.head)
					itr = self.head
					j += 1

			if itr.next == None and j < len(lists[i]) :
				while j < len(lists[i]) :
					print(f"inserting {lists[i][j]} after {itr.data}")
					self.print
					itr.next = Node(lists[i][j])
					itr = itr.next
					j += 1

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

ll = LinkedList()
lists = [[]]
ll.merge_k_sorted_lists(lists)
ll.print()


