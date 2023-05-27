T = int(input())
a = 1

while a <= T :

	N  = input()

	V = len(N)
	i =1
	SUM = 0


	while i <= V :
		j = N[(i - 1)]
		j = int(j)
		SUM += j
		i += 1

	print(SUM)

	a += 1






