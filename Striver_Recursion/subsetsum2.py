
def subset(arr, temparr, ansarr, i = 0):
	t = list(temparr)
	ansarr.append(t)

	if i >= len(arr):
		return

	for j in range(i, len(arr)):
		if j > i and arr[j - 1] == arr[j]:
			continue

		else:
			temparr.append(arr[j])
			subset(arr, temparr, ansarr, j+1)
			temparr.pop()

ansarr = []
arr = [int(x) for x in input().split()]
arr.sort()
temparr = []

subset(arr, temparr, ansarr)

print(ansarr)

