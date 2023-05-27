import random

def swap(arr, left, right, pivot_idx):
	i = left
	j = right
	while i < pivot_idx and j > pivot_idx :
		if arr[i] >= arr[pivot_idx] and arr[j] < arr[pivot_idx]:
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1

		elif arr[i] < arr[pivot_idx]:
			i += 1

		elif arr[j] >= arr[pivot_idx]:
			j -= 1

def quicksort(arr, left, right):
	if left >= right :
		return

	pivot_idx = random.randrange(left, right)
	pivot = arr[pivot_idx]

	count = 0
	for i in range(left, right+1):
		if arr[i] < pivot :
			count += 1


	arr[pivot_idx], arr[count + left] = arr[count + left], arr[pivot_idx]
	pivot_idx = left + count #You forgot this bitch right here (again)
	swap(arr, left, right, pivot_idx)

	quicksort(arr, left, pivot_idx - 1)
	quicksort(arr, pivot_idx + 1, right)

	return arr

arr = [int(x) for x in input().split()]
print(quicksort(arr, 0, len(arr) - 1))