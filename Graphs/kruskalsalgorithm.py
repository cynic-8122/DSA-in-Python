''' 
For Minimum spanning Tree of a graph(weighted, directed/undirected)

Description :
#For Given N vertices, we need to select N - 1 Edges (which we will do greedily).
#Start picking the Edges with minimum weight while checking if the Edge under consideration 
does not lead to formation of any cycles in the Tree.
#If so, then skip the Edge under consideration and move on the Edge with next minimum weight.
#Stop when your count reaches N - 1.
'''
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
				return True

			elif x[0] == v2 and x[1] == v1 and x[2] != None :
				return True

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

def custommerge(leftarr, rightarr):
	temparr = []
	i = 0
	j = 0
	while i < len(leftarr) and j < len(rightarr) :
		if leftarr[i][2] <= rightarr[j][2]:
			temparr.append(leftarr[i])
			i += 1

		else :
			temparr.append(rightarr[j])
			j += 1

	while i < len(leftarr):
		temparr.append(leftarr[i])
		i += 1

	while j < len(rightarr):
		temparr.append(rightarr[j])
		j += 1

	return temparr


def mergesort(arr, l, r) :
	if l > r :
		return

	if l == r :
		return [arr[l]]

	mid = (l + r)//2

	leftarr = mergesort(arr, l, mid)
	rightarr = mergesort(arr, mid+1, r)

	return custommerge(leftarr, rightarr)


def KruskalsAlgorithm(graph):
	MST = Graph(graph.Numberofvertices)
	temparr = mergesort(graph.EdgeMatrix, 0, len(graph.EdgeMatrix) - 1)
	count = 0
	i = 0
	while count < graph.Numberofvertices and i < len(temparr):
		#print('loopK')
		edge1 = temparr[i][0]
		edge2 = temparr[i][1]
		weight = temparr[i][2]
		if not MST.hasPath(edge1, edge2, [False for i in range(MST.Numberofvertices)]) :
			MST.addEdge(edge1, edge2, weight)
			count += 1 

		i += 1

	print(MST.EdgeMatrix)

graph = Graph(4)
graph.addEdge(0, 1, 3)
graph.addEdge(0, 3, 5)
graph.addEdge(1, 2, 1)
graph.addEdge(2, 3, 8)
#graph.addEdge(2, 3, 11)
#graph.addEdge(4, 5, 9)
#graph.addEdge(5, 6, 4)

KruskalsAlgorithm(graph)
