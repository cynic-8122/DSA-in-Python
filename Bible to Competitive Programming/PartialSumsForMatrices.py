
n = int(input("Enter the number of rows "))
matrix = []
for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

def partialsum(matrix):
	n = len(matrix)
	m = len(matrix[0])

	ansarr = [[0 for i in range(m)]for i in range(n)]

	sumsofar = 0
	for j in range(m):
		sumsofar += matrix[0][j]
		ansarr[0][j] = sumsofar

	sumsofar = 0
	for i in range(n):
		sumsofar += matrix[i][0]
		ansarr[i][0] = sumsofar

	for i in range(1, n):
		for j in range(1, m):
			ansarr[i][j] = ansarr[i-1][j] + ansarr[i][j-1] - ansarr[i-1][j-1] + matrix[i][j]

	return ansarr

t = partialsum(matrix)
for i in range(n):
	print(*t[i])




