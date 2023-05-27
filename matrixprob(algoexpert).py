def riverSizes(matrix):
	position1 = []
	position2 = []
	count_array = []
	for i in range(len(matrix)) :
		for j in range(len(matrix[i])) :
			if matrix[i][j] == 1 :
				position1.append(i)
				position2.append(j)
	i = 0
	while i < len(position1) :
		count = 1
		a = position1[i]
		b = position2[i]
		position1.pop(i)
		position2.pop(i)
		if a in position1 :
			check1 = True
			x = position1.index(a)
		elif b in position2 :
			check2 = True
			y = position2.index(b)
		if check1 or check2 :
			if abs(b - position2[x]) == 1 :
				count += 1
				i = x
			elif abs(a - position1[y]) == 1 :
				count += 1
				i = y
		else :
			i = 0
			count_array.append(count)
	
	return count_array

matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

riverSizes(matrix)