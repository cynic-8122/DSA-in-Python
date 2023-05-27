T = int(input())

for i in range(T) :
	check1 = True
	n = int(input())
	arr1 = [int(x) for x in input().split()]
	arr2 = [int(y) for y in input().split()]
	a = sorted(arr1)
	b = sorted(arr2)

	if a == b :
		print(n)
		check1 = False
		
	else :
		for i in range((n - 1), 0 , -1) :
			check = False
			if check :
				break
			x = n - i
			j = 0
			while j < len(arr2) and (j + i) <= len(arr1) :
				darr1 = sorted(arr1[j:(j + i + 1)])
				darr2 = sorted(arr2[j:(j + i + 1)])
				if darr1 == darr2 :
					print(i)
					check = True 
					check1 = False
					break

				else :
					j += x


		if check1 :
			print(0)




