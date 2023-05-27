N = int(input('Number of Vertices '))
adjlist = []
for i in range(N):
	print(f"i = {i}")
	arr = [int(x) for x in input().split()]
	adjlist.append(arr)

def TopologicalSort(currentlyat, visitedarr, stack, adjlist):
	visitedarr[currentlyat] = True
	for x in adjlist[currentlyat]:
		if visitedarr[x] == False:
			TopologicalSort(x, visitedarr, stack, adjlist)

	stack.append(currentlyat)


stack = []
visitedarr= [False for i in range(N)]
print(visitedarr)
TopologicalSort(0, visitedarr, stack, adjlist)
i = 0
j = len(stack)-1
while i <= j:
	stack[i], stack[j] = stack[j], stack[i]
	i += 1
	j -= 1

print(*stack)