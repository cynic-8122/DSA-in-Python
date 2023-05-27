n = int(input())

def fib(n) :
	if n == 0 or n == 1 :
		return n

	a1 = fib(n - 1)
	a2 = fib(n - 2)

	print(a1, end = " ")
	print(a2)

	return a1 + a2

print(fib(n))


