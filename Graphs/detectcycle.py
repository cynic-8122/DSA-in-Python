'''
Detect Cycle in a Directed Unweighted Graph.
'IMPORTANT':
To detect cycle in a directed graph, we can't use the same old algorithm as used for an undirected graph.
Algorithm for undirected graph:
# Use BFS or DFS while maintaining a visited array and as soon as we land at any node which has been previously visited, 
we simply declare that the graph has a cycle.

# If this condition doesn't arrive for any node of the graph, we conclude that the graph is acyclic.
'''
import queue

class Graph:
	def __init__(self, numberofvertices):
		self.numberofvertices = numberofvertices
		self.adjlist = []

	def takeinput(self):
		n = self.numberofvertices
		for i in range(n):
			numberofelements = int(input("number of elements "))
			if numberofelements:
				adjacentnodes = [int(x) for x in input().split()]

			else:
				adjacentnodes = []

			self.adjlist.append(adjacentnodes)


def detectcycle(graph):
	#Cycle can be detected using BFS or DFS
	#Using DFS (It can be done using BFS by Kahn's algorithm)
	ancestors = set()
	# Call a BFS while maintaining a ancestors set
	n = graph.numberofvertices
	visitedarr = [False for i in range(n)]
	for i in range(n):
		if visitedarr[i] == False:
			ancestors.clear()
			ans = DFS(graph, i, ancestors, visitedarr)
			if ans == True: 
				return ans 


	return False

def DFS(graph, currentlyat, ancestors, visitedarr):
	ancestors.add(currentlyat)
	ans = False
	visitedarr[currentlyat] = True
	for x in graph.adjlist[currentlyat]:
		ans = False
		if visitedarr[x] == True and x in ancestors:
			return True

		if visitedarr[x] == False:
			ans = DFS(graph, x, ancestors, visitedarr)

		if ans == True:
			return True

	ancestors.remove(currentlyat)
	return ans 


n = int(input("Number of vertices"))
G = Graph(n)
G.takeinput()
print(detectcycle(G))

