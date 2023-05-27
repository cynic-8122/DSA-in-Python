import math
def Helper(n):
	if n == 0:
		return 0

	if n%9 == 0:
		return 9

	else:
		return (n%9)

T = int(input())

for i in range(T):
	N = int(input())

	M = 1<<(N)
	print(Helper(M))

