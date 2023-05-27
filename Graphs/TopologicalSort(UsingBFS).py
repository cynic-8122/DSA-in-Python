import queue

N = int(input("Number of Vertices"))
adjlist = []
indegree = [0 for i in range(N)]
for i in range(N):
	arr = [int(x) for x in input().split()]
	adjlist.append(arr)
	for x in arr:
		indegree[x] += 1

def checkCycle(adjlist, n):
	ancestors = set()
	visitedarr = [False for i in range(n)]
	for i in range(n):
		if visitedarr[i] == False:
			ancestors.clear()
			ans = Helper(i, adjlist, ancestors, visitedarr)
			if ans == True:
				return True


	return False

def Helper(currentlyat, adjlist, ancestors, visitedarr):
	visitedarr[currentlyat] = True
	ancestors.add(currentlyat)
	for x in adjlist[currentlyat]:
		if visitedarr[x] == True and x in ancestors:
			return True

		if visitedarr[x] == False:
			return Helper(x, adjlist, ancestors, visitedarr)


	ancestors.remove(currentlyat)
	return False

def Toposort(adjlist, n, indegree):
	Q = queue.Queue()
	
	