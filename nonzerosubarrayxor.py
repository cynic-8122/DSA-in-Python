n = int(input())
arr = []
v = 1
t = 2
i = 0
while i < n:
	if v != (1<<t)-1 :
		arr.append(v)
		v += 1
		i += 1

	else :
		v += 1
		t += 1

print(arr)
for i in range(n):

	for j in range(i+1, n):
		xor = 0
		for k in range(i, j+1):
			xor^= arr[k]

		print(xor)
		if xor == 0:
			for k in range(i, j + 1):
				print(arr[k], end = " ")
			print()	




