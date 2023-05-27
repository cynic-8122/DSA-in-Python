import random

def quicksort(arr, l, r):
	if l >= r :
		return

	pivotidx = random.randrange(l, r)

	count = 0
	pivotval = arr[pivotidx]

	for k in range(l, r+1):
		if arr[k] < pivotval :
			count += 1

	arr[pivotidx], arr[l + count] = arr[l + count], arr[pivotidx]
	pivotidx = l + count

	i = l
	j = r 

	while i < pivotidx and j > pivotidx :
		if arr[i] < pivotval :
			i += 1

		if arr[j] >= pivotval :
			j -= 1

		if arr[i] >= pivotval and arr[j] < pivotval :
			arr[i], arr[j] = arr[j], arr[i]

	quicksort(arr, l, pivotidx - 1)
	quicksort(arr, pivotidx + 1, r)

arr = [int(x) for x in input().split()]

quicksort(arr, 0, len(arr) - 1)

print(*arr)