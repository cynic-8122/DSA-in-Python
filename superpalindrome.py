L = input()
R = input()
arr = []

count = 0
for i in range(int(L), (int(R) + 1)) :
	i = str(i)
	x = ""

	for j in range((len(i) - 1), -1, -1) :
		x += i[j]

	if i == x :
		i = int(i)
		x = int(x)
		arr.append(i)
		
		for k in range(len(arr)) :
			y = arr[k]
			if y**2 == i :
				print(i)
				count += 1

print(arr)
print(count)
