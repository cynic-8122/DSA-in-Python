
def lengthofLIS(arr, dp, comparewith = -float('inf')):
	if len(arr) == 0:
		return 0

	currentelement = arr[0]
	ans1 = -float('inf')
	if currentelement > comparewith :
		ans1 = 1 + lengthofLIS(arr[1:], dp, currentelement)

	ans2 = lengthofLIS(arr[1:], dp, comparewith)

	return max(ans1, ans2)

arr = [int(x) for x in input().split()]
dp = [-1 for i in range(len(arr))]

print(lengthofLIS(arr))

	