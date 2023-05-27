N = int(input())
M = int(input())

mat = []

for i in range(N) :
	row = [int(x) for x in input().split()]
	mat.append(row)

def spiral_print(arr, N, M) :
	i_s = 0
	j_s = 0
	i_e = N
	j_e = M
	ans = ""
	row_count = 0
	column_count = 0
	count = 0
	while count < (N)*(M) :
		while i_s < i_e:
			if j_s >= j_e :
				break
			ans += str(arr[i_s][j_s])
			print(str(arr[i_s][j_s]))
			count += 1
			j_s += 1
		row_count += 1
		j_s -= 1
		i_s += 1
		while i_s < i_e :
			ans += str(arr[i_s][j_s])
			print(str(arr[i_s][j_s]))
			count += 1
			i_s += 1
		column_count += 1
		i_s -= 1
		j_e -= 1
		j_s -= 1

		while (j_s - column_count + 1) > 0:
			print(f"(j_s - column_count + 1) = {(j_s - column_count + 1)}")
			print(f'j_s = {j_s}')
			print(f"i_s = {i_s}")
			ans += str(arr[i_s][j_s])
			print(str(arr[i_s][j_s]))
			count += 1
			print(f'j_s = {j_s}')
			j_s -= 1
			print(f'j_s = {j_s}')
		i_e -= 1
		
		while (i_s - row_count) > 0:
			print(f"i_s = {i_s}")
			ans += str(arr[i_s][j_s])
			print(str(arr[i_s][j_s]))
			count += 1
			i_s -= 1

	return ans

print(spiral_print(mat, N, M))







