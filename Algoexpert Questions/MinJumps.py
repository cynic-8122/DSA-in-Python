
def minjumps(arr, i):
	if i >= len(arr) - 1:
		return 0

	t = arr[i]

	ans = float('inf')

	for j in range(1, t+1):
		tempans = 1 + minjumps(arr, i + j)
		ans = min(ans, tempans)

	return ans 

arr = [int(x) for x in input().split()]

print(minjumps(arr, 0))