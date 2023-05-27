def combinationsum(arr, k, ansarr, temparr = []):
	if k < 0:
		return

	if k == 0:
		print(temparr)
		return

	if len(arr) == 0 :
		return

	if arr[0] <= k :
		temparr.append(arr[0])
		combinationsum(arr, k - arr[0], ansarr, temparr)
		temparr.pop()


	combinationsum(arr[1:], k, ansarr, temparr)

def Helperfunction(arr, k):
	ansarr = []
	combinationsum(arr, k, ansarr)
	return ansarr

arr = [int(x) for x in input().split()]

k = int(input())

combinationsum(arr, k, [])