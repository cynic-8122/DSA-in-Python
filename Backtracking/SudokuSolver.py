import sys
import copy

#sys.setrecursionlimit(20)
def Sudoku(matrix, ansarr):
	i = 0
	j = 0
	print(SudokuSolver(matrix, ansarr))

	return ansarr

def Choices(matrix, i, j, val):
	#vertical search
	for k in range(9):
		t = matrix[k][j]
		if t == val:
			return False
			

	#horizontalsearch
	for l in range(9):
		t = matrix[i][l]
		if t == val:
			return False

	#searching in the submatrix
	if i <= 2:
		if j <=2:
			for i in range(3):
				for j in range(3):
					t = matrix[i][j]
					if t == val:
						return False

		elif j <=5:
			for i in range(3):
				for j in range(3, 6):
					t = matrix[i][j]
					if t == val:
						return False


		else:
			for i in range(3):
				for j in range(6, 9):
					t = matrix[i][j]
					if t == val:
						return False


	elif i <= 5:
		if j <=2 :
			for i in range(3, 6):
				for j in range(3):
					t = matrix[i][j]
					if t == val:
						return False


		elif j <= 5:
			for i in range(3, 6):
				for j in range(3, 6):
					t = matrix[i][j]
					if t == val:
						return False


		else:
			for i in range(3, 6):
				for j in range(6, 9):
					t = matrix[i][j]
					if t == val:
						return False


	else:
		if j <= 2:
			for i in range(6, 9):
				for j in range(3):
					t = matrix[i][j]
					if t == val:
						return False

		elif j <= 5:
			for i in range(6, 9):
				for j in range(3, 6):
					t = matrix[i][j]
					if t == val:
						return False

		else:
			for i in range(6, 9):
				for j in range(6, 9):
					t = matrix[i][j]
					if t == val:
						return False

	return True

def SudokuSolver(matrix, ansarr, i=0, j=0):
	
	if i > 8 :
		if matrix[8][8]:
			#print(matrix)			
			t = copy.deepcopy(matrix)
			ansarr.append(t)
			return True

		else:
			return False


	ele = matrix[i][j]
	if ele:
		a = j+1
		b = i+(a//9)
		a = a%9
		check = SudokuSolver(matrix, ansarr, b, a)
		if check == True:
			return True

	else:
		for x in range(1, 10):
			if Choices(matrix, i, j, x):
				matrix[i][j] = x 
				'''
				print(f"at i = {i}, j = {j} , value = {matrix[i][j]}")
				print(matrix)
				print('__________________')
				'''
				a = j+1
				b = i+(a//9)
				a = a%9
				check = SudokuSolver(matrix, ansarr, b, a)

				if check == True:
					return True

				else:
					matrix[i][j] = 0 

	
	return False


matrix = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1 ],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]]

print(Sudoku(matrix, []))

			
				




	
	
			


