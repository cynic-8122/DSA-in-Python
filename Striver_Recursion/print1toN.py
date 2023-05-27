def print1toN(n, i = 1):
	if i > n:
		return

	print(i)
	print1toN(n, i+1)

N = int(input())
print1toN(N)
