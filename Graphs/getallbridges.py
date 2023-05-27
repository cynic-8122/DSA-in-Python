N = int(input("Number of Vertices "))
adjlist = []
for i in range(N):
	arr = [int(x) for x in input().split()]
	adjlist.append(arr)

time = [1]
mintime = [float('inf') for i in range(N)]
visitedarr = [False for i in range(N)]
bridges = []
starttime = [float('inf') for i in range(N)]

def getbridges(adjlist, visitedarr, mintime, bridges, N, time, starttime):
	for i in range(N):
		if visitedarr[i] == False:
			Helper(-1, i, visitedarr, adjlist, mintime, bridges, N, time, starttime)

def Helper(parent, currentnode, visitedarr, adjlist, mintime, bridges, N, time, starttime, currenttime=1):
	visitedarr[currentnode] = True
	mintime[currentnode] = starttime[currentnode] = time[0]
	for x in adjlist[currentnode]:
		if visitedarr[x] == False:
			time[0] += 1
			Helper(currentnode, x, visitedarr, adjlist, mintime, bridges, N, time, starttime, time[0])

		if x == parent:
			continue

		else:
			mintime[currentnode] = min(mintime[currentnode], mintime[x])
			if starttime[currentnode] < mintime[x]:
				bridges.append([currentnode, x])

			


getbridges(adjlist, visitedarr, mintime, bridges, N, time, starttime)
print(*bridges)


