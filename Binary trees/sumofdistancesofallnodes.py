import queue
Q = queue.Queue()

class Node :
	def __init__(self, data = None, left = None, right = None) :
		self.data = data
		self.right = right
		self.left = left 

def sumofdepths(root, depth = 0):
	#print(root.data, depth)
	if root == None :
		return 0

	ans = sumofdepths(root.left, depth + 1) + sumofdepths(root.right, depth + 1)
	ans += depth

	return ans 

def sumofdepthsofsubtree(root, depth = 0):
	if root == None :
		return 0 

	ans = sumofdepthsofsubtree(root.left) + sumofdepthsofsubtree(root.right)
	ans += sumofdepths(root)

	return ans

def sumofdepthsofsubtreebetter(root, ans = 0, temp = 0):
	if root == None :
		return 0, 0

	numnodesleft, leftdepth = sumofdepthsofsubtreebetter(root.left, ans, temp)
	numnodesright, rightdepth = sumofdepthsofsubtreebetter(root.right, ans, temp)

	numnodes = numnodesleft + numnodesright + 1
	ans += leftdepth + rightdepth + numnodesleft + numnodesright
	temp += ans 

	return numnodes, temp


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
print(sumofdepths(root))
print(sumofdepthsofsubtree(root))
print(sumofdepthsofsubtreebetter(root))


