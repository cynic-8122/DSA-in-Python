
def maximumfallingpathsum(matrix, i, col):
	if i == 1 :
		return matrix[0][j-1]

	if i == len(matrix):
		ans = -float('inf')
		for j in range(col, 0, -1):
			temp1 = -float('inf') if j - 1 < 1 else maximumfallingpathsum(matrix, i-1, j-1)
			temp2 = -float('inf') if j + 1 > len(matrix) else maximumfallingpathsum(matrix, i-1, j+1)
			temp3 = maximumfallingpathsum(matrix, i-1, j)

			tempans = max(temp1, temp2, temp3) + matrix[i-1][j-1]

			ans = max(ans, tempans)

		return ans 

	else:
		temp1 = -float('inf') if col - 1 < 1 else maximumfallingpathsum(matrix, i-1, col-1)
		temp2 = -float('inf') if col + 1 > len(matrix) else maximumfallingpathsum(matrix, i-1, col+1)
		temp3 = maximumfallingpathsum(matrix, i-1, col)

		return max(temp1, temp2, temp3) + matrix[i-1][col-1]


n = int(input())

matrix = []
for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

print(maximumfallingpathsum(matrix, n, len(matrix[0])))