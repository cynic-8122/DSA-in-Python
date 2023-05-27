def last_occurence(arr, x, l):
	if l == 0 :
		return -1

	if arr[l - 1] == x :
		return l - 1 

	return last_occurence(arr, x, l - 1)

l = int(input())
arr = [int(x) for x in input().split()]
x = int(input())
print(last_occurence(arr, x, l))