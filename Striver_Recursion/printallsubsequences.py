def printallsubsequences(arr, n, ans = ''):
	if len(arr) == 0:
		print(ans)
		return

	printallsubsequences(arr[1:], n - 1, ans + str(arr[0]) + " ")
	printallsubsequences(arr[1:], n - 1, ans)

arr = [int(x) for x in input().split()]

printallsubsequences(arr, len(arr))