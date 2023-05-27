def minsteps(n):
	if n < 1 :
		return -1

	if n == 1 :
		return 0

	ans1 = float('inf')
	if n%3 == 0 :
		ans1 = 1 + minsteps(n//3)

	ans2 = float('inf')
	if n%2 == 0 :
		ans2 = 1 + minsteps(n//2)

	ans3 = 1 + minsteps(n-1)

	return min(ans1, ans2, ans3)


n = int(input())

print(minsteps(n))