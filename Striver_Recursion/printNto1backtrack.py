def printNto1(n, i = 1):
	if i > n:
		return

	printNto1(n, i+1)

	print(i)

N = int(input())
printNto1(N)