arr = [[1, 1 , 1 , 0 , 0 , 0],
	[0 ,1, 0, 0, 0, 0],
	[1 ,1, 1, 0, 0, 0],
	[0 ,0, 2, 4, 4, 0],
	[0 ,0, 0, 2, 0, 0],
	[0 ,0, 1, 2, 4, 0]]

def template_arr(temp) :
	output = 0
	for i in range(3):
		for j in range(3) :
			output += temp[i][j]
			if i == 1 :
				if j == 0 or j == 2 :
					output -= temp[i][j]
    
	return output 

def hourglassSum(arr):
	ans = float('-inf')
	i = 0
	while i <= 3 :
		j = 0
		while j <= 3 :
			temp = []
			temp.append(arr[i][j:(j + 3)])
			temp.append(arr[i + 1][j:(j + 3)])
			temp.append(arr[i + 2][j :(j + 3)])
			ans = max(ans, template_arr(temp))
			#print(temp)
			j += 1
		i += 1

	return ans

print(hourglassSum(arr))