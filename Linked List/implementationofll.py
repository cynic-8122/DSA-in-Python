class Node :
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList :

	def __init__(self) :
		self.head = None
		self.tail = None

	def addatlast(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head

		else :
			self.tail.next = Node(data)
			self.tail = self.tail.next
			

	def addatbeginning(self, data):
		if self.head == None :
			self.head = Node(data)

		else :
			self.head = Node(data, self.head)

	def print(self):
		if self.head == None :
			return

		ans = ""
		itr = self.head
		while itr.next :
			ans += str(itr.data) + "->"
			itr = itr.next

		ans += str(itr.data)
		print(ans)

	def listtoll(self, arr):
		if len(arr) == 0:
			return

		if len(arr) == 1:
			self.addatlast(arr[0])
			return

		for i in range(len(arr)):
			self.addatlast(arr[i])

	def insertat(self, idx, data):
		if idx == 0 :
			self.addatbeginning(data)
			return
		itr = self.head
		while  idx - 1 and itr :
			itr = itr.next
			idx -= 1

		if itr :
			itr.next = Node(data, itr.next)
			return

		self.addatlast(data)

	def deletenode(self, idx) :
		if idx == 0 :
			self.head = self.head.next
			return

		itr = self.head
		while idx - 1 and itr :
			itr = itr.next
			idx -= 1

		if itr.next :
			itr.next = itr.next.next

	def insert_at_irecusive(self, i, data, head):
		if i == 0 :
			self.head = Node(data, self.head)
			return 

		if i == 1:
			head.next = Node(data, head.next)
			return
		if head.next :
			self.insert_at_irecusive(i - 1, data, head.next)

		else :
			head.next = Node(data)

	def delete_ith(self, i, head):
		if i == 0:
			self.head = self.head.next
			return

		if i == 1 :
			head.next = head.next.next
			return

		if head.next == None :
			return

		self.delete_ith(i - 1, head.next)

print("Enter the data seperated by spaces which you wish to be included in the Linked List ")
arr = [int(x) for x in input().split()]
LL  = LinkedList()
LL.listtoll(arr)
print("Linked List :")
LL.print()
print("Tail points to :", LL.tail.data)
X = int(input("Enter the index you wish to insert at : "))
LL.insert_at_irecusive(X, f"Got inserted at {X}", LL.head)
print("Linked List :")
LL.print()
LL.delete_ith(4, LL.head)
print("4th node is deleted ")
LL.print()



