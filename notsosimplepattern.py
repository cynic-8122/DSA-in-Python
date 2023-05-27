N = int(input())

row = 1
i = 1
while row <= N :
	i = row

	while i <= (2*row-1) :
		print(i , end = " ")
		i += 1

	while (i - 2) >= row :
		print ((i -2), end = " ")
		i -= 1

	print ("")
	row += 1



