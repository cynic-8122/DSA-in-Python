'''
Given an array arr[] of size N. For every element in the array, 
the task is to find the index of the farthest element in the array to the right which is smaller than the 
current element. If no such number exists then print -1. 

Examples: 

Input: arr[] = {3, 1, 5, 2, 4} 
Output: 3 -1 4 -1 -1 
arr[3] is the farthest smallest element to the right of arr[0]. 
arr[4] is the farthest smallest element to the right of arr[2]. 
And for the rest of the elements, there is no smaller element to their right.

Input: arr[] = {1, 2, 3, 4, 0} 
Output: 4 4 4 4 -1
'''

def FarthestSmallerNumber(arr, n):
	suffixminarr = [0]*n
	minsofar = arr[-1]
	for i in range(n-1, -1, -1):
		minsofar = min(minsofar, arr[i])
		suffixminarr[i] = minsofar

	# Now if you look closely, this suffix min array will be sorted in non deceasing manner
	# Hence, we can apply binary search for each value in arr to find in its farthest Smaller value

	ansarr = []
	for i in range(n):
		val = arr[i]
		ans = Findans(suffixminarr, i, val)
		ansarr.append(ans)

	return ansarr

def Findans(arr, i, val):
	l = i 
	r = len(arr)-1
	ans = 0

	while l <= r:
		mid = (l+r)//2
		if arr[mid] >= val:
			r = mid-1

		else:
			ans = mid
			l = mid+1

	if ans:
		return ans

	return -1

n = int(input())

arr = [int(x) for x in input().split()]

print(*FarthestSmallerNumber(arr, n))


