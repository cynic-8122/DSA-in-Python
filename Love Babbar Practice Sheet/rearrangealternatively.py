def partition(arr):
	i = 0
	j = 0

	while j < len(arr) and i < len(arr):
		if arr[i] < 0:
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
			
		i += 1


	print(*arr)
	return j


#all the elements to the left of j are negative

def rearrange(arr):
	pivot = partition(arr)

	i = 0
	j = pivot
	print(pivot)

	while i < len(arr) and j < len(arr):
		arr[i], arr[j] = arr[j], arr[i]
		i += 2
		j += 1

	

arr = [int(x) for x in input().split()]
rearrange(arr)
print(*arr)


