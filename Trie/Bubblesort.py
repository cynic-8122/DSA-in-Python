arr = [int(x) for x in input().split(',')]

def bubblesort(arr):
	arr.sort()


	return arr


ansarr = bubblesort(arr)
for i in range(len(ansarr)):
	ansarr[i] = str(ansarr[i])

ansarr = ",".join(ansarr)
print(ansarr)

