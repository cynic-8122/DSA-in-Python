class Node :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
		self.height = 1

class AVLTree :
	def __init__(self):
		self.root = None
		self.traversedpath = [] 

	def balancethetree(self, itr) :
		#Types of unbalances :
		# 1. LL : 
		# 2. RR :
		# 3. LR :
		# 4. RL :

		idx = -(itr.height - 1)
		if self.traversedpath[idx] == "L" and self.traversedpath[idx + 1] == "L":
			node1 = itr  
			node2 = itr.left  
			node3 = itr.left.left 
			r1 = node1.right  
			r2 = node2.right  
			r3 = node3.right 
			l1 = node3.left 
			node2.left = node3
			node1.height = max(int(0 if r2 is None else r2.height), int(0 if r1 is None else r1.height)) + 1 
			node2.right = node1 
			node2.height = max(int(0 if node3 is None else node3.height), int(0 if node1 is None else node1.height)) + 1
			node1.left = r2

			return node2

		elif self.traversedpath[idx] == "L" and self.traversedpath[idx + 1] == "R" :
			node1 = itr 
			node2 = itr.left 
			node3 = itr.left.right 
			r1 = node1.right 
			r2 = node3.right 
			l1 = node3.left 
			l2 = node2.left 
			node3.left = node2 
			node3.right = node1
			node1.height = max(int(0 if r1 is None else r1.height), int(0 if r2 is None else r2.height)) + 1
			node2.height = max(int(0 if l2 is None else l2.height), int(0 if l1 is None else l1.height)) + 1
			node2.right = l1
			node1.left = r2 
			node3.height = max(int(0 if node1 is None else node1.height), int(0 if node2 is None else node2.height)) + 1

			return node3 


		elif self.traversedpath[idx] == "R" and self.traversedpath[idx + 1] == "R" :
			node1 = itr 
			node2 = itr.right 
			node3 = itr.right.right  
			r1 = node3.right 
			l1 = node1.left 
			l2 = node2.left 
			l3 = node3.left 
			node2.right = node3 
			node2.left = node1
			node1.height = max(int(0 if l1 is None else l1.height), int(0 if l2 is None else l2.height)) + 1
			node2.height = max(int(0 if node3 is None else node3.height), int(0 if node2 is None else node2.height)) + 1
			node1.right = l2

			return node2

		elif self.traversedpath[idx] == "R" and self.traversedpath[idx + 1] == "L" :
			node1 = itr 
			node2 = itr.right 
			node3 = itr.right.left 
			l1 = node1.left 
			l2 = node3.left 
			r1 = node2.right 
			r2 = node3.right 
			node3.left = node1 
			node3.right = node2 
			node1.right = l2 
			node2.left = r2
			node2.height = max(int(0 if r1 is None else r1.height), int(0 if r2 is None else r2.height)) + 1
			node1.height = max(int(0 if l1 is None else l1.height), int(0 if l2 is None else l2.height)) + 1
			node3.height = max(int(0 if node1 is None else node1.height), int(0 if node2 is None else node2.height)) + 1

			return node3 

	def insert(self, itr, val, traversedpath):
		if self.root == None :
			self.root = Node(val)
			return self.root 

		if itr == None :
			itr = Node(val)
			return itr 

		if itr.data <= val :
			traversedpath.append("R")
			itr.right = self.insert(itr.right, val, traversedpath)
			if not itr.left :
				leftheight  = 0

			else :
				leftheight = itr.left.height

			rightheight = itr.right.height
			itr.height = max(rightheight, leftheight) + 1

		if itr.data > val :
			traversedpath.append("L")
			itr.left = self.insert(itr.left, val, traversedpath)
			if not itr.right :
				rightheight = 0

			else :
				rightheight = itr.right.height

			leftheight = itr.left.height 
			itr.height = max(leftheight, rightheight) + 1

		if not itr.left :
			leftheight = 0 

		else :
			leftheight = itr.left.height 

		if not itr.right :
			rightheight = 0

		else :
			rightheight = itr.right.height 

		balancefactor = leftheight - rightheight
		#print(f"At {itr.data}, balancefactor = {balancefactor}")
		if abs(balancefactor) > 1 :
			self.traversedpath = traversedpath
			return self.balancethetree(itr) 
		else :
			return itr 

	def minval(self, root):
		itr = root 
		while itr.left :
			itr = itr.left 

		return itr 

	def delete(self, itr, val):
		if self.root == None :
			return

		if itr == None :
			return 

		if itr.data < val:
			itr.right = self.delete(itr.right, val)

		if itr.data > val :
			itr.left = self.delete(itr.left, val)

		if itr.data == val and itr.right == None and itr.left == None :
			return None 

		elif itr.data == val and itr.left == None :
			return itr.right

		elif itr.data == val and itr.right == None :
			return itr.left 

		elif itr.data == val :
			replacewith = self.minval(itr.right)
			itr.right = self.delete(itr.right, replacewith.data)
			itr.data = replacewith.data
			return itr 

		

		itr.height = max(int(0 if itr.right is None else itr.right.height), int(0 if itr.left is None else itr.left.height)) + 1

		balancefactor = int(0 if itr.left is None else itr.left.height) - int(0 if itr.right is None else itr.right.height)
		if abs(balancefactor) > 1:
			return self.balancethetreedeleted(itr)

		

		return itr

	def balancefactor(self, itr):
		balancefactor = int(0 if itr.left is None else itr.left.height) - int(0 if itr.right is None else itr.right.height)
		return balancefactor

	def balancethetreedeleted(self, itr) :
		if self.balancefactor(itr) > 1 and self.balancefactor(itr.left) > 0 :
			node1 = itr  
			node2 = itr.left  
			node3 = itr.left.left 
			r1 = node1.right  
			r2 = node2.right  
			r3 = node3.right 
			l1 = node3.left 
			node2.left = node3
			node1.height = max(int(0 if r2 is None else r2.height), int(0 if r1 is None else r1.height)) + 1 
			node2.right = node1 
			node2.height = max(int(0 if node3 is None else node3.height), int(0 if node1 is None else node1.height)) + 1
			node1.left = r2

			return node2

		elif self.balancefactor(itr) > 1 and self.balancefactor(itr.left) < 0 :
			node1 = itr 
			node2 = itr.left 
			node3 = itr.left.right 
			r1 = node1.right 
			r2 = node3.right 
			l1 = node3.left 
			l2 = node2.left 
			node3.left = node2 
			node3.right = node1
			node1.height = max(int(0 if r1 is None else r1.height), int(0 if r2 is None else r2.height)) + 1
			node2.height = max(int(0 if l2 is None else l2.height), int(0 if l1 is None else l1.height)) + 1
			node2.right = l1
			node1.left = r2 
			node3.height = max(int(0 if node1 is None else node1.height), int(0 if node2 is None else node2.height)) + 1

			return node3

		elif self.balancefactor(itr) < -1 and self.balancethetreedeleted(itr.right) > 0 :
			node1 = itr 
			node2 = itr.right 
			node3 = itr.right.left 
			l1 = node1.left 
			l2 = node3.left 
			r1 = node2.right 
			r2 = node3.right 
			node3.left = node1 
			node3.right = node2 
			node1.right = l2 
			node2.left = r2
			node2.height = max(int(0 if r1 is None else r1.height), int(0 if r2 is None else r2.height)) + 1
			node1.height = max(int(0 if l1 is None else l1.height), int(0 if l2 is None else l2.height)) + 1
			node3.height = max(int(0 if node1 is None else node1.height), int(0 if node2 is None else node2.height)) + 1

			return node3
			

		elif self.balancefactor(itr) < -1 and self.balancethetreedeleted(itr.right) < 0 :
			node1 = itr 
			node2 = itr.right 
			node3 = itr.right.right  
			r1 = node3.right 
			l1 = node1.left 
			l2 = node2.left 
			l3 = node3.left 
			node2.right = node3 
			node2.left = node1
			node1.height = max(int(0 if l1 is None else l1.height), int(0 if l2 is None else l2.height)) + 1
			node2.height = max(int(0 if node3 is None else node3.height), int(0 if node2 is None else node2.height)) + 1
			node1.right = l2

			return node2


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

Tree = AVLTree()
Tree.root = Tree.insert(Tree.root, 40, [])
Tree.root = Tree.insert(Tree.root, 20, [])
Tree.root = Tree.insert(Tree.root, 10, [])
Tree.root = Tree.insert(Tree.root, 25, [])
Tree.root = Tree.insert(Tree.root, 30, [])
Tree.root = Tree.insert(Tree.root, 22, [])
print(Tree.traversedpath)
Tree.root = Tree.insert(Tree.root, 50, [])



Tree.printtree(Tree.root)
print("\n")

print("Delete 25")
print("\n")
Tree.root = Tree.delete(Tree.root, 25)
Tree.printtree(Tree.root)


		






	