class Node :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.right = right
		self.left = left

class BinaryTree :
	def __init__(self):
		self.root = None

	def heapify(self, arr, i = 1):
		
		if i > len(arr):
			return None
		itr = Node(arr[i - 1])
		if self.root == None :
			self.root = itr
		itr.left = self.heapify(arr, i<<1)
		itr.right = self.heapify(arr, (i<<1) + 1)

		return itr 

		
		

	def printtree(self, root):
		#print(i)
		if root == None :
			return

		print(root.data, end = ':')

		if root.left :
			print(root.left.data, end = ",")

		if root.right :
			print(root.right.data, end = '')

		print('')

		self.printtree(root.left)
		self.printtree(root.right)


def countnodes(root):
	if root == None :
		return 0

	return countnodes(root.left) + countnodes(root.right) + 1

def sumofnodes(root):
	if root == None :
		return 0

	return sumofnodes(root.left) + sumofnodes(root.right) + root.data

def preordertraversal(root):
	if root == None :
		return

	print(root.data)
	preordertraversal(root.left)
	preordertraversal(root.right)

def postordertraversal(root):
	if root == None :
		return

	postordertraversal(root.left)
	postordertraversal(root.right)
	print(root.data)

def inordertraversal(root):
	if root == None :
		return

	inordertraversal(root.left)
	print(root.data)
	inordertraversal(root.right)

def levelordertraversal(root, h):
	for i in range(h) :
		nodesatdepthk(root, i)
		print('')


def maxval(root, m = -float('inf')):
	if root == None :
		return m


	m = max(m, root.data)
	m1 = maxval(root.left, m)
	m2 = maxval(root.right, m)

	return max(m, m1, m2)

def countnodesgreaterthanX(root, X):
	if root == None :
		return 0 

	if root.data > X :
		return countnodesgreaterthanX(root.left, X) + countnodesgreaterthanX(root.right, X) + 1

	return countnodesgreaterthanX(root.left, X) + countnodesgreaterthanX(root.right, X)

def heightoftree(root):
	if root == None :
		return 0

	return max(heightoftree(root.left), heightoftree(root.right)) + 1

def numberofleafnodes(root):
	if root == None :
		return 0

	if root.left == None and root.right == None :
		return 1 

	count = numberofleafnodes(root.left) + numberofleafnodes(root.right)

	return count 

def nodesatdepthk(root, k) :
	if root == None :
		return

	if k == 0 :
		print(root.data, end  = " ")
		return

	nodesatdepthk(root.left, k - 1)
	nodesatdepthk(root.right, k - 1)

def replacenodewithdepth(root, k = 0):
	if root == None :
		return

	root.data = k 
	replacenodewithdepth(root.left, k + 1)
	replacenodewithdepth(root.right, k + 1)

	return root

def removeleafnodes(root):
	if root == None :
		return

	if root.left == None and root.right == None :
		return None 

	if root.left.left == None and root.left.right == None :
		root.left = None 

	if root.right.left == None and root.right.right == None :
		root.right = None 


	removeleafnodes(root.left)
	removeleafnodes(root.right)

	return root

def mirrortree(root):
	if root == None :
		return

	if root.left == None and root.right == None :
		return

	root.left , root.right = root.right , root.left
	mirrortree(root.left)
	mirrortree(root.right)

def checkbalanced(root):
	if root == None :
		return True

	if root.left == None and root.right == None :
		return True

	if abs(heightoftree(root.left) - heightoftree(root.right)) > 1 :
		return False

	if abs(heightoftree(root.left) - heightoftree(root.right)) <= 1:
		c1 = checkbalanced(root.left)
		c2 = checkbalanced(root.right)
		return (c1 and c2)

def checkbalancedimproved(root):
	if root == None :
		return True , 0 

	isleftbalanced, heightoflefttree = checkbalancedimproved(root.left)
	isrightbalanced, heightofrightree = checkbalancedimproved(root.right)

	height = 1 + max(heightoftree, heightoflefttree)
	 
	if abs(heightoflefttree - heightofrightree) > 1 :
		return False, height 

	if isrightbalanced and isleftbalanced :
		return True, height 

	else :
		return False, height 

def diameterofbinarytree(root):
	if root == None :
		return 0, 0

	leftdia, leftheight = diameterofbinarytree(root.left)
	rightdia, rightheight = diameterofbinarytree(root.right)

	height = max(rightheight, leftheight) + 1 

	return max(rightdia, leftdia, rightheight + leftheight), height 

def treefrominorderandpreorder(inorder, preorder):
	if len(inorder) == 0 :
		return 

	check = False
	for i in range(len(inorder)) :
		if preorder[0] == inorder[i]:
			check = True
			s = i 
			break


	if not check :
		return

	root = Node(preorder[0])
	#preorder = preorder[1:]
	leftsubtree = inorder[ :s]
	rightsubtree = inorder[(s + 1) : ]
	l = len(leftsubtree)
	leftpreorder = preorder[1:(l + 1)]
	rightpreorder = preorder[(l + 1):] 
	root.left = treefrominorderandpreorder(leftsubtree, leftpreorder)
	root.right = treefrominorderandpreorder(rightsubtree, rightpreorder)

	return root 

inorder = str(input("INORDER"))
preorder = str(input("PREORDER"))
root = treefrominorderandpreorder(inorder, preorder)
postordertraversal(root)
'''
#arr = [int(x) for x in input().split()]
#Tree = BinaryTree()
#Tree.heapify(arr)
#Tree.printtree(Tree.root)
#print(Tree.root.data)
#print(Tree.root.left.data)
#print(Tree.root.right.data)
#print(countnodes(Tree.root))
#print(sumofnodes(Tree.root))

preordertraversal(Tree.root)
print("__________________---------------___________________________")
postordertraversal(Tree.root)
print("__________________---------------___________________________")


#inordertraversal(Tree.root)

print("MAX VAL :", maxval(Tree.root))
print("COUNT :", countnodesgreaterthanX(Tree.root, 5))
print("HEIGHT :", heightoftree(Tree.root))
print("NUMBER OF LEAVES : ", numberofleafnodes(Tree.root))
#removeleafnodes(Tree.root)
#inordertraversal(Tree.root)
Tree.printtree(Tree.root)
#K = int(input("Give the value of k : "))
#nodesatdepthk(Tree.root, K)
#modifiedtree = replacenodewithdepth(Tree.root)
#inordertraversal(modifiedtree)
mirrortree(Tree.root)
levelordertraversal(Tree.root, heightoftree(Tree.root))
'''