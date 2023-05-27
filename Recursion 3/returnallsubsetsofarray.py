
import copy

def allsubsets(arr, i):
	if i <= 0:
		return [[]]

	temparr = allsubsets(arr, i-1)

	t = len(temparr)
	for j in range(t):
		temp = copy.deepcopy(temparr[j])
		temp.append(arr[i-1])
		temparr.append(temp)

	return temparr

arr = [int(x) for x in input().split()]

print(allsubsets(arr, len(arr)))

