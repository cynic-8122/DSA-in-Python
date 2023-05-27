def bubblesort(arr) :
	
	swaps = 0
	for i  in range(1, (len(arr))) :
		swapped = True	
		for j in range(0, (len(arr) - i)) :
			i = j + 1
			if arr[i] < arr[j] :
				arr[i], arr[j] = arr[j], arr[i]
				swaps += 1
				swapped = False
		
		if swapped :
			break
	print(arr)
	return swaps


T = int(input())
for i in range(T) :
	N = int(input())
	arr = list(map(int, input().split()))
	x = bubblesort(arr)
	print(x)



