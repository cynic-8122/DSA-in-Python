N = int(input())
startingnode = int(input())
adjlist = []
for i in range(N):
	ele = int(input("Number of adjacent nodes "))
	arr = []
	for i in range(ele):
		pair = [int(x) for x in input().split()]
		arr.append(pair)

	adjlist.append(arr)

def topologicalsort(adjlist, stack, visitedarr, currentnode):
	visitedarr[currentnode] = True

	for x in adjlist[currentnode]:
		if visitedarr[x[0]] == False:
			topologicalsort(adjlist, stack, visitedarr, x[0])

	stack.append(currentnode)

def minpath(adjlist, stack, patharr):
	while len(stack):
		currentnode = stack.pop()
		if patharr[currentnode] != float('inf'):
			for x in adjlist[currentnode]:
				node, weight = x
				patharr[node] = min(patharr[node], patharr[currentnode]+weight)


visitedarr = [False for i in range(N)]
patharr = [float('inf') for i in range(N)]
patharr[startingnode] = 0
stack = []
topologicalsort(adjlist, stack, visitedarr, 0)
minpath(adjlist, stack, patharr)
print(patharr)