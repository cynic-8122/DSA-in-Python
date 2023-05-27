def check_first_occurence(arr, x, i = 0):
	L = len(arr)
	if i == L :
		return False
	if i == L - 1 and arr[i] == x:
		return i
	if arr[i] == x :
		return i
	return check_first_occurence(arr, x, i + 1)


arr = [int(x) for x in input().split()]
x = int(input())
print(check_first_occurence(arr, x))


