def geometric_sum(k):
	if k == 0:
		return 1

	return (1/2)**k + geometric_sum(k - 1)

k = int(input())
ans = round(geometric_sum(k), 5)
print(ans)
