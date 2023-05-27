import copy

def printsubsets(arr, temparr, i= 0):
	if i > len(arr):
		return

	if i == len(arr):
		print(temparr)
		return

	printsubsets(arr, temparr, i + 1)
	t = copy.deepcopy(temparr)
	t.append(arr[i])
	printsubsets(arr, t, i + 1)


arr = [int(x) for x in input().split()]

printsubsets(arr, [])