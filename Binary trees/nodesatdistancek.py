import queue

Q = queue.Queue()

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

path_arr = []
def leaftonodepath(root, val):
	if root == None :
		return

	if root.data == val :
		path_arr.append(root)
		return root

	leftchild = leaftonodepath(root.left, val)
	rightchild = leaftonodepath(root.right, val)

	if leftchild :
		path_arr.append([root, "L"])
		return root

	if rightchild :
		path_arr.append([root, "R"])
		return root 

ans_arr = []
def printnodesatdepthk(root, k) :
	if root == None :
		return

	if k < 0 :
		return

	if k == 0 :
		ans_arr.append(root.data)
		return

	printnodesatdepthk(root.left, k - 1)
	printnodesatdepthk(root.right, k - 1)


def nodesatdistancek(arr, k):
	initial_distance = len(arr) - 1 
	for i in reversed(range(1, len(arr))):
		if initial_distance > k :
			initial_distance -= 1
			continue

		if initial_distance == k :
			ans_arr.append(arr[i][0].data)
			initial_distance -= 1
			continue

		if arr[i][1] == "L":
			printnodesatdepthk(arr[i][0].right, k - initial_distance - 1)

		elif arr[i][1] == 'R':
			printnodesatdepthk(arr[i][0].left, k - initial_distance - 1)

		initial_distance -= 1

	printnodesatdepthk(arr[0], k)


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


root = takeinput()
t = int(input())
k = int(input())
leaftonodepath(root, t)
nodesatdistancek(path_arr, k)
print(ans_arr)