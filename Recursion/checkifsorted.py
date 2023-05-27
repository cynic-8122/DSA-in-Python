def check_sorted(arr, i ):
	if i == 1 :
		return True

	x = check_sorted(arr, i-1)
	
	if x and (arr[i - 1] >= arr[i - 2]):
		return True

	else :
		return False

arr = [int(x) for x in input().split()]
print(check_sorted(arr, len(arr)))

