def subsequenceswithsumk(arr, k, sumsofar = 0, temparr = []):
	if sumsofar == k :
		print(temparr)
		return
		
	if len(arr) == 0:
		return

	if sumsofar > k :
		return

	temparr.append(arr[0])
	subsequenceswithsumk(arr[1:], k, sumsofar + arr[0], temparr)
	temparr.pop()
	subsequenceswithsumk(arr[1:], k, sumsofar, temparr)

arr = [int(x) for x in input().split()]

k = int(input())

subsequenceswithsumk(arr, k)
