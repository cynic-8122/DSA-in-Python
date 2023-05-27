
def combinationsum(arr, ansarr, i, target, temparr):
	if target == 0:
		t = list(temparr)
		ansarr.append(t)
		return

	for j in range(i, len(arr)):
		if j > i and arr[j] == arr[j-1]:
			continue

		if arr[j] > target:
			break

		temparr.append(arr[j])
		combinationsum(arr, ansarr, j+1, target-arr[j], temparr)
		temparr.pop()
		#combinationsum(arr, ansarr, j+1, target, temparr)


ansarr =[]
temparr = []
arr = [int(x) for x in input().split()]
arr.sort()
target = int(input())
combinationsum(arr, ansarr, 0, target, temparr)
print(ansarr)
