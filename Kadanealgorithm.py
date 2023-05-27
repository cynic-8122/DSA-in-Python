def Kadane(arr) :
	sum_so_far = 0
	max_sum = 0
	for i in range(len(arr)) :
		sum_so_far += arr[i]
		if sum_so_far < 0 :
			sum_so_far = 0
			continue
		max_sum = max(max_sum, sum_so_far)

	return max_sum

N = int(input("Length of array"))
arr = [int(x) for x in input().split()]

print(Kadane(arr))