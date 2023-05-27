def hanoi(n, a, b, c):
	if n == 1:
		x = a.pop()
		c.append(x)
		print(f"a = {a}, b = {b}, c = {c}")
		return

	else :
		hanoi(n - 1, a, c, b)
	
	x = a.pop()
	c.append(x)
	print(f"a = {a}, b = {b}, c = {c}")	

	hanoi(n - 1, b, a, c)
	print(f"a = {a}, b = {b}, c = {c}")

N = int(input())
a = []
b = []
c = []

for i in reversed(range(1, N + 1)) :
	a.append(i)

hanoi(N, a, b, c)












