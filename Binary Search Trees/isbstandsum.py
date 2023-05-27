import queue

Q = queue.Queue()

class Node :
	def __init__(self, data = None, left = None, right = None) :
		self.data = data 
		self.left = left 
		self.right = right

def takeinput():
	print("Enter root ")
	rootdata = int(input())
	if rootdata == -1 :
		return None

	root = Node(rootdata)
	Q.put(root)
	while (not(Q.empty())) :
		current_node = Q.get()
		print("Enter left child of ",current_node.data)
		leftchilddata = int(input())
		if leftchilddata != -1 :
			leftchild = Node(leftchilddata)
			current_node.left = leftchild 
			Q.put(leftchild)

		print("Enter right child of ", current_node.data)
		rightchilddata = int(input())
		if rightchilddata != -1 :
			rightchild = Node(rightchilddata)
			current_node.right = rightchild 
			Q.put(rightchild)

	return root 


def sumandisBST(root, maxval = 0, maxtree = -float('inf'), mintree = float('inf')) :

	if root == None :
		return maxtree, mintree, max(maxval, 0), 0, True
	#print(root.data)
	maxleft, minleft, maxval, leftsum, isleftBST = sumandisBST(root.left, maxval, maxtree, mintree)
	maxright, minright, maxval, rightsum, isrightBST = sumandisBST(root.right, maxval, maxtree, mintree)

	sumoftree = leftsum + rightsum + root.data
	maxtree = max(maxleft, maxright, maxtree, root.data)
	mintree = min(minleft, minright, mintree, root.data)
	#print("sum of subtree", sumoftree)
	rdata = float('inf')
	ldata = -float('inf')
	if root.right :
		rdata = root.right.data 

	if root.left :
		ldata = root.left.data 

	print("maxleft, minleft", maxleft, minleft)
	print("maxright, minright", maxright, minright)

	if isleftBST and isrightBST and root.data > maxleft and root.data < minright:
		return maxtree, mintree, max(maxval, sumoftree), sumoftree, True 

	elif isleftBST :
		return maxtree, mintree, max(maxval, leftsum), leftsum, False

	elif isrightBST :
		return maxtree, mintree, max(maxval, rightsum), rightsum, False

	else :
		return maxtree, mintree, maxval, 0, False

root = takeinput()
print(sumandisBST(root))
		


