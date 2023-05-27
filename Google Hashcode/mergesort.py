def merge(arr1, arr2):
	i = 0
	j = 0

	temparr = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			temparr.append(arr1[i])
			i += 1

		else :
			temparr.append(arr2[j])
			j += 1

	while i < len(arr1):
		temparr.append(arr1[i])
		i += 1

	while j < len(arr2):
		temparr.append(arr2[j])
		j += 1

	return temparr

def mergesort(arr, l, r):
	if l > r :
		return

	if l == r:
		return [arr[l]]

	mid = (l + r)//2
	x = mergesort(arr, l , mid)
	y = mergesort(arr, mid+1, r)

	return merge(x, y)

arr = [int(x) for x in input().split()]

print(mergesort(arr, 0, len(arr) - 1))