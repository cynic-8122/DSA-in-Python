def binarysearch(arr, left, right, target) :
	check = True
	while right >= left :
		mid = (left + right) // 2
		if arr[mid] == target :
			check = False
			return mid
		elif arr[mid] > target :
			right = mid
		else :
			left = mid + 1

	if check :
		return mid

arr = list(map(int, input().split()))
n = len(arr)
target = int(input("Target "))
x = binarysearch(arr, 0, (n-1), target)
print(arr[x])


