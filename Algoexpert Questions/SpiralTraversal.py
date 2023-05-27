
def ZigZagTraversal(Matrix):
	ZigZagArr = []

	i = 0
	t = len(Matrix[0])
	p = len(Matrix)
	j = 0
	count = t*p
	while count:
		while i < t:
			ZigZagArr.append(Matrix[j][i])
			count -= 1
			i += 1

		i -= 1
		t -= 1
		j += 1
		while j < p :
			ZigZagArr.append(Matrix[j][i])
			count -= 1
			j += 1

		j -= 1
		p -= 1
		i -= 1
		while i >= (len(Matrix[0]) - t - 1):
			ZigZagArr.append(Matrix[j][i])
			count -= 1
			i -= 1

		i += 1
		j -= 1
		while j >= (len(Matrix) - p):
			ZigZagArr.append(Matrix[j][i])
			count -= 1
			j -= 1

		j += 1
		i += 1

	return ZigZagArr

Matrix = [[1, 3, 4, 10] ,[2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
print(ZigZagTraversal(Matrix))




