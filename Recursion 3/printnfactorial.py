
def printfact(n, ans = 1):
	if n == 0 :
		print(ans)
		return

	printfact(n - 1, ans*n)


n = int(input())
printfact(n)