
def dnfsort(arr, n):
	l = -1
	r = n 
	mid = 0

	while mid < r :
		if arr[mid] == 0:
			arr[mid], arr[l+1] = arr[l+1], arr[mid]
			l += 1

		elif arr[mid] == 2 :
			arr[mid], arr[r-1] = arr[r-1], arr[mid]
			r -= 1
			continue

		mid += 1

arr = [int(x) for x in input().split()]
dnfsort(arr, len(arr))
print(arr)
