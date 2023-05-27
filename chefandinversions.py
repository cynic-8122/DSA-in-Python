T = int(input())
for i in range(T) :
	N = int(input())
	arr = list(map(int, input().split()))
	count = 0
	for j in range(0, (len(arr) - 1)) :
		k = j + 1
		while k < len(arr) :
			
			if arr[k] < arr[j] :				
				count += 1
				
			k += 1

	print(count)



