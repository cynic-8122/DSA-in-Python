def xorQuery(queries):
	arr = []
	final_xor = 0
	xor_update = []
	total_values_added_so_far = 0
	i = 0
	while i < len(queries):
		j = i
		while j < len(queries):
			if queries[j][0] == 1 :
				arr.append(queries[j][1])
				j += 1
			else:
				break

		values_added = (j - i)
		total_values_added_so_far += values_added
		i = j
		if queries[i][0] == 2:
			till = total_values_added_so_far - 1
			xor = queries[i][1]
			val = [xor, till]
			if total_values_added_so_far :			
				xor_update.append(val)
				final_xor ^= xor 

		i += 1
	#print("xor_update", xor_update)
	#print("arr", arr)
	for i in range(xor_update[0][1]+1):
		arr[i] ^= final_xor


	i = 1 
	while i < len(xor_update):
		j = xor_update[i - 1][1] + 1
		final_xor ^= xor_update[i - 1][0] 
		while j <= xor_update[i][1]:
			arr[j] ^= final_xor
			j += 1

		i += 1

	return arr 

T = int(input())

for i in range(T):
	Q = int(input())
	queries = [] 
	for i in range(Q):
		xarr = [int(x) for x in input().split()]
		queries.append(xarr)

	print(xorQuery(queries))




