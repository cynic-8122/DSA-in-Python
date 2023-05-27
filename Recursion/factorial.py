def factorial(n):
	if n == 0 or n == 1 :
		return 1
	ans = factorial(n - 1)
	ans *= n
	return ans

n = int(input())
print(factorial(n))
