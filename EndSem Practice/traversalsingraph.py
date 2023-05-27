import queue
Q = queue.Queue()

class AdjacencyMatrix :
	def __init__(self, Numberofvertices):
		self.Numberofvertices = Numberofvertices
		self.AdjMatrix = [[0 for i in range(self.Numberofvertices)] for i in range(self.Numberofvertices)]

	
class Graph :
	def __init__(self, Numberofvertices):
		self.Numberofvertices = Numberofvertices
		self.AdjMatrix = AdjacencyMatrix(self.Numberofvertices)

	def addEdge(self, node1, node2, weight = 1):
		self.AdjMatrix[node1][node2] = weight
		self.AdjMatrix[node2][node1] = weight

	def removeEdge(self, node1, node2):
		self.AdjMatrix[node1][node2] = 0
		self.AdjMatrix[node2][node1] = 0

	def BFS(self, node, checkarr):
		Q.put(node)
		while not Q.empty():
			parent = Q.get()

			for i in range(self.Numberofvertices):
				if self.AdjMatrix[node][i] and not checkarr[node]:
					checkarr[i] = True
					Q.put(i)

			print(parent)

	def DFS(self, node, checkarr):
		if checkarr[node] == None :
			return

		print(node)
		checkarr[node] = True
		for i in range(self.Numberofvertices):
			if self.AdjMatrix[node][i] :
				self.DFS(i)




