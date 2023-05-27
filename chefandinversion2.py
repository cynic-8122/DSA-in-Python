def merge(arr1, arr2) :
	i = 0
	j = 0
	count = 0
	arr = []
	while i < len(arr1) and j < len(arr2) :
		if arr1[i] <= arr2[j] :
			arr.append(arr1[i])
			i += 1

		else :
			count += len(arr1) - i + 1
			arr.append(arr2[j])
			j += 1

	if i < len(arr1) :
		while i < len(arr1) :
			arr.append(arr1[i])
			i += 1

	else:
		while j < len(arr2) :
			arr.append(arr2[j])
			j += 1

	return arr, count

def mergesort(arr, left, right, totalcount) :
	if left == right :
		return [arr[left]]
	mid = (left + right) // 2

	x = mergesort(arr, left, mid, totalcount)
	y = mergesort(arr, mid + 1, right, totalcount)

	m, count2 = merge(x, y)
	totalcount += int(count2)
	if left == 0 and right == (len(arr) - 1) :
		print(totalcount)
	return m

arr = [int(x) for x in input().split()]
n = len(arr)
p = mergesort(arr, 0, (n - 1), 0)



