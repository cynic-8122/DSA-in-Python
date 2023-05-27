def insertionsort(arr, n):
	for i in range(1, n):
		idx = i

		while idx - 1 >= 0 and arr[idx - 1] > arr[idx]:
			arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
			idx -= 1

	return arr

arr = [int(x) for x in input().split()]
print(insertionsort(arr, len(arr)))





