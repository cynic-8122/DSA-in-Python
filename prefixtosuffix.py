prefix_arr = [int(x) for x in input().split()]

def prefixToSuffix(prefixSumArray):
	c = prefixSumArray[0]
	Arr = [0]*len(prefixSumArray)
	Arr[0] = c
	print(prefixSumArray)
	for i in range(1, len(prefixSumArray)):
		#print(prefix_arr[i - 1])
		#print(i)
		Arr[i] = prefixSumArray[i] - prefixSumArray[i - 1]
        
	suffix_arr = [0]*len(prefixSumArray)
	sum_so_far = 0
	for i in range(1, len(Arr) + 1):
		sum_so_far += Arr[-i]
		suffix_arr[i - 1] = sum_so_far
	print(Arr)
        
	return suffix_arr

print(prefixToSuffix(prefix_arr))