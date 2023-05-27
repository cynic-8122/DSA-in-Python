N = int(input())

i = 10
while i >= 1 :
	if N % i == 0 :
		print(i)
		break

	else:
		i -= 1
