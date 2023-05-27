
def LIS(arr, i, n, dp, comparewith = -float('inf')):
	if i >= n :
		return 0

	currentelement = arr[i]
	ans1 = -float('inf')
	if arr[i] >= comparewith and dp[i] == -1:
		ans1 = 1 + LIS(arr, i+1, n, dp, arr[i])
		dp[i] = ans1

	elif arr[i] >= comparewith :
		ans1 = dp[i]

	ans2 = LIS(arr, i+1, n, dp, comparewith)

	return max(ans1, ans2)


arr = [int(x) for x in input().split()]
dp = [-1 for i in range(len(arr))]

print(LIS(arr, 0, len(arr), dp))