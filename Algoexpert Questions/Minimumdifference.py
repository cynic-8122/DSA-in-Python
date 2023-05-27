def check(arr2, t):
	l = 0
	r = len(arr2) - 1
	tempans = float('inf')
	while l <= r:
		mid = (l + r)//2
		tempans = min(tempans, abs(arr2[mid] - t))
		if arr2[mid] > t :
			r = mid - 1 

		elif arr2[mid] < t :
			l = mid + 1

		else :
			break

	return tempans
	
def minimumdifference(arr1, arr2):
	arr1.sort()
	arr2.sort()
	ans = float('inf')
	for i in range(len(arr1)):
		t = arr1[i]
		tempans = check(arr2, t)
		ans = min(ans, tempans)

	return ans 

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

print(minimumdifference(arr1, arr2))