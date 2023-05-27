
def minjumps(arr, n) :

	maxreach = arr[0]

	steps = maxreach
	jumps = 0
	for i in range(1, len(arr)):
		maxreach = max(maxreach, arr[i] + 1)

		steps -= 1
		if steps == 0 :
			jumps += 1
			steps = maxreach - i 


	return jumps + 1

arr = [int(x) for x in input().split()]
print(minjumps(arr, len(arr)))
