import queue
Q = queue.Queue()
S = queue.Queue()

class Node :
	def __init__(self, value):
		self.value = value
		self.children = []

class GenericTree :
	def __init__(self):
		self.root = None

	def takeinput(self):
		val = int(input("Enter the root node : "))
		self.root = Node(val)
		Q.put(self.root)
		while not Q.empty():
			parent = Q.get()
			numberofnodes = int(input(f"Number of children of {parent.value} are : "))
			for i in range(numberofnodes):
				child = int(input(f"{i + 1}th child of {parent.value} is : "))
				Q.put(Node(child))
				parent.children.append(Node(child))

class BinaryTreeNode :
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

class BinaryTree :
	def __init__(self):
		self.root = None

	def convertGenerictreetoLCRS(self, tree):
		self.root = BinaryTreeNode(tree.root.value)
		self.conversionHelper(tree.root, self.root, None)

	def conversionHelper(self, root, itr, parent):
		if not root or not itr or len(root.children) == 0 :
			return

		itr.left = BinaryTreeNode(root.children[0].value)
		root.children = root.children[1:]
		itr.right = None if parent is None else parent.children[0]
		print("itr =", itr.data)
		print("leftchild =", itr.left.data)
		print("rightchild =", None if not itr.right else itr.right.data)

		if parent and len(parent.children) >= 2 and itr.right :
			parent.children = parent.children[1:]

		else :
			parent = root

		self.conversionHelper(root.children[0], itr.left, parent)
		self.conversionHelper(parent.children, itr.right, parent)

Gtree = GenericTree()
Gtree.takeinput()
LCRS = BinaryTree()
LCRS.convertGenerictreetoLCRS(Gtree)

def printtree(root):
	if root == None :
		return 

	print(root.data, end = " :")

	leftchild = root.left
	rightchild = root.right

	if leftchild :
		print(leftchild.data, end = ', ')

	if rightchild :
		print(rightchild.data, end = '')

	print('')
	printtree(root.left)
	printtree(root.right)

printtree(LCRS.root)


