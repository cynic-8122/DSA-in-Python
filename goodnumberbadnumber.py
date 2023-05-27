n = int(input())

i = 2
SUM = 1 

while i**2 <= n :
	if n % i == 0 :
		a = n // i
		if a != i :
			SUM = SUM + a + i

		else :
			SUM += i



		i += 1

	else :
		i += 1


if SUM == n :
	print("YES")

else :
	print("NO")

