import math, sys

def minsquares(n, dp):
	t = math.sqrt(n)
	if t == int(t):
		dp[n] = 1
		return dp[n]

	if dp[n] != -1 :
		return dp[n]


	minans = float('inf')
	for i in range(1, int(t) + 1):
		tempans = minsquares(n - i*i, dp)
		minans = min(minans, tempans)

	dp[n] = 1 + minans
	return dp[n]

n = int(input())

dp = [-1 for i in range(n+1)]
dp[0] = 1
dp[1] = 1

print(minsquares(n, dp))