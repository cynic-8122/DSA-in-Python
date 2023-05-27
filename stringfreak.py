N = int(input())

arr = list(map(str, input().split()))

count = N

for i in range(len(arr)):
	temp_arr = []
	for j in range(len(arr[i])) :
		temp_arr.append(arr[i][j])

	start = 0
	 
	while start < (len(temp_arr) - 1) :
		if temp_arr[start] == temp_arr[start + 1] :
			temp_arr.pop(start)
			temp_arr.pop(start + 1)
			start = 0
		else :
			start += 1

	if not len(temp_arr) :
		count -= 1

print(count)





