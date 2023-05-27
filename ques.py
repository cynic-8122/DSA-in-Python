def binarysearch(arr, left, right, target) :
	condition = 0
	check = True
	while right >= left :
		mid = (left + right) // 2
		if arr[mid] == target :
			check = False
			return mid
		elif arr[mid] > target :
			right = mid - 1
			condition = 1
		else :
			left = mid + 1
			condition = 2

	if check :
		if condition == 1 :
			return mid

		elif condition == 2 and mid + 1 < len(arr):
			return mid + 1

		else :
			print("No such case")
			exit("________fuck off__________")

arr = list(map(int, input().split()))
n = len(arr)
target = int(input("Target "))
x = binarysearch(arr, 0, (n-1), target)
print(arr[x], x)


