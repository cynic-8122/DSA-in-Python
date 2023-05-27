import random

def quicksort(arr, l, r):
	if l >= r:
		return
	temp  = arr[l:(r + 1)]
	x = random.choice(temp)
	idx = arr.index(x)
	count = 0
	for i in range(l, r + 1):
		if arr[i] <= x:
			count += 1

	count -= 1
	arr[idx], arr[l + count] = arr[l + count], arr[idx]
	i = l 
	j = r 
	while i < l + count and j > l + count :
		check1 = False
		check2 = False
		if arr[i] > x :
			check1 = True

		if arr[j] <= x:
			check2 = True

		if check1 and check2 :
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1

		elif check1 :
			j -= 1

		elif check2 :
			i += 1

		else :
			i += 1
			j -= 1

	quicksort(arr, l, l+count - 1)
	quicksort(arr, l + count + 1, r)

	return arr

arr = [int(x) for x in input().split()]
print(quicksort(arr, 0, len(arr) - 1)) 