N = int(input())

i = 1

while i <= N :
	if i % 2 != 0 :
		x = 10*((i//2)+1)
		print(x, end = " ")
		i += 1

	else :
		print((x//5), end = " ")
		i += 1



