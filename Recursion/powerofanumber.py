def power(n, p):
	if p == 0:
		return 1
	if n == 0 :
		return 0
	temp = power(n, p//2)
	if p&1 :
		return (n)*(temp)*(temp)

	else :
		return (temp)*(temp)

n = int(input())
p = int(input())
print(power(n, p))
