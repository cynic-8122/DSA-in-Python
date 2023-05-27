def merge(l1, l2):
	sorted_arr = []
	i = 0
	j = 0
	while i < len(l1) and j < len(l2) :
		if l1[i] <= l2[j] :
			sorted_arr.append(l1[i])
			i += 1

		else :
			sorted_arr.append(l2[j])
			j += 1

	while i < len(l1):
		sorted_arr.append(l1[i])
		i += 1

	while j < len(l2):
		sorted_arr.append(l2[j])
		j += 1

	return sorted_arr


def merge_sort(arr, l, r):
	if l == r :
		return [arr[l]]

	mid = (l + r) // 2
	x = merge_sort(arr, l , mid)
	y = merge_sort(arr, mid+1, r)

	return merge(x, y)

print('Enter the array you want to sort ')
arr = [int(x) for x in input().split()]
print(merge_sort(arr, 0, len(arr) - 1))


