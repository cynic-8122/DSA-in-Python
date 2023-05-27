class Node :
	def __init__(self, data = None, next = None ):
		self.data = data
		self.next = next

class LinkedList :
	def __init__(self):
		self.head = None
		self.tail = None

	def addatlast(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head
			return

		self.tail.next = Node(data)	
		self.tail = self.tail.next

	def arrtoll(self, arr):
		if len(arr) == 0 :
			return

		for i in range(len(arr)):
			self.addatlast(arr[i])

	def print(self):
		itr = self.head
		ans = ""
		while itr.next :
			ans += str(itr.data) + " -> "
			itr = itr.next

		ans += str(itr.data)
		print(ans)

	def search(self, val):
		if self.head == None :
			print(-1)
			return

		itr = self.head
		while itr :
			if itr.data == val :
				print("Found the match ")
				return

			itr = itr.next

		print(-1)

arr = [int(x) for x in input().split()]
LL = LinkedList()
LL.arrtoll(arr)
LL.print()
LL.search(5)


