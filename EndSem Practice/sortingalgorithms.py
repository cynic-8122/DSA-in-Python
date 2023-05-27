'''
Bubble sort (Count number of comparisons for a bubble sort)
Insertion sort
Selection sort
Merge sort
Quick Sort
'''


def merge(arr1, arr2):
	arr = []
	i = 0
	j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			arr.append(arr1[i])
			i += 1

		else:
			arr.append(arr2[j])
			j += 1

	while i < len(arr1):
		arr.append(arr1[i])
		i += 1

	while j < len(arr2):
		arr.append(arr2[j])
		j += 1

	return arr

def mergesort(arr, left, right):
	if left > right :
		return

	mid = (left + right)//2

	if left == right :
		return [arr[mid]]

	X = mergesort(arr, left, mid)
	Y = mergesort(arr, mid+1, right)

	return merge(X, Y)

arr = [int(x) for x in input().split()]
print(mergesort(arr, 0, len(arr) - 1))

'''
def insertvalue(arr, value, sortedarrlength):
	for i in range(sortedarrlength):
		if arr[i] >= value :
			arr.insert(i, value)
			break

def insertionsort(arr):
	sortedarrlength = 1
	i = 1
	while i < len(arr):
		value = arr[i]
		arr.pop(i)
		insertvalue(arr, value, sortedarrlength)
		sortedarrlength += 1
		i += 1

	return arr

arr = [int(x) for x in input().split()]
print(insertionsort(arr))
'''
'''
def getminelement(arr, sortedarraylength):
	minelement = float('inf')
	idx = None
	for i in range(sortedarraylength, len(arr)) :
		if arr[i] < minelement :
			minelement = arr[i]
			idx = i 
	return idx

def selectionsort(arr):
	#pick the minimum element from the unsorted subarray and place it in the the sorted part of the subarray
	sortedarraylength = 0
	for i in range(len(arr)):
		minelementidx = getminelement(arr, sortedarraylength)
		arr[sortedarraylength], arr[minelementidx] = arr[minelementidx], arr[sortedarraylength]
		sortedarraylength += 1

	return arr 

arr = [int(x) for x in input().split()]
print(selectionsort(arr))
'''
'''
def bubblesort(arr):
	totalswaps = 0
	totalnumberofcomparisons = 0
	for i in range(len(arr)):
		numberofswaps = 0
		for j in range(i+1, len(arr)):
			totalnumberofcomparisons += 1
			if arr[i] > arr[j]:
				arr[i], arr[j] = arr[j], arr[i]
				numberofswaps += 1

			else :
				break

		totalswaps += numberofswaps
		
	print("Total Number of Swaps =", totalswaps)
	print("Total Number of Comparisons =", totalnumberofcomparisons)
	return arr

arr = [int(x) for x in input().split()]
print(bubblesort(arr))
'''

import random

def quicksort(arr, left, right):
	if left >= right :
		return

	pivotindex = random.randrange(left, right)

	pivotvalue = arr[pivotindex]
	count = 0
	for i in range(left, right + 1):
		if arr[i] < pivotvalue :
			count += 1

	swapindex = left + count
	arr[pivotindex], arr[swapindex] = arr[swapindex], arr[pivotindex]

	i = left
	j = swapindex + 1

	while i < swapindex and j <= right :
		if arr[i] < pivotvalue :
			i += 1

		if arr[j] >= pivotvalue :
			j += 1

		if arr[i] >= pivotvalue and arr[j] < pivotvalue :
			arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j += 1

	quicksort(arr, left, swapindex - 1)
	quicksort(arr, swapindex + 1, right)


arr = [int(x) for x in input().split()]
quicksort(arr, 0, len(arr) - 1)
print(arr)

def linearsearch(arr, value):
	for i in range(len(arr)) :
		if arr[i] == value :
			return i

	return -1 

def binarysearch(arr, value):
	#Array must be sorted for binary search to work properly
	arr.sort()

	i = 0
	j = len(arr) - 1
	while i <= j:
		mid = (i + j)//2
		if arr[mid] == value :
			return mid

		elif arr[mid] > value :
			j = mid - 1

		else :
			i = mid + 1

	return -1

arr2 = [int(x) for x in input("Second Array for Binary Search \n").split()]
arr1 = [int(x) for x in input("First Array for Linear Search \n").split()]
value = int(input("Enter the value you want to search in the Array"))

print(linearsearch(arr1, value))
print(binarysearch(arr2, value))