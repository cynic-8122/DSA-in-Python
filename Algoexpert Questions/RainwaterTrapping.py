def RainwaterTrapping(arr):
	previousmaxarr = []
	nextmaxarr = [0]*(len(arr))

	temp1 = -float('inf')
	temp2 = -float('inf')

	for i in range(len(arr)):
		temp1 = max(temp1, arr[i])
		previousmaxarr.append(temp1)

	for j in range(len(arr) - 1, -1, -1) :
		temp2 = max(temp2, arr[j])
		nextmaxarr[j] = temp2

	ans = 0
	for i in range(len(arr)):
		t = min(previousmaxarr[i], nextmaxarr[i])
		if t > arr[i]:
			ans += (t - arr[i])

	return ans

arr = [int(x) for x in input().split()]
print(RainwaterTrapping(arr))