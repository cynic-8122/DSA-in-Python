
def fastpower(a, b):
	if b == 0:
		return 1

	ans = 1

	while b >= 1:
		if b&1:
			ans *= a
			b -= 1

		else:
			a *= a  
			b = b>>1

	return ans

a = int(input())
b = int(input())

print(fastpower(a, b))
