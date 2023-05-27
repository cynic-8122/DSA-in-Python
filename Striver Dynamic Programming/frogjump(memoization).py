
n = int(input())
dp = [-1 for i in range(n+1)]

def frogjump(arr, n, dp):
	if n <= 1:
		return 0

	if dp[n-2] != -1:
		cost1 = dp[n-2] + abs(arr[n-1] - arr[n-2])

	else:
		t = frogjump(arr, n-2, dp)
		dp[n-2] = t 
		cost1 = t + abs(arr[n-1] - arr[n-2])

	if dp[n-3] != -1:
		cost2 = dp[n-3] + abs(arr[n-1] - arr[n-3])

	else:
		t2 = frogjump(arr, n-3, dp)
		dp[n-3] = t2 
		cost2 = t2 + abs(arr[n-1] + arr[n-3])

	dp[n-1] = min(cost1, cost2)

	return dp[n-1]

arr = [int(x) for x in input().split()]

print(frogjump(arr, len(arr), dp))