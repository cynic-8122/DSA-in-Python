def selectionsort(arr):
	i = 0
	while i < len(arr):
		j = i 
		minval = float('inf')
		minidx = -1
		while j < len(arr):
			if arr[j] < minval :
				minval = arr[j]
				minidx = j

			j += 1

		arr[i], arr[minidx] = arr[minidx], arr[i]
		i += 1

arr = [int(x) for x in input().split()]
selectionsort(arr)
print(arr)