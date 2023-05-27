T = int(input())

for i in range(T) :
	C = int(input())
	a = 2
	while True :
		if C // a == 0 :
			break

		else :
			a *= 2

	arr = []
	for j  in reversed(range(((C // 2) + 1), (a - 1))) :
		A = j
		B = C^A
		if B < a :
			product = A*B
			arr.append(product)

	print(max(arr))






