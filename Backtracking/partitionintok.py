n = int(input('Size of the array '))
k = int(input('Number of partitions '))

arr = [int(x) for x in input().split()]

ansarr = []
temparr = [[] for i in range(k)]
def partition(arr, n, k, temparr, ansarr, emptycount, i):
	if i >= n:
		if emptycount == 0:
			print(temparr)
			
		return

	check = True
	for t in range(k):
		if len(temparr[t]):
			temparr[t].append(arr[i])
			partition(arr, n, k, temparr, ansarr, emptycount, i+1)
			temparr[t].pop()

		elif check:
			emptycount -= 1
			temparr[t].append(arr[i])
			check = False
			partition(arr, n, k, temparr, ansarr, emptycount, i+1)
			temparr[t].pop()
			emptycount += 1



partition(arr, n, k, temparr, ansarr, k, 0)
#print(ansarr)



