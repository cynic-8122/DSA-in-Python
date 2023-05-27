def spiral_traverse(arr, N, M) :
	rects = []
	x_start = 0
	y_start = 0
	x_end = M 
	y_end = N 
	row_count = 0
	column_count = 0
	
	while M > 0 and N > 0 :
		rect = []
		while x_start < x_end :
			rect.append(arr[y_start][x_start])
			print("loop 1", arr[y_start][x_start])
			x_start += 1
		row_count += 1
		x_start -= 1
		y_start += 1
		while y_start < y_end :
			rect.append(arr[y_start][x_start])
			print("loop 2", arr[y_start][x_start])
			y_start += 1
		y_start -= 1
		x_start -= 1
		column_count += 1
		while ((x_start - column_count) + 1) >= 0:
			rect.append(arr[y_start][x_start])
			print("loop 3", arr[y_start][x_start])
			x_start -= 1 

		y_start -= 1
		while (y_start - row_count) >= 0 :
			rect.append(arr[y_start][x_start])
			print("loop 4", arr[y_start][x_start])
			print("y_start", y_start)
			y_start -= 1
			print("y_start", y_start)

		x_start += 1
		y_start += 1
		print("x_start", x_start)
		x_end -= 1
		print("x_end", x_end)
		y_end -= 1
		rects.append(rect)
		#print(rect)
		M -= 2
		N -= 2

	return rects

N = int(input())
M = int(input())

mat = []
for i in range(N) :
	row = [int(x) for x in input().split()]
	mat.append(row)
print(mat)
print(spiral_traverse(mat, N, M))
