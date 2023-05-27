def ascendnatural(n) :
	if n == 1 :
		print(1)
		return 1

	a = ascendnatural(n - 1) + 1
	print(a)

	return a
n = int(input())

def descendnatural(n) :
	if n == 1 :
		print(1)
		return
	print(n)
	descendnatural(n - 1)
	return
	



descendnatural(n)