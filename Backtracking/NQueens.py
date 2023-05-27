
def check(pos, i, j):
	if len(pos) == 0:
		return True

	for x in pos:
		if x[1] == j:
			return False

		elif abs(x[0] - i) == abs(x[1] - j):
			return False

	return True

def NQueens(n):
	ansarr = [[0 for i in range(n)] for i in range(n)]

	Nqueenshelper(n, ansarr, 0, [])

def Nqueenshelper(n, ansarr, i, pos, flag = True):
	if i == n and not flag:
		print(ansarr)
		return

	elif i == n:
		return

	for j in range(n):
		#print(pos)
		if check(pos, i, j):
			ansarr[i][j] = "Q"
			pos.append([i, j])
			Nqueenshelper(n, ansarr, i+1, pos, False)
			pos.pop()
			ansarr[i][j] = 0




N = int(input())
NQueens(N)

		





