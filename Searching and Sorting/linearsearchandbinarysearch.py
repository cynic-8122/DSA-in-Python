def linear_search(arr, target):
	idx = -1
	for i in range(len(arr)):
		if arr[i] == target :
			idx = i 
			break

	return idx

def binary_search(arr, left, right, target):
	idx = -1

	while left < right :
		mid = (left + right)//2

		if arr[mid] == target :
			idx = mid
			break

		if arr[mid] > target :
			right = mid - 1

		else :
			left = mid + 1

	return idx

print("Enter the array you want to search : ")
arr1 = [int(x) for x in input().split()]

T = int(input("Enter the target element "))

idx = linear_search(arr1, T)
if idx == -1 :
	print(f"The element was not found in the array ")

else :
	print(f"The element {T}, was found at index = {idx} ")

print("For binary search we need a sorted array, so the array now becomes")
arr1.sort()
print(arr1)

idx = binary_search(arr1, 0, len(arr1) - 1, T)

if idx == -1 :
	print(f"The element was not found in the array ")

else :
	print(f"The element {T}, was found at index = {idx} ")