T = int(input())

i = 1
j = 1 


while i  <= T :
	N, H, Y1, Y2, L = input().split(" ")
	N = int(N)
	H = int(H)
	Y1 = int(Y1) 
	Y2 = int(Y2)
	L = int(L)
	a = 0
	

	while j <= N :
		t, X = input().split(" ")
		t = int(t)
		X = int(X)
		

		if t == 1 :
			if (H - Y1 <= X) :
				a += 1


			else :
				if L <= 1:
					break


				L -= 1
				a += 1

		else :
			if Y2 >= X :
				a += 1

			else :
				if L <= 1:
					break


				L -= 1
				a += 1

		
		j += 1

	j = 1
	i += 1
	print(a)





