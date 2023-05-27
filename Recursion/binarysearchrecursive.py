def binary_search(arr, l, r, target) :
	if l > r :
		return
	mid = (l + r)//2
	#x = arr[mid]
	print(arr[mid])
	if l == r :
		return arr[mid]
	
	if target == arr[mid]:
		x = arr[mid]
		return x
	elif target < arr[mid] :
		x = binary_search(arr, l, mid - 1, target)
		return x

	else :
		binary_search(arr, mid + 1, r, target)

	#return x

arr = [int(x) for x in input().split()]
arr.sort()
target = int(input())
print(binary_search(arr, 0, len(arr) - 1, target))
