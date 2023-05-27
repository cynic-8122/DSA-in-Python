'''
This algorithm does not use any extra space.
The running time complexity of this algorithm is O(n). (where n is the size of the array)
'''

def reversearray(arr):
	i = 0
	j = len(arr) - 1

	while i <= j:
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1

arr = [int(x) for x in input().split()]

reversearray(arr)
print(arr)