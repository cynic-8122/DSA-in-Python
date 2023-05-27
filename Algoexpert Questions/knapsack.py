import copy

def subsequences(arr, i = 0) :
	if i >= len(arr):
		return [[]]

	ansarr = subsequences(arr, i+1)
	t = len(ansarr)
	for j in range(t):
		temp = copy.deepcopy(ansarr[j])
		temp.insert(0, arr[i])
		ansarr.append(temp)

	return ansarr


arr = [int(x) for x in input().split()]
print(subsequences(arr))
