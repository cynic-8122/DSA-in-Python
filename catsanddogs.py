T = int(input())

i = 1
while i <= T:
	C, D, L = input().split(" ")
	C = int(C)
	D = int(D)
	L = int(L)

	if C > 2*D :
		if 4*(C + D) >= L and L >= 4*(C - D) and L % 4 == 0 :
			print("yes")

	elif 4*(C + D) >= L and L >= 4*(D) and L % 4 == 0 :
		print("yes")

	else :
		print("no")


	i += 1







