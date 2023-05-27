import queue
Q = queue.Queue()
P = queue.Queue()
class Node :
	def __init__(self, data = None, left = None, right = None) :
		self.data = data
		self.left = left
		self.right = right

class BinaryTree :
	def takeinput(self, arr) :
		root = Node(arr[0])
		Q.put(root)
		for i in range(1, len(arr), 2) :
			x = arr[i]
			y = arr[i + 1]
			parent = Q.get()
			if x != -1:
				leftchild = Node(x)
				parent.left = leftchild 
				Q.put(leftchild)

			if y != -1 :
				rightchild = Node(y)
				parent.right = rightchild
				Q.put(rightchild)

		return root

	def levelordertraversal(self, root) :
		P.put(root)
		while not P.empty():
			Node = P.get()
			if Node :
				P.put(Node.left)
				P.put(Node.right)
				print(Node.data, end = " ")

print("Give the tree input in a single line (Level-Wise) ")
arr = [int(x) for x in input().split()]
Tree = BinaryTree()
root = Tree.takeinput(arr)
print("Levelorder Traversal ", end = " ")
Tree.levelordertraversal(root)