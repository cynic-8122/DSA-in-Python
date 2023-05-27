
n = int(input())
dp = [-1 for i in range(n+1)]
def maxsumsubsequence(arr, n, dp):
	if n == 1:
		return arr[0]

	if n < 1:
		return 0

	if dp[n-1] != -1:
		return dp[n-1]

	take = maxsumsubsequence(arr, n-3, dp) + arr[n-1]

	nottake = maxsumsubsequence(arr, n-2, dp) + 0

	dp[n-1] = max(take, nottake)

	return dp[n-1]

arr = [int(x) for x in input().split()]

print(maxsumsubsequence(arr, n, dp))
 