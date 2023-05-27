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

	sumofnodes = root.data
	for child in root.children :
		sumofnodes += sumofallnodes(child)

	return sumofnodes 

def maxoftree(root, maxtree = -float('inf')):
	if root == None :
		return maxtree

	maxtree = max(maxtree, root.data)
	for child in root.children :
		maxtree = max(maxtree, maxoftree(child, maxtree))

	return maxtree 

def heightoftree(root):
	if root == None :
		return 0

	height = 1
	for child in root.children :
		childheight = heightoftree(child)
		