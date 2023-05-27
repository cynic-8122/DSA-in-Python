class Node:
	def __init__(self, data, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def addnode(self, val):
		if self.head == None:
			self.head = Node(val)
			return

		itr = self.head
		while itr.next:
			itr = itr.next

		itr.next = Node(val)

	def print(self):
		itr = self.head

		while itr:
			print(f"{itr.data}->", end = " ")
			itr = itr.next


	def makell(self, arr):
		for x in arr:
			self.addnode(x)


def swapnodes(idx1, idx2, head):
	itr = head
	prev1 = None
	prev2 = None
	next1 = None
	next2 = None
	while itr:
		if itr.next == idx1 :
			prev1 = itr

		if itr.next == idx2:
			prev2 = itr

		if itr == idx
	#if nodes are next to each other
	if idx1 + 1 == idx2 :




