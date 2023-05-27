class Node :
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right


def constructBSTfromsortedarr(arr, left, right):
	if left > right :
		return 

	mid = (left + right) // 2
	root = Node(arr[mid])
	root.left = constructBSTfromsortedarr(arr, left, mid - 1)
	root.right = constructBSTfromsortedarr(arr, mid + 1, right)

	return root

def valuesbetweenrange(root, k1, k2):
	if root == None :
		return

	if root.data >= k2 :
		valuesbetweenrange(root.left, k1, k2)

	elif root.data < k1 :
		valuesbetweenrange(root.right, k1, k2)

	else :
		print(root.data)
		valuesbetweenrange(root.left, k1, k2)
		valuesbetweenrange(root.right, k1, k2)

def printtree(root):
	if root == None :
		return

	print(root.data, end = " :")

	leftchild = root.left
	rightchild = root.right

	if leftchild :
		print(leftchild.data, end = ",")

	if rightchild :
		print(rightchild.data, end = "")

	print("")

	printtree(root.left)
	printtree(root.right)

def isBST(root, prevsmaller = -1, greater = float('inf')):
	if root == None :
		return True 

	if root.data > prevsmaller and root.data < greater :
		isleftBST = isBST(root.left, prevsmaller, root.data)
		isrightBST = isBST(root.right, root.data - 1, greater)
		return (isrightBST and isleftBST)

	else :
		return False

arr = [int(x) for x in input().split()]
N = len(arr)
arr.sort()
root = constructBSTfromsortedarr(arr, 0, N - 1)
printtree(root)
print(isBST(root))


	