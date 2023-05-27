import time
import random

lenarr = [40, 400, 4000, 20000]

for i in range(4):
	n = lenarr[i]
	random.seed(100)
	array1 = random.sample(range(2*n + 1), n)
	array2 = random.sample(range(2*n + 1), n)
	target = n*1.5

	def mergesort(arr, i, j):
		if i > j:
			return

		if i == j:
			return [arr[i]]

		mid = (i + j)//2

		x = mergesort(arr, i, mid)
		y = mergesort(arr, mid + 1, j)

		temparr = merge(x, y)

		return temparr

	def merge(arr1, arr2):
		temparr = []
		l1 = 0
		l2 = 0

		while l1 < len(arr1) and l2 < len(arr2):
			if arr1[l1] <= arr2[l2]:
				temparr.append(arr1[l1])
				l1 += 1

			else :
				temparr.append(arr2[l2])
				l2 += 1

		while l1 < len(arr1):
			temparr.append(arr1[l1])
			l1 += 1

		while l2 < len(arr2):
			temparr.append(arr2[l2])
			l2 += 1

		return temparr

	def getactualindex(arr, startingidx, pointer):
		count = 0
		for i in range(startingidx + 1):
			if arr[i] <= arr[pointer]:
				count += 1

			else :
				break

		return count

	def insertionsort(arr):
		startingidx = 0
		while startingidx < len(arr) - 1:
			pointer = startingidx + 1
			idx = getactualindex(arr, startingidx, pointer)
			temp = pointer - 1
			while temp >= idx :
				arr[temp], arr[temp + 1] = arr[temp + 1], arr[temp]
				temp -= 1

			startingidx += 1

		return arr 

	st_insertion = time.time()
	insertionsort(array1)
	end_insertion = time.time()
	print('Time taken by insertion sort :', end_insertion - st_insertion)
	st_merge = time.time()
	mergesort(array2, 0, len(array2) - 1)
	end_merge = time.time()
	print('Time taken by merge sort :', end_merge - st_merge)

	def binarysearch(arr, l, r, target):
		while l <= r :
			mid = (l + r)//2

			if arr[mid] == target :
				print(mid)
				return 

			elif arr[mid] > target :
				r = mid - 1

			else :
				l = mid + 1

		print("This element can not be found")
		

	def linersearch(arr, target):
		for i in range(len(arr)):
			if arr[i] == target :
				print(i)
				return  

		print("This element can not be found")

			
	st_linear = time.time()
	linersearch(array1, target)
	end_linear = time.time()
	print("Time taken by linear search :", end_linear - st_linear)

	st_binary = time.time()
	binarysearch(array2,0 , len(array2)-1, target)
	end_merge = time.time()

	print("Time taken by the binary search", end_merge - st_merge)


