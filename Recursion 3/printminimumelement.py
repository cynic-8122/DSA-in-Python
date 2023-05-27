def printmin(n, arr, ans = float('inf')):
	if n <= 0:
		print(ans)
		return

	printmin(n-1, arr, min(ans, arr[n-1]))

arr = [int(x) for x in input().split()]
printmin(len(arr), arr)