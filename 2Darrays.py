import random


def generate_2Darray(a, b) : # a and b represent dimensions of the matrix
	matrix = []
	for i in range(a) :
		row = []
		for j in range(b) :
			a = (i*j) #random.randrange(0, 21)
			row.append(a)
		matrix.append(row)
		

	return matrix

a = generate_2Darray(3, 4)

b = generate_2Darray(3, 4)

def print_2Darray(a) :
	for i in range(len(a)):
		print(a[i])

	return

print_2Darray(a)
print("________________________________________________")
print_2Darray(b)
print("________________________________________________")


def reshape_2Darray(m, matrix) : # m represents the no. of rows in new matrix
	reshaped_2Darray = []
	N = (len(matrix)*len(matrix[0])) // m 
	for i in range(len(matrix)) :
		if N <= len(matrix[0]) :
			a = matrix[i][:N]
			reshaped_2Darray.append(a)
			b = matrix[i][N:]
			reshaped_2Darray.append(b)
		else :
			x = N - len(matrix[0])
			

	return reshaped_2Darray

a_reshaped = reshape_2Darray(2, a)
b_reshaped = reshape_2Darray(6, b)

print_2Darray(a_reshaped)
print("________________________________________________")
print_2Darray(b_reshaped)
print("________________________________________________")





