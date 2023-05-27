
def CountNumberofWays(n):
	if n < 1 :
		return 0

	if n == 1 or n == 2 :
		return n 

	numberofways = CountNumberofWays(n-1) + CountNumberofWays(n-2) + CountNumberofWays(n-3)
	return numberofways

n = int(input())
print(CountNumberofWays(n))