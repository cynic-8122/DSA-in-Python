n = int(input())

matrix = []
for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

def printallpaths(matrix, n):
	temparr = [[0 for i in range(n)] for i in range(n)]
	printpathshelper(matrix, 0, 0, n, temparr)

def printpathshelper(matrix, i, j, n, ansarr):
	if i == n-1 and j == n-1:
		ansarr[i][j] = 1
		print(ansarr)
		return

	if i < 0 or j < 0 or i >= n or j >= n or matrix[i][j] == 0 or ansarr[i][j] == 1:
		return

	ansarr[i][j] = 1
	printpathshelper(matrix, i + 1, j, n, ansarr)
	printpathshelper(matrix, i - 1, j, n, ansarr)
	printpathshelper(matrix, i, j + 1, n, ansarr)
	printpathshelper(matrix, i, j - 1, n, ansarr)
	ansarr[i][j] = 0


printallpaths(matrix, n)
