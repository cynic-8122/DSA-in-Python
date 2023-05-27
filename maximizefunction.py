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

		m = int(abs(arr[x] - arr[y]))
		n = int(abs(arr[y] - arr[z]))
		o = int(abs(arr[z] - arr[x]))

		a = (m + n + o)
		darr.append(a)
	maximum = max(darr)

	print(maximum)

	i += 1
	



