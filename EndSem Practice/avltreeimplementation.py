'''
First we implement a BST and then add a check function for balancing.
'''
import queue
Q = queue.Queue()

class BSTNode :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class BST :
	def __init__(self):
		self.root = None
		self.__count = 0

	def insertValueHelper(self, itr, val):
		if itr == None :
			return BSTNode(val)

		if val >= itr.data :
			itr.right = self.insertValueHelper(itr.right, val)

		else :
			itr.left = self.insertValueHelper(itr.left, val)

		return itr

	def insertValue(self, val):
		self.__count += 1
		if self.root == None :
			self.root = BSTNode(val)
			return self.root

		itr = self.root
		return self.insertValueHelper(itr, val)

	def getminval(self, itr):
		if itr == None :
			return

		while itr.left :
			itr = itr.left

		return itr

	def isLeaf(self, node):
		return node.left == None and node.right == None

	def RemoveValueHelper(self, itr, val):
		if itr == None :
			return

		if itr.data == val and self.isLeaf(itr):
			return None

		elif itr == val and not(itr.left and itr.right) :
			if itr.right :
				return itr.right

			return itr.left

		elif itr == val :
			replacewith = self.getminval(itr.right)
			itr.data = replacewith.data
			itr.right = self.RemoveValueHelper(itr.right, replacewith.data)
			return itr

		if itr.data > val :
			itr.left = self.RemoveValueHelper(itr.left, val)

		else :
			itr.right = self.RemoveValueHelper(itr.right, val)

		return itr

	def removevalue(self, val):
		if not self.__count :
			return

		itr = self.root
		self.__count -= 1
		return self.RemoveValueHelper(itr, val)

	def printtree(self, node):
		itr = node
		Q.put(itr)
		while not Q.empty() :
			parent = Q.get()
			print(f"{parent.data} : {None if parent.left is None else parent.left.data}, {None if parent.right is None else parent.right.data}")
			if parent.left :
				Q.put(parent.left)

			if parent.right :
				Q.put(parent.right)

def inordertraversal(root):
	if root == None :
		return

	inordertraversal(root.left)
	print(root.data)
	inordertraversal(root.right)

def postordertraversal(root):
	if root == None :
		return

	postordertraversal(root.left)
	postordertraversal(root.right)
	print(root.data)

def preordertraversal(root):
	if root == None :
		return

	print(root.data)
	preordertraversal(root.left)
	preordertraversal(root.right)

BinarySearchTree = BST()
BinarySearchTree.insertValue(15)
BinarySearchTree.insertValue(12)
BinarySearchTree.insertValue(11)
BinarySearchTree.insertValue(13)
BinarySearchTree.insertValue(10)
BinarySearchTree.insertValue(9)
BinarySearchTree.insertValue(17)
BinarySearchTree.insertValue(14)
BinarySearchTree.printtree(BinarySearchTree.root)

inordertraversal(BinarySearchTree.root)
postordertraversal(BinarySearchTree.root)
preordertraversal(BinarySearchTree.root)