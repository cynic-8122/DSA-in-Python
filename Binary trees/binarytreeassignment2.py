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

def createandinsertduplicatenodes(root):
	#print('In recursion stack ')
	if root == None :
		return

	duplicatenode = Node(root.data, root.left)
	root.left = duplicatenode 
	createandinsertduplicatenodes(root.left.left)
	createandinsertduplicatenodes(root.right)

	return root

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

def minandmax(root, minsofar = float('inf'), maxsofar = -float('inf')):

	if root == None :
		return minsofar, maxsofar

	minleft, maxleft = minandmax(root.left, minsofar, maxsofar)
	minright, maxright = minandmax(root.right, minsofar, maxsofar)

	return (min(minright, minleft, root.data), max(maxright, maxleft, root.data))

def pathsumroottoleaf(root, k, s = 0, ans = ""):
	#print(s)
	if root == None :
		return 

	
	ans += str(root.data) + " "
	s += root.data
	
	if root.right == None and root.left == None and s == k:
		print(ans)
		return


	pathsumroottoleaf(root.left, k, s, ans)
	pathsumroottoleaf(root.right, k, s, ans)



arr = [int(x) for x in input().split()]
root = heapify(arr)
printtree(root)
#root = createandinsertduplicatenodes(root)
#printtree(root)
print(minandmax(root))
K = int(input())
pathsumroottoleaf(root, K)

