import queue

Q = queue.Queue()
P = queue.Queue()

class Graph :
	def __init__(self, Numberofvertices):
		self.Numberofvertices = Numberofvertices
		self.AdjacencyMatrix = [[0 for i in range(Numberofvertices)] for i in range(Numberofvertices)]
		self.checkmatrix = [False]*(self.Numberofvertices)

	def addEdge(self, v1, v2):
		self.AdjacencyMatrix[v1][v2] = 1 
		self.AdjacencyMatrix[v2][v1] = 1

	def removeEdge(self, v1, v2):
		if not self.containsEdge(v1, v2):
			return

		self.AdjacencyMatrix[v1][v2] = 0
		self.AdjacencyMatrix[v2][v1] = 0

	def containsEdge(self, v1, v2):
		if self.AdjacencyMatrix[v1][v2] == 1 or self.AdjacencyMatrix[v2][v1] == 1 :
			return True

		return False

	def DFS(self, node = 0):
		if self.checkmatrix[node] :
			return

		print(node, end = " ")

		for j in range(self.Numberofvertices):
			self.checkmatrix[node] = True
			isEdge = self.AdjacencyMatrix[node][j]
			if isEdge : 
				self.DFS(j)


	def BFS(self, node = 0):
		Q.put(node)
		while not Q.empty() :
			currentlyat = Q.get()
			if not self.checkmatrix[currentlyat] :
				print(currentlyat, end = " ")

			self.checkmatrix[currentlyat] = True
			for i in range(self.Numberofvertices) :
				if self.AdjacencyMatrix[currentlyat][i] and not self.checkmatrix[i]:
					Q.put(i)

	def hasPath(self, v1, v2):
		if self.AdjacencyMatrix[v1][v2] :
			return True 

		Q.put(v1)
		while not Q.empty() :
			#print("loop works")
			currentlyat = Q.get()
			#print(currentlyat)
			self.checkmatrix[currentlyat] = True
			for i in range(self.Numberofvertices):
				if self.AdjacencyMatrix[currentlyat][i] and not self.checkmatrix[i] and i != v2:
					Q.put(i)

				elif self.AdjacencyMatrix[currentlyat][i] and not self.checkmatrix[i] and i == v2 :
					return True					

		return False

	def DFSforDisconnectedGraph(self, node = 0):
		self.DFS(node)

		for i in range(self.Numberofvertices) :
			if not self.checkmatrix[i] :
				self.DFSforDisconnectedGraph(i)


	def BFSforDisconnectedGraph(self, node = 0):
		self.BFS(node)

		for i in range(self.Numberofvertices):
			if not self.checkmatrix[i]:
				self.BFSforDisconnectedGraph(i)


	def getpathDFS(self, v1, v2, path = None):
		if self.checkmatrix[v1] :
			return

		self.checkmatrix[v1] = True
		for i in range(self.Numberofvertices):
			isEdge = self.AdjacencyMatrix[v1][i]
			if isEdge and i != v2 :
				path = self.getpathDFS(i, v2, path)
				if path :
					path = str(v1) + " " + path
					return path


			elif isEdge and i == v2 :
				path = str(v1) + " " + str(i)
				return path

	def degree(self, node):
		count = 0
		for i in range(self.Numberofvertices):
			if self.AdjacencyMatrix[node][i] :
				count += 1

		return count

	def getpathBFS(self, v1, v2):
		path = []
		ParentHashmap = {}
		ParentHashmap[v1] = None
		Q.put(v1)
		check = True
		while not Q.empty() :
			currentlyat = Q.get()
			self.checkmatrix[currentlyat] = True
			for i in range(self.Numberofvertices):
				if self.AdjacencyMatrix[currentlyat][i] and not self.checkmatrix[i] and i != v2 :
					Q.put(i)
					ParentHashmap[i] = currentlyat

				elif self.AdjacencyMatrix[currentlyat][i] and not self.checkmatrix[i] and i == v2 :
					ParentHashmap[i] = currentlyat
					#print(f"currentlyat = {currentlyat}")
					path.append(i)
					temp = currentlyat
					while temp != None :
						path.append(temp)
						temp = ParentHashmap[temp]

					return path

		return path


G = Graph(7)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(2, 3)
G.addEdge(2, 4)
G.addEdge(4, 5)
G.addEdge(5, 6)
G.addEdge(1, 6)
#G.addEdge()
#G.addEdge()
#print(G.AdjacencyMatrix)
#print(G.hasPath(0, 5))
#G.BFS()

print(G.getpathBFS(0, 3))






		
