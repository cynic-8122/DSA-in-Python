T = int(input())

for i in range(T) :
	N = int(input())
	arr1 = [int(x) for x in input().split()]
	arr2 = [int(x) for x in input().split()]
	for i in range(N) :
		for j in range(i, N):
			A_x = arr1[i]
			A_y = arr2[i]
			B_x = arr1[j]
			B_y = arr2[j]
			