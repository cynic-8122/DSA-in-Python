def minsteps(n, dp):

	if n < 1 :
		return -1

	if n == 1 :
		return dp[n]

	ans1 = float('inf')
	if n%3 == 0 and dp[n//3] != -1 :
		return 1 + dp[n//3]

	else :
		ans1 = 1 + minsteps(n//3, dp)

	ans2 = float('inf')
	if n%2 == 0 and dp[n//2] != -1 :
		return dp[n//2]

	else :
		ans2 = 1 + minsteps(n//2, dp)
	
	ans3 = 1 + minsteps(n-1, dp)

	dp[n] = 1 + min(ans1, ans2, ans3)

	return dp[n]


n = int(input())
dp = [-1 for i in range(n + 1)]
dp[1] = 0
dp[0] = 0
print(minsteps(n, dp))
