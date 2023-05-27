
def Triangle(matrix):
	i = 1
	ans = float('inf')
	while i < len(matrix):
		j = 0
		while j <= i:
			ans1 = float('inf') if j-1 < 0 else matrix[i-1][j-1]
			ans2 = float('inf') if j > i-1 else matrix[i-1][j]

			matrix[i][j] += min(ans1, ans2)

			if i == len(matrix) - 1:
				ans = min(ans, matrix[i][j])


			j += 1

		#print('Inside loop') 

		i += 1

	return ans 

n = int(input())

matrix = []

for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

print(Triangle(matrix))

			

