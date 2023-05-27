
'''
Already submitted the memoization solution codestudio.
This will be a tabulation solution.
'''

def SubsetSumEqualToK(arr, k):
	n = len(arr)
	#dp = [[-1 for i in range(k+1)] for i in range(n)]
	''' 
	for space optimization just start with a prev array and current array of size (k+1) each
	'''
	prev = [-1 for i in range(k+1)]
	current = [-1 for i in range(k+1)]


	i = 0
	for j in range(k+1):
		if j == 0:
			prev[j] = True

		elif arr[i] == j:
			prev[j] = True

		else:
			prev[j] = False

	if prev[k] == True:
		return True

	i += 1
	while i < n:
		for j in range(k+1):
			target = j
			if target == 0:
				current[j] = True

			#either the current element can be selected only and only if it's less than or equal to target 
			elif arr[i] <= target and prev[target-arr[i]]:
				current[j] = True

			#the current element can not be selected
			elif prev[target]:
				current[j] = True

			else:
				current[j] = False

		if current[k] == True:
			return True

		prev = list(current)
		i += 1

	return False


arr = [int(x) for x in input().split()]
k = int(input())

print(SubsetSumEqualToK(arr, k))






