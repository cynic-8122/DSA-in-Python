def last_occurence_of_x(arr, x, i = 0):
	l = len(arr)
	if i == l :
		return -1

	ans = last_occurence_of_x(arr, x, i + 1)
	if arr[i] == x and ans == -1:
		return i

	else :
		return ans 

arr = [int(x) for x in input().split()]
x = int(input())
print(last_occurence_of_x(arr, x))


