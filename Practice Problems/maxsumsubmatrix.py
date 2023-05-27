'''
Given a 2D matrix M of dimensions RxC. Find the maximum sum subarray in it.

Example 1:

Input:
R=4
C=5
M=[[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
Output:
29
Explanation:
The matrix is as follows and the
blue rectangle denotes the maximum sum
rectangle.
'''
'''
R, C = [int(x) for x in input().split()]
matrix = []
for i in range(R):
	row_arr = [int(x) for x in input().split()]
	matrix.append(row_arr)
'''

R=4
C=5
matrix = [[1,2,-1,-4,-20],
[-8,-3,4,2,1],
[3,8,10,1,3],
[-4,-1,1,7,-6]]
def maximum_sum_submatrix(matrix, R, C):
	if R >= C :
		# fix the variables along the columns and take prefix array of rows
		prefix_matrix = []

		for i in range(C):
			row_prefix_arr = []
			sum_so_far = 0
			for j in range(R):
				sum_so_far += matrix[i][j]
				row_prefix_arr.append(sum_so_far)
			prefix_matrix.append(row_prefix_arr)

		ans = 0
		for i in range(C):
			for j in range(i, C):
				L = i 
				R = j
				temp_arr = []
				for k in range(R):
					val = row_prefix_arr[k][R] - row_prefix_arr[k][L] + matrix[k][L]
					temp_arr.append(val)
				# Now the problem boils down to choosing the maximum sum subarray from the temp_arr
				# Use kadane's algorithm to do the remaining
				max_sum = -float('inf')
				sum_so_far = 0
				for i in range(R):
					sum_so_far += temp_arr[i]
					
					if sum_so_far < 0 :
						sum_so_far = 0
					max_sum = max(max_sum, sum_so_far)
			ans = max(ans, max_sum)

	else :
		# fix the variables along the rows and take prefix array of columns
		prefix_matrix = []
		prefix_matrix.append(matrix[0])

		for i in range(1, R):
			column_prefix_arr = []
			sum_so_far = 0

			for j in range(C):
				sum_so_far = prefix_matrix[i - 1][j] + matrix[i][j]
				column_prefix_arr.append(sum_so_far)

			prefix_matrix.append(column_prefix_arr)
		print(prefix_matrix)
		ans = 0
		for i in range(R):
			for j in range(i, R):
				L = i 
				R = j
				temp_arr = []
				for k in range(C):
					a = prefix_matrix[R][k]
					print("L", L)
					print('i', i)
					print("k", k)
					b = prefix_matrix[L][k]
					c = matrix[L][k]
					val = prefix_matrix[R][k] - prefix_matrix[L][k] + matrix[L][k]
					temp_arr.append(val)

				# Use the kadane's algorithm
				sum_so_far = 0
				max_sum = -float('inf')
				for i in range(C):
					sum_so_far += temp_arr[k]
					if sum_so_far < 0:
						sum_so_far = 0
					max_sum = max(max_sum, sum_so_far)
				ans = max(ans, max_sum)
	print(prefix_matrix)

	return ans


print(maximum_sum_submatrix(matrix, R, C))