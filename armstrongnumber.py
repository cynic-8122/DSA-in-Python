N = input()

a = len(N)
i = 0
b = int(N)
SUM = 0
while i < a :
	x = (N[i])
	x = int(x)
	x = x**a
	SUM += x
	i += 1

if SUM == b :
	print("yes")

else :
	print("no")

