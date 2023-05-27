from queue import PriorityQueue as pq 

N = int(input("Number of Nodes "))
startingnode = int(input("Starting Node "))
adjlist = []
for i in range(N):
	ele = int(input("Number of adjacent nodes "))
	arr = []
	for i in range(ele):
		pair = [int(x) for x in input().split()]
		arr.append(pair)

	adjlist.append(arr)

distarr = [float('inf') for i in range(N)]
distarr[startingnode] = 0
q = pq()
ele = [0, startingnode]
q.put(ele)
def dijkstra(adjlist, distarr, q):
	while not q.empty():
		dist, currentnode = q.get()
		for x in adjlist[currentnode]:
			node, weight = x
			if distarr[node] > dist + weight:
				newdist = dist + weight
				ele = [newdist, node]
				q.put(ele)
				distarr[node] = newdist


dijkstra(adjlist, distarr, q)
print(distarr)
