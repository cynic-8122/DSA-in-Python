import copy 
ansarr = []

def subsetswithsumk(arr, k, i, temparr):
	if k == 0 and i == len(arr):
		t = copy.deepcopy(temparr)
		ansarr.append(t)
		return

	elif i >= len(arr):
		return temparr

	elif k < 0:
		return

	temparr.append(arr[i])
	subsetswithsumk(arr, k-arr[i], i+1, temparr)

	temparr.pop()
	subsetswithsumk(arr, k, i+1, temparr)

arr = [int(x) for x in input().split()]
k = int(input())

subsetswithsumk(arr, k, 0, [])
print(ansarr)




