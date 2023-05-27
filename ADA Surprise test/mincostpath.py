n = int(input())
m = int(input())

matrix = []
for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

def mincostpath(matrix, n, m):
	if n < 1 or m < 1:
		return float('inf')

	if n == 1 and m == 1:
		return matrix[0][0]

	ans1 = mincostpath(matrix, n-1, m)
	ans2 = mincostpath(matrix, n, m-1)
	ans3 = mincostpath(matrix, n-1, m-1)

	return matrix[n-1][m-1] + min(ans1, ans2, ans3)

print(mincostpath(matrix, n, m))