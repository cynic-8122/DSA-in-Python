'''
Longest Subarray with atmost k distinct elements
'''

arr = [int(x) for x in input().split()]
K = int(input())

def function(arr, n, K):
	#Find the maximum reach possible starting from the first index
	i = 0
	j = 1
	count = 1
	Hashmap = {arr[0]:1}
	ans = 0
	while j < n:
		Hashmap[arr[j]] = Hashmap.get(arr[j], 0) + 1
		if Hashmap[arr[j]] == 1:
			count += 1

		if count > K:
			break

		j += 1

	# This loop could've ended due to break condition or j has exceed the value of n

	if j >= n:
		# This implies that I've traveresed the entire array without violating the condition 
		# hence entire array is the answer
		return n 

	else:
		# j-1 is the bound for the starting index 0
		Hashmap[arr[j]] -= 1
		if Hashmap[arr[j]] == 0:
			count -= 1

		ans = max(ans, j - i)

	Hashmap[arr[i]] -= 1
	if Hashmap[arr[i]] == 0:
		count -= 1

	i += 1
	
	while i < n:
		while j < n:
			Hashmap[arr[j]] = Hashmap.get(arr[j], 0) + 1
			if Hashmap[arr[j]] == 1:
				count += 1

			if count > K:
				break

			j += 1

		if j >= n:
			return max(ans, j - i)

		else:
			Hashmap[arr[j]] -= 1
			if Hashmap[arr[j]] == 0:
				count -= 1

			ans = max(ans, j-i)

		Hashmap[arr[i]] -= 1
		if Hashmap[arr[i]] == 0:
			count -= 1

		i += 1

	return ans






	

print(function(arr, len(arr), K))
