temp = 100000
dp = [-1]*temp
dp[0] = 0
def Fib(n, dp):
	if n == 0 or n == 1:
		return n

	if dp[n] != -1 :
		return dp[n]

	dp[n] = Fib(n-1, dp) + Fib(n-2, dp)

	return dp[n]

T = int(input("Enter the number of testcases"))

for i in range(T):
	n = int(input("Enter the value of n"))
	print(Fib(n, dp))

