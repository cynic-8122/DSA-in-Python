from itertools import permutations

T = int(input())

for i in range(T) :
	N, M = [int(x) for x in input().split()]
	upperlimit = (1<<(M))
	arr = []
	for i in range(upperlimit) :
		arr.append(i)
	print(arr)
	perm = permutations(arr, N) 
	count = 0
	for i in list(perm) :
		a = i
		print(i) 
		itr = i[0]
		for j in range(1, N) :
			itr = (itr)&(i[j])
		if itr == 0 :
			count += 1
	print(count)

