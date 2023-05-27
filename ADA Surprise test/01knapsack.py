n = int(input())

weightarr = [int(x) for x in input().split()]
valuearr = [int(x) for x in input().split()]

k = int(input())

ans = 0

def knapsack(weightarr, valuearr, n, k, tempans = 0, i = 0):

	if k == 0:
		return tempans

	if k < 0:
		return 0

	if i >= n :
		return tempans

	ans1 = knapsack(weightarr, valuearr, n, k-weightarr[i], tempans+valuearr[i], i+1)

	ans2 = knapsack(weightarr, valuearr, n, k, tempans, i+1)

	return max(ans1, ans2)

print(knapsack(weightarr, valuearr, n, k))




