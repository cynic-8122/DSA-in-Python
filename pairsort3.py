N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def merge(arr1, arr2) :
	arr = []
	j = i = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] >= arr2[j] :
			arr.append(arr1[i])
			i += 1
		else :
			arr.append(arr2[j])
			j += 1

	if j >= len(arr2) :
		while i < len(arr1) :
			arr.append(arr1[i])
			i += 1

	else :
		while j < len(arr2) :
			arr.append(arr2[j])
			j += 1

	return arr 

def mergesort(arr, left, right) :
	if left == right :
		return 	[arr[left]]

	mid = (right + left) // 2
	x = mergesort(arr, left, mid)
	y = mergesort(arr, mid + 1, right)
	output = merge(x, y)
	return output
#def insertsort(arr1, arr2) :
	#count = 0
	#for i in range(1, len(arr2)) :
		#j = i - 1
		#while j >= 0 and arr2[j] < arr2[i]:			
			#arr2[j], arr2[i] = arr2[i], arr2[j]	
			#arr1[j], arr1[i] = arr1[i], arr1[j]
			#i = j			
			#j -= 1
	
	#for i in range(len(arr2)) :
		#print(arr1[i], arr2[i], end = " ")
		
	#return 

x = insertsort(A, B)








