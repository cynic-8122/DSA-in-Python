import queue
Q = queue.Queue()

class Graph :
	def __init__(self, Numberofvertices):
		self.Numberofvertices = Numberofvertices
		self.EdgeMatrix = []

	def addEdge(self, v1, v2, weight = 1):
		self.EdgeMatrix.append([v1, v2, weight])		

	def hasEdge(self, v1, v2):
		for x in self.EdgeMatrix :
			if x[0] == v1 and x[1] == v2 and x[2] != None :
				return x[2]

			elif x[0] == v2 and x[1] == v1 and x[2] != None :
				return x[2]

		return False		

	def removeEdge(self, v1, v2):
		for x in self.EdgeMatrix :
			if x[0] == v1 and x[1] == v2 :
				x[2] = None

	def hasPath(self, v1, v2, checkarr):
		Q.put(v1)
		while not Q.empty() :
			currentlyat = Q.get()
			checkarr[currentlyat] = True
			for x in self.EdgeMatrix :
				if x[0] == currentlyat and x[1] == v2 and x[2] != None :
					return True

				elif x[1] == currentlyat and x[0] == v2 and x[2] != None :
					return True

				elif x[0] == currentlyat and x[2] != None and not checkarr[x[1]] :
					Q.put(x[1])

				elif x[1] == currentlyat and x[2] != None and not checkarr[x[0]] :
					Q.put(x[0])

		return False

def getminweight(visitedarr, weight):
	minweight = float('inf')
	idx = None
	for i in range(len(visitedarr)):
		if not visitedarr[i] and weight[i] < minweight:
			minweight = weight[i]
			idx = i 

	return idx

def dijkstrasalgorithm(graph, weight, visitedarr):
	currentlyat = 0
	for i in range(graph.Numberofvertices):
		visitedarr[currentlyat] = True
		for i in range(graph.Numberofvertices):
			twt = graph.hasEdge(currentlyat, i) 
			if twt != False and not visitedarr[i] and twt + weight[currentlyat] < weight[i]:
				weight[i] = twt + weight[currentlyat]

		currentlyat = getminweight(visitedarr, weight)

	print(weight)

graph = Graph(5)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 2, 8)
graph.addEdge(1, 2, 2)
graph.addEdge(2, 3, 5)
graph.addEdge(2, 4, 9)
graph.addEdge(1, 3, 5)
graph.addEdge(3, 4, 4)

visitedarr = [False for i in range(graph.Numberofvertices)]
weight = [float('inf') for i in range(graph.Numberofvertices)]
weight[0] = 0
dijkstrasalgorithm(graph, weight, visitedarr)

		

