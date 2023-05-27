a = int(input())

def root(a, left, right) :
	for i in range(left, (right + 1)) :
		mid = (left + right) // 2
		if (mid)**2 == a :
			return mid
			break
		elif (mid)**2 > a :
			right = mid - 1

		else :
			left = mid + 1

	return mid

print(root(a, 1, (a + 1)//2))

