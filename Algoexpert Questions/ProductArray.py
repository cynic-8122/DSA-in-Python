
arr = [int(x) for x in input().split()]

def productarray(arr):
	ansarr = [1]
	tempans = 1
	for i in range(1, len(arr)):
		tempans *= arr[i-1]
		ansarr.append(tempans)

	tempans = 1
	for i in range(len(arr)-2, -1, -1):
		tempans *= arr[i+1]
		ansarr[i] *= tempans

	return ansarr

print(*productarray(arr))