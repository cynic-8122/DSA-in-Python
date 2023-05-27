class Stack:
	def __init__(self):
		self.arr = []

	def isEmpty(self):
		return len(self.arr) == 0

	def push(self, val):
		self.arr.append(val)

	def pop(self):
		return self.arr.pop()

class Node :
	def __init__(self, data = None, left = None, right = None):
		self.left = left
		self.right = right
		self.data = data

class BST:
	def __init__(self):
		self.head = None

	def addNode(self, val, itr):
		if self.head == None :
			self.head = Node(val)
			return

		if itr == None :
			return Node(val)

		if val < itr.data :
			itr.left = self.addNode(val, itr.left)

		elif val >= itr.data :
			itr.right = self.addNode(val, itr.right)

		return itr

	def inordertraversal(self, itr):
		if itr == None :
			return

		self.inordertraversal(itr.left)
		print(itr.data)
		self.inordertraversal(itr.right)

	def Kthlargestval(self, K, itr):
		S = Stack()
		t = self.head
		S.push(t)
		itr = itr.right
		count = 0
		while True:
			while itr :
				S.push(itr)
				itr = itr.right

			count += 1
			itr = S.pop()
			if count == K :
				print('Value returned')
				return itr.data
			itr = itr.left



Tree = BST()

arr = [int(x) for x in input().split()]

for x in arr :
	Tree.addNode(x, Tree.head)


k = int(input())
print(f"{k}th largest value in the tree is {Tree.Kthlargestval(k, Tree.head)}")






		