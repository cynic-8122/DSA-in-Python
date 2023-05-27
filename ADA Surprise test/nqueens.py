
n = int(input())
arr = [[0 for i in range(n)] for i in range(n)]

def nqueens(n, arr, i = 0):
	if i >= n:
		print(arr)
		return 

	for j in range(n):
		if check(arr, i, j):
			arr[i][j] = "Q"
			nqueens(n, arr, i+1)
			arr[i][j] = 0


	return

def check(arr, i, j):
	for a in range(i):
		for b in range(len(arr)):
			if arr[a][b] == 'Q':
				if b == j:
					return False

				if abs(a-i) == abs(b-j):
					return False

	return True

nqueens(n, arr)



	
