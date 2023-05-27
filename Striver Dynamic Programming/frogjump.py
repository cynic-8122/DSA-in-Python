
def frogjump(arr, n):
	if n <= 0:
		return 0

	cost1 = frogjump(arr, n - 1) + abs(arr[n] - arr[n-1])
	cost2 = float('inf')
	if i > 1:
		cost2 = frogjump(arr, n-2) + abs(arr[n] - arr[n-2])

	return min(cost1, cost2)

arr = [int(x) for x in input().split()]
print(frogjump(arr, len(arr) - 1))