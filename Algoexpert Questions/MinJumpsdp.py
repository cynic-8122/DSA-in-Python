
def minjumps(arr, i, dp):
	if i >= len(arr) - 1:
		return 0

	t = arr[i]

	ans = float('inf')
	for j in range(1, t+1):
		if i + j < len(arr) and dp[i + j] != -1 :
			tempans = 1 + dp[i + j]

		else :
			tempans = 1 + minjumps(arr, i + j, dp)
			if i + j < len(arr):
				dp[i + j] = tempans - 1

		ans = min(ans, tempans)

	dp[i] = ans
	return dp[i]

arr = [int(x) for x in input().split()]

dp = [-1]*(len(arr))

print(minjumps(arr, 0, dp))
