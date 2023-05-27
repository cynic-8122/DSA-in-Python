N = 6
H = 5
Y1 = 1
Y2 = 2
L = 3
a = 0


j = 1

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

print(a)