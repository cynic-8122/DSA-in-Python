def subset(arr, i, n) :
	if i == n :
		print(arr)
		return arr

	x = subset(arr, i + 1, n)
	for m in range(len(arr)) :
		y = x
		y.remove(arr[i])
		print(y)

	



