def combinationsum(arr, k, sumsofar = 0, temparr = []):
	if sumsofar > k :
		return

	if sumsofar == k:
		print('sumsofar', sumsofar)
		print(temparr)
		return

	if len(arr) == 0 :
		return

	count = k//arr[0]

	for i in range(count):
		temparr.append(arr[0])
		combinationsum(arr, k, sumsofar + arr[0], temparr)

		sumsofar -= temparr[-1]
		temparr.pop()
		combinationsum(arr[1:], k, sumsofar, temparr)

arr = [int(x) for x in input().split()]

k = int(input())

combinationsum(arr, k)