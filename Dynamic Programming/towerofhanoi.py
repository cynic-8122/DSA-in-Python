def towerofhanoi(n, a, b, c):
	
	
	ctop = float('inf') if len(c) == 0 else c[-1]

	if n == 1 and a[0] < ctop :
		c.append(a.pop())
		return

	
	lastelement = a[-1] if len(a) else None
	a = a[:len(a) - 1]
	towerofhanoi(n - 1, a, c, b)
	towerofhanoi(1, [lastelement], b, c)
	print(f"a = {a}, \nb = {b}, \nc = {c}")
	towerofhanoi(n -1, b, a, c)

n = int(input())

a = [i for i in range(1, n+1)]
towerofhanoi(n, a, [], [])
