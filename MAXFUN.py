T = int(input())

i = 1
while i <= T:
	N = int(input())
	arr = list(map(int, input().split()))
	
	darr = []
	n = len(arr)

	for x in range(0, n - 2) :
		y = x + 1
		z = x + 2
		arr[x] = X1
		arr[y] = X2
		arr[z] = X3

		a = (abs(X1 - X2) + abs(X2 - X3) + abs(X3 - X1))

		darr.append(a)
		
	maximum = max(darr)

	print(maximum)

	i += 1




