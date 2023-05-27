import random

def quicksort(arr, l, r):
	if l >= r :
		return
	pivot = random.randrange(l, r)
	i = l
	j = r
	count = 0
	for k in range(l, r+1):
		if arr[k] < arr[pivot]:
			count += 1

	arr[pivot], arr[count + l] = arr[count + l], arr[pivot]

	pivot = count + l
	
	while i < pivot and j > pivot :
		if arr[i] < arr[pivot]:
			i += 1

		if arr[j] >= arr[pivot]:
			j -= 1

		if arr[i] >= arr[pivot] and arr[j] < arr[pivot]:
			arr[i], arr[j] = arr[j], arr[i]
	
	quicksort(arr, l, pivot - 1)
	quicksort(arr, pivot + 1, r)

arr = [int(x) for x in input("Enter the array you want to sort using quicksort \n").split()]

quicksort(arr, 0, len(arr) - 1)
print(arr)

