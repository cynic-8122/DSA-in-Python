def riverSizes(matrix):
	position1 = []
	position2 = []
	count_array = []
	for i in range(len(matrix)) :
		for j in range(len(matrix[i])) :
			if matrix[i][j] == 1 :
				position1.append(i)
				position2.append(j)
	
	count = 1
	i = 0
	while i < len(position1) :
		print(f"i = {i}")
		print(f"length of position list = {len(position1)}")
		
		a = position1[i]
		b = position2[i]
		position1.pop(i)
		position2.pop(i)
		if a in position1 :
			
			x = position1.index(a)
			print(f"x = {x}")
			
			if abs(b - position2[x]) == 1 :
				count += 1
				print(f"count = {count}")
				i = x

		elif b in position2 :
			
			y = position2.index(b)
			print(f"y = {y}")
			
			if abs(a - position1[y]) == 1 :
				count += 1
				print(f"count = {count}")
				i = y
			
		else :
			print("else got executed")
			i = 0
			count_array.append(count)
			print(f"count = {count}")
	
	return count_array

matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

print(riverSizes(matrix))