def sum_of_n_natural(n):
	if n <1 :
		return None
	if n == 1:
		return 1
	return n + sum_of_n_natural(n - 1)


n = int(input())
print(sum_of_n_natural(n))

