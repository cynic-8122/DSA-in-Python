arr = [int(x) for x in input().split()]

def longestconsecutivesubarray(arr, n):
	ans = 0
	for i in range(n):
		Hashmap = {}
		maxval = arr[i]
		minval = arr[i]
		for j in range(i,n):
			if arr[j] in Hashmap.keys():
				break

			Hashmap[arr[j]] = 1
			minval = min(minval, arr[j])
			maxval = max(maxval, arr[j])

			if maxval - minval == j - i :
				tempans = j - i + 1
				ans = max(ans, tempans)

	return ans  

print(longestconsecutivesubarray(arr, len(arr)))


