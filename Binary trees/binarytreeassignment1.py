class Node :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right


def heapify(arr, i = 1):
	if i > len(arr):
		return 

	root = Node(arr[i - 1])
	root.left = heapify(arr, i << 1)
	root.right = heapify(arr, (i << 1) + 1)

	return root

def ispresent(root, val):
	if root == None :
		return False

	if root.data == val:
		return True 

	leftchild = ispresent(root.left, val)
	rightchild = ispresent(root.right, val)

	return leftchild or rightchild

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

def nodeswithoutsiblings(root):
	if root == None :
		return 

	leftchild = root.left 
	rightchild = root.right 

	if (leftchild and not rightchild) : 
		print(leftchild.data, end = " ")

	elif (rightchild and not leftchild) :
		print(rightchild.data, end = " ")

	nodeswithoutsiblings(root.left)
	nodeswithoutsiblings(root.right)

arr = [int(x) for x in input().split()]
root = heapify(arr)
printtree(root)
X = int(input())
print(ispresent(root,X))
nodeswithoutsiblings(root)




