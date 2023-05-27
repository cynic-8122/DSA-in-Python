def multiplication(n, m):
	if n == 0 or m == 0 :
		return 0

	return n + multiplication(n, m - 1)

n, m = [int(x) for x in input().split()]
print(multiplication(n, m))
