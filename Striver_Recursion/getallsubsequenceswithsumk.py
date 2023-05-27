def allsubsequenceswithsumk(arr, k, ansarr, sumsofar = 0, temparr = []):
	if sumsofar == k:
		return temparr

	if len(arr) == 0:
		return False

	if sumsofar > k :
		return False

	temparr.append(arr[0])
	t1 = allsubsequenceswithsumk(arr[1:], k, ansarr, sumsofar + arr[0], temparr)
	if t1 :
		

	temparr.pop()
	t2 = allsubsequenceswithsumk(arr[1:], k, ansarr, sumsofar, temparr)
	if t2 :
		print(t2)

def HelperFunction(temparr, ansarr):
	ansarr.append(temparr)
	return ansarr


arr = [int(x) for x in input().split()]

k = int(input())

ansarr = []
print(allsubsequenceswithsumk(arr, k, ansarr))

