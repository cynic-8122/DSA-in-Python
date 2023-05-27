class Node :
	def __init__(self, data = None):
		self.data = data
		self.children = []

def takeinput():
	print("Enter node data ")
	data = int(input())

	if data == -1 :
		return 

	root = Node(data)
	print("Number of children of ", data)
	numchild = int(input())

	for i in range(numchild) :
		child = takeinput()
		root.children.append(child)

	return root 

def preorder(root):
	if root == None :
		return

	print(root.data)

	for child in root.children :
		preorder(child)

def printtree(root):
	if root == None :
		return

	print(root.data, end = " : ")

	for child in root.children :
		print(child.data, end = ", ")

	print()

	for child in root.children :
		printtree(child)

def countnodes(root):
	if root == None :
		return 0

	count = 1
	for child in root.children :
		count += countnodes(child)

	return count 

def sumofallnodes(root):
	if root == None :
		return 0 

	sumsofar = root.data 
	for child in root.children :
		sumsofar += sumofallnodes(child)

	return sumsofar

def maxoftree(root, maxval = -float('inf')):
	if root == None :
		return -float('inf')

	maxval = max(maxval, root.data)

	for child in root.children :
		maxval = maxoftree(child, maxval)

	return maxval

def heightoftree(root):
	if root == None :
		return 0 

	subtreeheight = 0
	
	for child in root.children :
		heightofthischild = heightoftree(child)
		subtreeheight = max(subtreeheight, heightofthischild)

	return subtreeheight + 1 


root = takeinput()
preorder(root)
printtree(root)
print(countnodes(root))
print(sumofallnodes(root))
print(maxoftree(root))
print(heightoftree(root))
