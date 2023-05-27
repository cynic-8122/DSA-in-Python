
arr = [int(x) for x in input().split()]

k = int(input())

def check(arr, k, mid):
	count = 1
	temp = 0
	prevans = 0
	for i in range(len(arr)):
		temp += arr[i]
		if temp > mid :
			temp = arr[i]
			count += 1

		prevans = max(prevans, temp)

	if count <= k :
		return prevans

	return False


def bookallocation(arr, k):
	l = min(arr)
	r = sum(arr) - l 
	ans = r 

	while l <= r :
		mid = (l + r)//2
		tempans = check(arr, k, mid)
		if tempans :
			ans = min(ans, tempans)
			r = mid - 1
			continue

		else :
			l = mid + 1
			continue

	return ans 

print(bookallocation(arr, k))
