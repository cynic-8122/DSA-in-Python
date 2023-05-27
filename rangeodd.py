L, R = input().split(" ")
L = int(L)
R = int(R)

if L > R :

	if R%2 != 0 :
		a = R 

	else :
		a = R + 1

	while a <= L :
		print(a, end = " ")
		a += 2

else :
	
	 if L% 2 != 0 :
	 	a = L

	 else :
	 	a = L + 1

	 while a <= R :
	 	print(a, end = " ")
	 	a += 2
	 	

