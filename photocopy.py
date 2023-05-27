N = int(input("No of copies required "))

x = int(input())
y = int(input())

def good(N, x, y, mid) :
	if ((mid - min(x, y))/max(x, y)) + ((mid)/min(x, y)) >= N :
		return True

	else :
		return False

def min_time(N, left, right) :
	ans = 0
	for i in range(left, right + 1) :
		mid = (left + right) // 2
		if good(N, x, y, mid) :
			ans = mid
			right = mid - 1
		else :
			left = mid + 1

	return ans

print(min_time(N, 0, (N*min(x, y))))

