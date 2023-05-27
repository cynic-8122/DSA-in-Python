N = int(input())

row = 1
 
while row <= N :
	if row % 2 != 0 :
		a = 10*((row//2)) + 1
		i = a
		while a < i + 5 :
			print(a, end = " ")
			a += 1
		
		

	else :
		a = 5*row
		i = a
		while a > i - 5 :
			print(a, end = " ")
			a -= 1

		
	print("")
	row += 1


	