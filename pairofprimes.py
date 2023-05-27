T = int(input())
def check_if_prime(a) :
	x = a**(0.5)
	if a == 2 :
		return True
	elif (x == int(x)) :
		return False

	else :
		y = int(x)
		for i in range(2, (y + 1)):
			if (a % i == 0) :
				
				return False
				break


		return True
for j in range(T) :

	N = int(input())

	check = True
	for i in range(2, (N //2 + 1)) :
		if (check_if_prime(i) and check_if_prime((N - i))) :
			print(i , end = " ")
			print(N - i)
			check = False
			break


	if check :
		print("-1 -1")






