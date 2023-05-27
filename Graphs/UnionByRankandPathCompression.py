'''
Using a rank matrix and path compression for improving the time complexity of Union Fing Algorithm.

Description :

#Through maintaining a rank array we ensure that a higher ranked vertex never gets attached to 
a lower ranked vertex.
(Consider it analogus to height balancing in a BST, 
we try ensure that the each vertex has its topmost parent at the closest possible distance.)

#In the path compression process we try to ensure that the query (of get parent) gets solved as fast as possible.
(for a query that we just answered, we update the topmost parent for all the vertices we traversed so that
any further queries with any of traversed vertices gets answered in O(1) time.)
'''

import queue

Q = queue.Queue()

class Edge:
	def __init__(self, node1, node2, weight = 1):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight

class Graph :
	def __init__(self, Numberofvertices):
		self.Numberofvertices = Numberofvertices
		self.EdgeMatrix = []

	def addEdge(self, v1, v2, weight = 1):
		edge = Edge(v1, v2, weight)
		self.EdgeMatrix.append(edge)		

	def hasEdge(self, v1, v2):
		for x in self.EdgeMatrix :
			if x.node1 == v1 and x.node2 == v2 and x.weight != None :
				return True

			elif x.node1 == v2 and x.node2 == v1 and x.weight != None :
				return True

		return False		

	def removeEdge(self, v1, v2):
		for x in self.EdgeMatrix :
			if x.node1 == v1 and x.node2 == v2 :
				x.weight = None

	def hasPath(self, v1, v2, checkarr):
		Q.put(v1)
		while not Q.empty() :
			currentlyat = Q.get()
			checkarr[currentlyat] = True
			for x in self.EdgeMatrix :
				if x.node1 == currentlyat and x.node2 == v2 and x.weight != None :
					return True

				elif x.node2 == currentlyat and x.node1 == v2 and x.weight != None :
					return True

				elif x.node1 == currentlyat and x.weight != None and not checkarr[x.node2] :
					Q.put(x.node2)

				elif x.node2 == currentlyat and x.weight != None and not checkarr[x.node1] :
					Q.put(x.node1)

		return False

def gettopmostparent(parentarr, graph, node):
	if parentarr[node] == node :
		return node

	ans = gettopmostparent(parentarr, graph, parentarr[node])
	parentarr[node] = ans

	return ans


def kruskalsAlgorithm(graph, parentarr, rankarr, temparr) :
	MST = Graph(graph.Numberofvertices)
	count = 0

	for x in temparr :
		e1 = x.node1
		e2 = x.node2
		weight = x.weight
		
		p1 = gettopmostparent(parentarr, graph, e1)
		p2 = gettopmostparent(parentarr, graph, e2)

		if p1 != p2 :

			if count == graph.Numberofvertices - 1 :
				break

			MST.addEdge(e1, e2, weight)
			count += 1
			if rankarr[e1] > rankarr[e2]:
				parentarr[e2] = e1 

			elif rankarr[e2] > rankarr[e1]:
				parentarr[e1] = e2 

			else :
				parentarr[e1] = e2 
				rankarr[e2] += 1

	return MST


def printedgematrix(mst) :
	for x in mst.EdgeMatrix :
		print(f"In the MST there is an edge between {min(x.node1, x.node2)} and {max(x.node1, x.node2)} of weight {x.weight} ")

T = int(input("Enter the number of vertices you want in your graph \n"))
graph = Graph(T)
Edges = int(input("Enter the number of edges the graph has \n"))
for i in range(Edges):
	n1, n2, w = [int(x) for x in input().split()]
	graph.addEdge(n1, n2, w)


temparr = sorted(graph.EdgeMatrix, key = lambda Edge : Edge.weight)

parentarr = [i for i in range(T)]
rankarr = [0 for i in range(T)]

mst = kruskalsAlgorithm(graph, parentarr, rankarr, temparr) 
printedgematrix(mst)