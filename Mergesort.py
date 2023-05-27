def merge(arr1, arr2) :
	arr = []
	j = i = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j] :
			arr.append(arr1[i])
			i += 1
		else :
			arr.append(arr2[j])
			j += 1

	if j >= len(arr2) :
		while i < len(arr1) :
			arr.append(arr1[i])
			i += 1

	else :
		while j < len(arr2) :
			arr.append(arr2[j])
			j += 1

	return arr 

def mergesort(arr, left, right) :
	if left == right :
		return 	[arr[left]]

	mid = (right + left) // 2
	x = mergesort(arr, left, mid)
	print("x = ", x)
	y = mergesort(arr, mid + 1, right)
	output = merge(x, y)
	print("y = " , y)
	return output
	
arr = list(map(int, input().split()))
n = len(arr)
print(mergesort(arr, 0, (n - 1)))





