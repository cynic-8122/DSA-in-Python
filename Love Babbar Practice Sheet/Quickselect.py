import random
import sys
sys.setrecursionlimit(50)

def quickselect(arr, l, r, k):
	print(f"l = {l}, r = {r}, k = {k}")
	print("before partition", arr)

	pivot = r

	pivotidx = partition(arr, l, r, pivot)
	print(f"pivotidx = {pivotidx}")
	print(arr)
	

	if pivotidx == k:
		return arr[pivotidx]

	elif pivotidx > k:
		return quickselect(arr, l, pivotidx-1, k)

	else:
		return quickselect(arr, pivotidx+1, r, k)


def partition(arr, l, r, pivotidx):
	count = 0
	for i in range(l, r+1):
		if arr[i] < arr[pivotidx]:
			count +=1

	newpivotidx = l+count

	arr[pivotidx], arr[newpivotidx] = arr[newpivotidx], arr[pivotidx]
	i = l
	j = r 

	while i < newpivotidx and j > newpivotidx :
		if arr[i] < arr[newpivotidx]:
			i += 1

		if arr[j] >= arr[newpivotidx]:
			j -= 1

		if arr[i] >= arr[newpivotidx] and arr[j] < arr[newpivotidx]:
			arr[i], arr[j] = arr[j], arr[i]

	return newpivotidx


arr = [int(x) for x in input().split()]
k = int(input())

ans = quickselect(arr, 0, len(arr)-1, k-1)
ans2 = quickselect(arr, 0, len(arr)-1, len(arr)-k)
print(f"{k}th smallest element in the array is {ans}")
print(f"{k}th largest element in the array is {ans2}")


