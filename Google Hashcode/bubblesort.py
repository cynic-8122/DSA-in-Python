def bubblesort(arr, n):
	for i in range(n):
		for j in range(0, n - i - 1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

			j += 1

	return arr

arr = [int(x) for x in input().split()]

print(bubblesort(arr, len(arr)))