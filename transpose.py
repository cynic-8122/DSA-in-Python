def transpose(arr, N) :
	for i in range(N) :
		j = i + 1
		while j < N :
			arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
			j += 1

	return arr

for i in range(T) :
	sum_of_matrix = 0
	arr = []
	x = list(arr)
	N = int(input())
	check = 0
	for j in range(N) :
		darr = [int(x) for x in input().split()]
		
		


	tarr = transpose(arr, len(arr))