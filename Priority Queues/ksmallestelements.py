import heapq

arr = [int(x) for x in input().split()]
k = int(input("Enter the value of k \n"))
temparr = arr[:k]
heapq._heapify_max(temparr)

for i in range(k, len(arr)):
	print(i)
	if arr[i] < temparr[0]:
		heapq._heapreplace_max(temparr, arr[i])

print(*temparr)