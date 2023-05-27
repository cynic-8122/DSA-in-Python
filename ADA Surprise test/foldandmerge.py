def foldandmerge(arr, n):
	i = 0
	j = n - 1

	temparr = []

	while i < j:
		temp = arr[i]*arr[j]
		temparr.append(temp)
		i += 1
		j -= 1

	print(temparr)


arr = [int(x) for x in input().split()]
foldandmerge(arr, len(arr))
