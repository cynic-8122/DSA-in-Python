''' 
Kruskal's Algorithm with union by rank and path compression
'''

class Edge :
	def __init__(self, node1, node2, weight = 1):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight

parentarr = [i for i in range(Graph.Numberofvertices)]
rankmatrix = [0 for i in range(Graph.Numberofvertices)]
tempmatrix = sorted(EdgeMatrix, key = lambda Edge: Edge.weight)


def getparent(node, parentarr):
	if parentarr[node] == node :
		return

	parent = getparent(parentarr[node], parentarr)

	parentarr[node] = parent

	return parent

def KrusksalAlgorithm(parentarr, rankmatrix, tempmatrix):
	MST = Graph(Graph.Numberofvertices)
	count = 0
	i = 0
	while count != (Graph.Numberofvertices - 1) and i < len(tempmatrix):
		node1 = tempmatrix[i][0]
		node2 = tempmatrix[i][1]
		t = getparent(node1)
		p = getparent(node2)

		if p != t :
			count += 1
			MST.addEdge(node1, node2, weight)

			if rankmatrix[node1] > rankmatrix[node2]:
				parentarr[node2] = node1

			else :

		i += 1

