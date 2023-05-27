def LinearSearch(arr, ele):
	for i in range(len(arr)):
		if arr[i] == ele :
			print('YES')
			return

	print("No")

arr = [int(x) for x in input().split()]
ele = int(input())

LinearSearch(arr, ele)