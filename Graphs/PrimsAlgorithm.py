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

def PrimsAlgorithm(graph, weight, visitedarr, parentarr):
	MST = Graph(graph.Numberofvertices)
	weight[0] = 0
	visitedarr[0] = True
	currentlyat = 0
	for i in range(graph.Numberofvertices):
		visitedarr[currentlyat] = True
		minweight = float('inf')
		idx = currentlyat
		for i in range(graph.Numberofvertices):
			hasedge = graph.hasEdge(currentlyat, i)
			if hasedge != False and weight[i] > hasedge and not visitedarr[i] :
				parentarr[i] = currentlyat
				weight[i] = hasedge
				
		currentlyat = getminweight(visitedarr, weight)

	#print(parentarr)
	for i in range(len(parentarr)):
		if parentarr[i] >= 0:
			#print(i, parentarr[i])
			#print(weight[i])
			MST.addEdge(i, parentarr[i], weight[i])

	print(MST.EdgeMatrix)

T = int(input("Enter the number of vertices you want in your graph \n"))

graph = Graph(T)
Edges = int(input("Enter the number of edges your graph has \n"))

for i in range(Edges):
	e1, e2, w = [int(x) for x in input().split()]
	graph.addEdge(e1, e2, w)

weight = [float('inf') for i in range(graph.Numberofvertices)]
visitedarr = [False for i in range(graph.Numberofvertices)]
parentarr = [-1 for i in range(graph.Numberofvertices)]

print("Edge Matrix of the MST is :")
PrimsAlgorithm(graph, weight, visitedarr, parentarr)