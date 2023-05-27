class Entry:
	def __init__(self, node1, node2, weight):
		self.node1 = node1
		self.node2 = node2
		self.weight = weight

N = int(input("Number of vertices "))
adjmatrix = []
temparr = []
for i in range(N):
	arr = [int(x) for x in input().split()]
	for j in range(N):
		if arr[j]:
			ele = Entry(i, j, arr[j])
			temparr.append(ele)

	adjmatrix.append(arr)

def kruskalsalgo(temparr, N):
	temparr = sorted(temparr, key = lambda Entry:Entry.weight)
	MST = [[0 for i in range(N)] for i in range(N)]
	parentarr = [i for i in range(N)]
	rankarr = [0 for i in range(N)]
	count = 0
	i = 0
	while i < len(temparr) and count != N-1:
		ele = temparr[i]
		node1 = ele.node1
		node2 = ele.node2
		weight = ele.weight
		if not haspath(node1, node2, parentarr, rankarr):
			MST[node1][node2] = weight
			MST[node2][node1] = weight
			count += 1

		i += 1

	return MST

def getparent(node, parentarr):
	if parentarr[node] == node:
		return node 

	parentarr[node] = getparent(parentarr[node], parentarr)
	return parentarr[node]

def haspath(node1, node2, parentarr, rankarr):
	parent1 = getparent(node1, parentarr)
	parent2 = getparent(node2, parentarr)
	print(f"node1 = {node1}, node2 = {node2}, {parent1}, {parent2}")
	if parent1 == parent2:
		return True

	if rankarr[node1] > rankarr[node2]:
		parentarr[node2] = node1
		return False

	elif rankarr[node1] < rankarr[node2]:
		parentarr[node1] = node2
		return False

	else:
		parentarr[node1] = node2
		rankarr[node2] += 1

		return False


print(kruskalsalgo(temparr, N))

