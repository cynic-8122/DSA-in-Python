def countsubsequenceswithsumk(arr, k, sumsofar = 0):
	if sumsofar == k :
		return 1

	if len(arr) == 0 :
		return 0

	if sumsofar > k :
		return 0

	t1 = countsubsequenceswithsumk(arr[1:], k, sumsofar + arr[0])
	t2 = countsubsequenceswithsumk(arr[1:], k, sumsofar)

	return t1 + t2


arr = [int(x) for x in input().split()]

k = int(input())

print(countsubsequenceswithsumk(arr, k))
