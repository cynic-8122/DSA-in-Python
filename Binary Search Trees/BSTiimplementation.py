class Node :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right


class BST :
	def __init__(self):
		self.root = None

	def insert(self, itr, val):
		if self.root == None :
			self.root = Node(val)
			return self.root

		if itr == None :
			itr = Node(val)
			return itr 

		if val >= itr.data :
			itr.right = self.insert(itr.right, val)

		else :
			itr.left = self.insert(itr.left, val)

		return itr

	def minval(self, root):
		while root.left :
			root = root.left 

		return root

	def delete(self, val, itr):
		if itr == None :
			return itr 

		if val > itr.data :
			itr.right = self.delete(val, itr.right)

		elif val < itr.data :
			itr.left = self.delete(val, itr.left)

		elif val == itr.data and itr.left == None and itr.right == None :
			return None

		elif val == itr.data and itr.left == None :
			return itr.right 

		elif val == itr.data and itr.right == None :
			return itr.left
		
		elif val == itr.data :
			replacewith = self.minval(itr.right)
			itr.right = self.delete(replacewith.data, itr.right)
			#print(itr.right.data)
			itr.data = replacewith.data 
			return itr  
		return itr 

	def ispresent(self, val, itr) :
		if itr == None :	
			return False

		if itr.data == val :
			return True 

		if itr.data > val :
			return self.ispresent(val, itr.left)

		elif itr.data < val :
			return self.ispresent(val, itr.right)

	def printtree(self, itr) :
		if itr == None :
			return 

		print(itr.data, end = " :")

		leftchild = itr.left
		rightchild = itr.right

		if leftchild :
			print(leftchild.data, end = ' ')

		if rightchild :
			print(",", rightchild.data, end = '')

		print('')
		self.printtree(itr.left)
		self.printtree(itr.right)


Tree = BST()
Tree.root = Tree.insert(Tree.root, 50)
Tree.root = Tree.insert(Tree.root, 30)
Tree.root = Tree.insert(Tree.root, 20)
Tree.root = Tree.insert(Tree.root, 40)
Tree.root = Tree.insert(Tree.root, 70)
Tree.root = Tree.insert(Tree.root, 60)
Tree.root = Tree.insert(Tree.root, 80)
Tree.root = Tree.insert(Tree.root, 35)
Tree.printtree(Tree.root)
print("Deleted Node 50")
Tree.delete(50, Tree.root)
Tree.printtree(Tree.root)
