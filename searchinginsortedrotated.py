def point_of_rotation(arr) :
	left = 0
	right = len(arr)
	start = 0
	ans = None
	while left <= right :
		mid = (left + right)//2
		if arr[mid] >= arr[start]:
			if arr[mid] > arr[mid - 1] :
				if arr[mid] > arr[mid + 1] :
					ans = mid 
					break
				else :
					left = mid + 1
			else :
				right = mid - 1

		else :
			if arr[mid] < arr[mid + 1] :
				if arr[mid] < arr[mid - 1] :
					ans = mid 
					break
				else :
					right =  mid - 1
			else :
				left = mid + 1
	return ans

def bin_search(arr, ans) :
	if arr[0] >= arr[1] :
		


				
