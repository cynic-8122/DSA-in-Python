A = int(input())

B = int(input())

i = A
while i > 0 :
	if i % B == 0 :
		print(i)
		break

	else :
		i -= 1

