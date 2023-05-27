import math

def minsquares(n, minans = float('inf')):
	t = math.sqrt(n) 
	if t == int(t) :
		return 1

	t = int(t)
	for i in range(1, t + 1):
		tempans = minsquares(n - (i*i), minans)
		minans = min(minans, tempans)

	return 1 + minans

n = int(input())
print(minsquares(n))
print(math.sqrt(15))




