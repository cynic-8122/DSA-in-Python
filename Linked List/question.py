A = [float(x) for x in input().split()]

prefix_arr = []
sum_so_far = 0

for i in range(len(A)) :
	sum_so_far += A[i]
	prefix_arr.append(sum_so_far)

matrix = []
for i in range(len(A)):
	row = []
	for j in range(len(A)):
		if i <= j :
			req_sum = prefix_arr[j] - prefix_arr[i] + A[i]
			avg = req_sum/(j - i + 1)
			row.append(avg)

		else :
			row.append(0)

print(matrix)


