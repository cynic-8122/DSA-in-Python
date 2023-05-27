def multiply(a, b):
	if a == 0 or b == 0:
		return 0

	return a + multiply(a, b-1)

a, b = [int(x) for x in input().split()]
print(multiply(a, b))