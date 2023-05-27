
def Triangle(arr, i, j):
	if i == 1 :
		return arr[0][0]

	
	if i == len(arr):
		ans = float('inf')
		for j in range(i, 0, -1):
			temp1ij = float('inf') if j-1 < 1 else (Triangle(arr, i-1,j-1))
			temp2ij = float('inf') if j > i - 1 else (Triangle(arr, i-1, j))
			ansij = min(temp1ij, temp2ij) + arr[i-1][j-1]
			ans = min(ans, ansij) 
			#print(f"At i = {i}, j = {j}, ANS = {ans}")

		return ans

	else:
		temp1ij = float('inf') if j-1 < 1 else (Triangle(arr, i-1,j-1))
		temp2ij = float('inf') if j > i-1 else (Triangle(arr, i-1, j))
		#print(f"At i = {i}, j = {j}, ANS = {min(temp1ij, temp2ij) + arr[i-1][j-1]}")
		return min(temp1ij, temp2ij) + arr[i-1][j-1]


n = int(input())
matrix = []
for i in range(n):
	row = [int(x) for x in input().split()]
	matrix.append(row)

print(Triangle(matrix, n, n))



	