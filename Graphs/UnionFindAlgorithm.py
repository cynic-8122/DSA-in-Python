'''
Kruskal's Algorithm Using Union Find Algorithm 
(for checking whether selecting certain edge would lead to cycle formation)

Description :
(Selecting an Edge which connects two vertices on same connected component )

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
	rightarr = mergesort(arr, mid + 1, r)

	return custommerge(leftarr, rightarr)

def gettopmostparent(parentarr, vertex):
	if parentarr[vertex] == vertex :
		return vertex

	itr = vertex
	while itr != parentarr[itr]:
		itr = parentarr[itr]

	return itr

def KruskalsAlgorithm(graph, parentarr):
	MST = Graph(graph.Numberofvertices)
	temparr = mergesort(graph.EdgeMatrix, 0, len(graph.EdgeMatrix) - 1)
	i = 0
	count = 0
	while count < MST.Numberofvertices and i < len(temparr):
		node1 = temparr[i][0]
		node2 = temparr[i][1]
		weight = temparr[i][2]
		p1 = gettopmostparent(parentarr, node1)
		p2 = gettopmostparent(parentarr, node2)

		if p1 != p2 :
			MST.addEdge(node1, node2, weight)
			count += 1
			parentarr[p1] = p2

		i += 1

	print(MST.EdgeMatrix)

graph = Graph(7)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 2, 5)
graph.addEdge(2, 4, 1)
graph.addEdge(2, 3, 4)
graph.addEdge(1, 6, 7)
graph.addEdge(6, 5, 11)
graph.addEdge(4, 5, 9)

parentarr = [i for i in range(graph.Numberofvertices)]

KruskalsAlgorithm(graph, parentarr)
