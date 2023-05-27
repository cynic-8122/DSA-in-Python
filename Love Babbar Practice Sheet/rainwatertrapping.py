
arr = [int(x) for x in input().split()]

ans = 0
previousmax = arr[0]
previousmaxidx = 0
prefixarr = [0]*(len(arr))
sumsofar = 0
for i in range(len(arr)):
	sumsofar += arr[i]
	prefixarr[i] = sumsofar

for i in range(len(arr)):
	if arr[i] >= previousmax :
		dist = max(0, i - previousmaxidx - 1)
		ans += (min(previousmax, arr[i]))*(dist)
		t = prefixarr[i] - prefixarr[previousmaxidx]
		ans -= t 
		previousmaxidx = i 
		previousmax = arr[i]

print()

