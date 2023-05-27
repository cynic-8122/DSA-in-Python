def reversethegroups(arr, n, k):
	t = n - 1

	while t > 0:
		otheridx = t - k + 1

		if otheridx < 0 :
			break

		reverse(arr, otheridx, t)

		t -= k 

	print(arr)

def reverse(arr, i, j):
	while i <= j:
		arr[i], arr[j] = arr[j], arr[i]
		i += 1
		j -= 1


arr = [int(x) for x in input().split()]
k = int(input())
reversethegroups(arr, len(arr), k)