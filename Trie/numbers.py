def largestprimefactor(n):
	maxPrime = -1
	while n%2 == 0:
		maxPrime = 2
		n >>= 1

	while n%3 == 0:
		maxPrime = 3
		n = n/3

	for i in range(5, math.sqrt(n)+1, 6):
		while n%i == 0:
			maxPrime = i 
			n = n/i

		while n%(i+2) == 0:
			maxPrime = i + 2
			n = n/(i+2)


	if n > 4:
		maxPrime = n 

	return int(maxPrime)


def function(n):
	if n == 0:
		return 0

	t = largestprimefactor(n)
	return 1 + min(fuction(n-1), function(t))

