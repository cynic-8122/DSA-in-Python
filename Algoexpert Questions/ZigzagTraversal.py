
def zigzagtraversal(matrix):
	r = len(matrix)
	c = len(matrix[0])

	count = r*c 
	ZigZagArr = []
	i = 0
	j = 0

	while count > 0 :
		while i < r and j >= 0:
			ZigZagArr.append(matrix[i][j])
			count -= 1
			i += 1
			j -= 1 

		if i >= r:
			j += 2
			i = r - 1

		else:
			j = 0

		while i >= 0 and j < c:
			ZigZagArr.append(matrix[i][j])
			count -= 1
			i -= 1
			j += 1

		if j >= c:
			i += 2
			j = c-1

		else:
			i = 0
				

	return ZigZagArr

matrix = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(zigzagtraversal(matrix))


