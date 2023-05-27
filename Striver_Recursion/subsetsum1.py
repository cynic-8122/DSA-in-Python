
def subsetsum(arr, ansarr,  i = 0, sumsofar = 0):
	if i > len(arr):
		return 

	if i == len(arr):
		ansarr.append(sumsofar)
		return

	subsetsum(arr, ansarr, i+1, sumsofar+arr[i])
	subsetsum(arr, ansarr, i+1, sumsofar)

arr = [int(x) for x in input().split()]

ansarr = []
subsetsum(arr, ansarr)
print(ansarr)