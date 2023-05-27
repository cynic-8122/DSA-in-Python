T = int(input())

for i in range(T):
	N, K, S = [int(x) for x in input().split()]
	arr = [int(x) for x in input().split()]

	max_len_so_far = 0

	for i in range(N):
		if (N - i) <  max_len_so_far :
			#print("EXIT1")
			#print(i)
			break
		sum_so_far = 0
		j = i 
		splits = 0
		while splits < K and j < N:
			sum_so_far += arr[j]
			if sum_so_far > S:
				sum_so_far = 0
				splits += 1
				continue 
			j += 1

		j = min(j, (N - 1))
		#print(max_len_so_far)
		max_len_so_far = max(max_len_so_far, (j - i))

	print(max_len_so_far)





