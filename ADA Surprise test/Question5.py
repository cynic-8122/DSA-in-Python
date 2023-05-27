
def printallcombinations(arr, r, ansarr):
	if r < 0 :
		return

	if r == 0 :
		print(ansarr)
		return

	if len(arr) == 0:
		return

	temp = ansarr
	ele = arr[0]
	newcombination = temp.append(ele)

	printallcombinations(arr[1:], r - 1, newcombination)
	printallcombinations(arr[1:], r, ans)

arr = [int(x) for x in input().split()]
r = int(input())

printallcombinations(arr, r)

