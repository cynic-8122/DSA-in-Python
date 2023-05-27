T = int(input())

i = 1
while i <= T:
	N = int(input())
	arr = list(map(int, input().split()))
	X1 = int()
	X2 = int()
	X3 = int()

	arrd = []
	m = 0
	while m < len(arr) :
		n = m 
		X1 = arr[m]
		while n < len(arr) :
			o = n 
			X2 = arr[n]
			while o < len(arr) :
				X3 = arr[o]

				a = (abs(X1 - X2) + abs(X2 - X3) + abs(X3 - X1))
				arrd.append(a)
				o += 1

			n += 1

		m += 1
	b = max(arrd)
	print(b)
	i += 1

	
		




