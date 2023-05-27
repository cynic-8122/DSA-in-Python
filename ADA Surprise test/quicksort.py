import random

def quicksort(arr, l, r):
	if l >= r :
		return

	pivot = random.randrange(l, r)

	pivotidx = helper(arr, pivot, l, r)

	quicksort(arr, l, pivotidx - 1)
	quicksort(arr, pivotidx + 1, r)

def helper(arr, pivot, i, j):
	pivotval = arr[pivot]

	count = 0
	for t in range(i, j+1):
		if arr[t] < pivotval :
			count += 1


	pivotidx = i + count
	arr[pivot], arr[pivotidx] = arr[pivotidx], arr[pivot]

	while i < pivotidx and j > pivotidx :
		if arr[i] < pivotval :
			i += 1

		if arr[j] >= pivotval :
			j -= 1

		if arr[i] >= pivotval and arr[j] < pivotval :
			arr[i], arr[j] = arr[j], arr[i]

	return pivotidx

arr = [int(x) for x in input().split()]

quicksort(arr, 0, len(arr) - 1)
print(arr)
