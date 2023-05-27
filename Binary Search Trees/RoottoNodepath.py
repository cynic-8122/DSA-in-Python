class Node :
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.right = right
		self.left = left

def heapify(arr, i = 1):
	if i > len(arr):
		return

	root = Node(arr[i - 1])
	root.left = heapify(arr, i<<1)
	root.right = heapify(arr, (i << 1) + 1)

	return root

ans_arr = []
def Nodetorootpath(root, val):
	if root == None :
		return None

	if root.data == val :
		ans_arr.append(root.data)
		return root 

	isleftchildof = Nodetorootpath(root.left, val)
	isrightchildof = Nodetorootpath(root.right, val)

	if isrightchildof :
		ans_arr.append(root.data)
		return root 


	elif isleftchildof :
		ans_arr.append(root.data)
		return root

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

arr = [int(x) for x in input().split()]
X = int(input())
root = heapify(arr)
printtree(root)
Nodetorootpath(root, X)
print(ans_arr)




