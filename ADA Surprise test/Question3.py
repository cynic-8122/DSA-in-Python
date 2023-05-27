'''
To sort the binary array we use a two pointer algorithm.
We maintain two pointers , one is used for the traversal of the array while the other pointer points the boundary, 
of 1(s) in the array. (All the ones must come after the 0s)

The running time complexity of this algorithm is O(n). (where n is the size of the array)
'''

arr = [int(x) for x in input().split()]

rightpointer = len(arr)
i = 0

while i < rightpointer :
	if arr[i] == 1:
		arr[i], arr[rightpointer - 1] = arr[rightpointer - 1], arr[i]
		rightpointer -= 1

	else :
		i += 1

print(arr)