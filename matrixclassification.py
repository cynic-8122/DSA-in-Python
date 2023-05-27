def trace(arr, N) :
	sum_of_diagonal_elements = 0
	for i in range(N):
		sum_of_diagonal_elements += arr[i][i]

	return sum_of_diagonal_elements

def transpose(arr, N) :
	for i in range(N) :
		j = i + 1
		while j < N :
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
			j += 1

	return arr
T = int(input())

for o in range(T) :
	
	sum_of_matrix = 0
	arr = []
	x = list(arr)
	N = int(input())
	check = 0
	for m in range(N) :
	
		darr = [int(x) for x in input().split()]
		sum_of_matrix += sum(darr)
		arr.append(darr)
		if sum(darr[(m + 1):]) == 0 and (m + 1) < N :
			check += 1
	
	tarr = transpose(arr, N)
	print("Symmetric check", tarr == x)
	if sum_of_matrix == trace(arr, N) :
		print(7)
		# means matrix is diagonal i.e. symmertic and triangular too

	if check != (N - 1) :# matrix is not lower triangular
		check2 = True
		for j in range(N) :
			temp = list(tarr[j])
			if ((j+1) < N and sum(temp[(j+1):]) != 0) :
				check2 = False
				break
		print(f"check = {check}, check2 = {check2}")
		# if check is True or (N - 1) -> Matrix is triangular

	elif (x == tarr) :
		if (check2 == True or check == (N - 1)):
			print(3)
		# means martix is symmetric, triangular and not diagonal
		else :
			print(1) # matrix is only symmetric

	else :
		if (check2 == True or check == (N - 1)):
			print(2)
		# means matrix is only triangular
		else :
			print(0) # matrix is neither...
	






