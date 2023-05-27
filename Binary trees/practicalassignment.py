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

	def preordertraversal(self, root):
		if root == None :
			return

		print(root.data, end = " ")
		self.preordertraversal(root.left)
		self.preordertraversal(root.right)

	def inordertraversal(self, root) :
		if root == None :
			return

		self.inordertraversal(root.left)
		print(root.data, end = " ")
		self.inordertraversal(root.right)

	def postordertraversal(self, root) :
		if root == None :
			return

		self.postordertraversal(root.left)
		self.postordertraversal(root.right)
		print(root.data, end = " ")


print("Give the tree input in a single line (Level-Wise) ")
arr = [int(x) for x in input().split()]
Tree = BinaryTree()
root = Tree.takeinput(arr)
print("Preorder Traversal ", end = " ") 
Tree.preordertraversal(root)
print()
print("Inorder Traversal ", end = " ")
Tree.inordertraversal(root)
print()
print("Postorder Traversal ", end = " ")
Tree.postordertraversal(root)



