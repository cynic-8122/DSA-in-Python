
def printlcs(str1, str2):
	dp = [[-1 for i in range(len(str2)+1)] for i in range(len(str1) + 1)]

	i = 0
	for j in range(len(str2)+1):
		dp[i][j] = 0


	for i in range(1, len(str1)+1):
		dp[i][0] = 0


	i = 1
	while i < len(str1) + 1:
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]

			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])


		i += 1


	ans = ''
	i = len(str1)
	j = len(str2)

	while i > 0 and j > 0:
		if str1[i-1] == str2[j-1]:
			ans = str1[i-1] + ans
			i -= 1
			j -= 1

		elif dp[i-1][j] > dp[i][j-1]:
			i -= 1

		else:
			j -= 1

	return ans

str1 = str(input('Enter String 1 '))
str2 = str(input('Enter String 2 '))

print(printlcs(str1, str2))