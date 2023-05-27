T = int(input())
for i in range(T) :
	S = input()
	count = 0
	a = 0
	for j in range(len(S)) :
		b = int(S[j])
		if a^b :
			if a == 0 :
				count += 1

			a = b

	print(count)

	

	