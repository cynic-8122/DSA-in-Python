def printonly1subsequencewithsumk(arr, k, sumsofar = 0, temparr = []):
	if sumsofar == k :
		print(temparr)
		return True

	if len(arr) == 0 :
		return False

	if sumsofar > k :
		return False

	temparr.append(arr[0])
	t1 = printonly1subsequencewithsumk(arr[1:], k, sumsofar + arr[0], temparr)

	if t1 :
		return True

	temparr.pop()

	t2 = printonly1subsequencewithsumk(arr[1:], k, sumsofar, temparr)

	if t2 :
		return True

arr = [int(x) for x in input().split()]

k = int(input())

printonly1subsequencewithsumk(arr, k)
