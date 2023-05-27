def selectionsort(arr, n):

	for i in range(n):
		minval =  float('inf')
		idx = -1
		for j in range(i, n):
			if arr[j] < minval :
				minval = arr[j]
				idx = j

		arr[idx], arr[i] = arr[i], arr[idx]

	return arr

arr = [int(x) for x in input().split()]

print(selectionsort(arr, len(arr)))

