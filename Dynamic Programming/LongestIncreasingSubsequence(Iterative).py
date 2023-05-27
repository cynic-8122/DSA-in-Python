
def LIS(arr, n):
	if n == 0 :
		return n 

	dp = [-1 for i in range(n)]

	ans = 1
	for i in reversed(range(n)):
		currentelement = arr[i]
		tempans = 0
		for j in range(i + 1, n):
			if arr[j] > currentelement :
				tempans = max(tempans, dp[j])

		dp[i] = 1 + tempans
		ans = max(ans, dp[i])
		
	return ans

arr = [int(x) for x in input().split()]

print(LIS(arr, len(arr)))



