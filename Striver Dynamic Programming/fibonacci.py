
n = int(input())


def fibonacci(n):
	prev = 1
	prev2 = 0

	i = 2
	while i <= n:
		t = prev + prev2
		prev2 = prev 
		prev = t 
		i += 1

	return prev 

print(fibonacci(n))
