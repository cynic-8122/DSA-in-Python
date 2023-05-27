import math

def minsquares(n, dp):
	for i in range(1, n+1):
		temp = math.sqrt(i)
		if temp == int(temp) :
			dp[i] = 1

		else :
			minans = float('inf')
			for j in range(1, int(temp) + 1):
				minans = min(minans, dp[i - j*j])

			dp[i] = 1 + minans

	return dp[-1]

n = int(input())

dp = [-1 for i in range(n+1)]
dp[0] = 1

print(minsquares(n, dp))

