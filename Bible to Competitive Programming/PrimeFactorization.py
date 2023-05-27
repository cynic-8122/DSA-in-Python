
n = int(input())

factors = []
exponents = []

i = 2
t = n**(1/2)
while n > 1 and i <= t:
	count = 0
	while (n%i) == 0 :
		count += 1
		n = n//i 

	if count > 0 :
		factors.append(i)
		exponents.append(count)

	i += 1

if n > 1:
	factors.append(n)
	exponents.append(1)

print(*factors)
print(*exponents)

